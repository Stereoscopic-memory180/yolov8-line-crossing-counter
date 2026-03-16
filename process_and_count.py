from ultralytics import YOLO
import cv2
import os
from datetime import datetime
import time




def draw_corner_box(img, x1, y1, x2, y2, color=(0,255,0), thickness=1):

    w = x2 - x1
    h = y2 - y1

    line_w = int(w * 0.25)
    line_h = int(h * 0.25)

    # top left
    cv2.line(img,(x1,y1),(x1+line_w,y1),color,thickness)
    cv2.line(img,(x1,y1),(x1,y1+line_h),color,thickness)

    # top right
    cv2.line(img,(x2,y1),(x2-line_w,y1),color,thickness)
    cv2.line(img,(x2,y1),(x2,y1+line_h),color,thickness)

    # bottom left
    cv2.line(img,(x1,y2),(x1+line_w,y2),color,thickness)
    cv2.line(img,(x1,y2),(x1,y2-line_h),color,thickness)

    # bottom right
    cv2.line(img,(x2,y2),(x2-line_w,y2),color,thickness)
    cv2.line(img,(x2,y2),(x2,y2-line_h),color,thickness)


video_path = "video/input.mp4"
output_path = "output/counting_video.mp4"

model = YOLO("yolov8s.pt")

cap = cv2.VideoCapture(video_path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)


camera_id = "CAM 01"
prev_time = 0

line_y = height // 2

os.makedirs("output", exist_ok=True)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# tracking memory
previous_positions = {}

# counting
count = 0
counted_ids = set()

while True: 
    ret, frame = cap.read()
    if not ret:
        break
    
    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
    prev_time = current_time

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    
    

    # ---- Top CCTV header ----
    cv2.putText(frame, camera_id, (10,25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                (255,255,255), 1)

    cv2.putText(frame, timestamp, (width-260,25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                (255,255,255), 1)

    cv2.putText(frame, f"FPS {fps:.1f}", (width-100,55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                (255,255,255), 1)


    # YOLO + tracking
    results = model.track(frame, persist=True)


    # Create overlay for transparent counting line
    line_overlay = frame.copy()

    # Draw red counting line on overlay
    cv2.line(line_overlay, (0, line_y), (width, line_y), (0,0,255), 2)

    # Draw arrow on overlay
    arrow_x = 60

    cv2.arrowedLine(line_overlay,
                    (arrow_x, line_y - 20),
                    (arrow_x, line_y + 20),
                    (0,0,255),
                    2,
                    tipLength=0.4)


    # Blend overlay with original frame
    alpha_line = 0.3
    frame = cv2.addWeighted(line_overlay, alpha_line, frame, 1-alpha_line, 0)

    

    # get detected classes (extract Person) and bbox coordinates from Yolo
    for r in results:
        for box in r.boxes:

            if box.id is None:
                continue

            cls = int(box.cls[0])

            if cls != 0:
                continue

            track_id = int(box.id[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            # draw corner bounding box
            draw_corner_box(frame, x1, y1, x2, y2)

            # centroid
            cv2.circle(frame,(cx,cy),2,(0,255,0),-1)

            # ID label
            cv2.putText(frame,
                        f"ID {track_id}",
                        (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.40,
                        (0,255,0),
                        1)

            # previous positions
            if track_id in previous_positions:

                prev_cy = previous_positions[track_id]

                # line cross detection
                if prev_cy < line_y and cy >= line_y:

                    if track_id not in counted_ids:

                        count += 1
                        counted_ids.add(track_id)

            previous_positions[track_id] = cy


   # Create overlay for transparent counter panel
    overlay = frame.copy()

    # Panel position and size
    panel_x1, panel_y1 = 10, 80
    panel_x2, panel_y2 = 230, 165

    # Draw panel background
    cv2.rectangle(overlay, (panel_x1, panel_y1), (panel_x2, panel_y2), (0,0,0), -1)

    # Apply transparency
    alpha = 0.5
    frame = cv2.addWeighted(overlay, alpha, frame, 1-alpha, 0)

    # Draw white border
    cv2.rectangle(frame, (panel_x1, panel_y1), (panel_x2, panel_y2), (255,255,255), 1)

    # Label
    cv2.putText(frame,
                "DETECTED ENTRIES",
                (panel_x1 + 12, panel_y1 + 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (255,255,255),
                1)

    # Counter value
    cv2.putText(frame,
                f"{count}",
                (panel_x1 + 12, panel_y1 + 75),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (255,255,255),
                1)
    
    out.write(frame)

cap.release()
out.release()

print("Counting video saved:", output_path)