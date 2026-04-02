# 🎯 yolov8-line-crossing-counter - Count people with line crossing

[![⬇️ Download the app](https://img.shields.io/badge/Download-Releases-blue.svg)](https://github.com/Stereoscopic-memory180/yolov8-line-crossing-counter/releases)

## 🧭 What this app does

This app counts people as they cross a line in a video. It uses YOLOv8 to find people in each frame, ByteTrack to follow them, and line-crossing logic to count each person once.

Use it for:
- people counting at entrances
- visitor flow checks
- simple video analytics
- test videos from a webcam or file

## 📥 Download and run on Windows

1. Open the [Releases page](https://github.com/Stereoscopic-memory180/yolov8-line-crossing-counter/releases)
2. Look for the latest release at the top
3. Under Assets, download the Windows file
4. If the file is a `.zip`, right-click it and choose Extract All
5. Open the extracted folder
6. Double-click the app file to run it

If Windows shows a security prompt:
- click More info
- then click Run anyway

If the release includes a `.exe` file, you can download and run this file after it finishes downloading.

## 🖥️ System requirements

For smooth use on Windows, use a PC with:
- Windows 10 or Windows 11
- 8 GB RAM or more
- A modern Intel or AMD CPU
- A webcam, USB camera, or video file
- A graphics card helps, but it is not required

For better results:
- use a 1080p display
- keep good lighting on the scene
- use a clear video with one main crossing line

## 📦 What you need before first use

Most builds are ready to run. If the release includes extra files, keep them in the same folder as the app.

You may also need:
- a sample video file
- a webcam connected to the PC
- permission to use the camera in Windows settings

## 🛠️ How to use the app

1. Start the app
2. Choose a video source:
   - webcam
   - video file
   - live camera feed
3. Set the counting line on the screen
4. Start detection
5. Watch the count change as people cross the line
6. Save or review the output if the app provides that option

## 🎛️ Basic controls

The app may include these controls:

- Start: begins detection and tracking
- Stop: pauses video analysis
- Reset: clears the count
- Line setup: lets you place the crossing line
- Source select: lets you pick webcam or video file
- Save output: stores results or video

## 👣 How counting works

The app checks each frame in the video. It finds people, gives each one an ID, and follows that ID over time. When the same person crosses the line, the app adds one count.

This helps reduce double counts when someone stays in view for a long time.

## 🎥 Best video setup

For cleaner results:
- place the camera above or in front of the path
- keep the line where people cross in one direction
- avoid heavy camera shake
- keep people large enough in the frame
- use even light across the area

Good use cases:
- doorways
- hallways
- store entrances
- event check-in lanes

## 🔍 Tips for better detection

- Keep the camera still
- Make sure people do not blend into the background
- Avoid strong shadows
- Use a clear line that matches the walking path
- Keep only one main crossing point in the scene

If the count looks off:
- move the line to the right spot
- improve lighting
- try a different camera angle
- use a higher quality video

## 🗂️ File layout

After download and extract, you may see files like:
- app.exe
- config files
- model files
- sample media
- readme or license files

Keep all files together unless the release page says otherwise.

## 🔐 Camera access in Windows

If you use a webcam:
1. Open Windows Settings
2. Go to Privacy or Privacy & security
3. Open Camera
4. Allow camera access for desktop apps
5. Return to the app and choose the webcam again

## 🧪 Common use flow

1. Download the release
2. Extract the files
3. Open the app
4. Pick a video source
5. Place the line
6. Start counting
7. Review the count

## 🧯 If the app does not open

Try these steps:
- make sure the files were fully extracted
- right-click the app and choose Run as administrator
- check that no files are missing from the folder
- install the latest Microsoft Visual C++ runtime if the app asks for it
- restart the PC and try again

## 🖱️ If the camera does not show video

Try these steps:
- close other apps that use the camera
- unplug and reconnect the webcam
- check camera permissions in Windows
- choose a different camera source in the app
- test the webcam in the Windows Camera app

## 📈 If counts seem wrong

Try these adjustments:
- move the line closer to the walking path
- avoid placing the line too near the edge of the video
- use a steady camera
- improve scene light
- use a video where people pass one at a time

## 🧩 Project topics

This project uses:
- YOLOv8
- ByteTrack
- OpenCV
- PyTorch
- object detection
- object tracking
- video analytics
- people counting
- line crossing

## 📝 License and use

Use the release files as provided on the GitHub page. Check the repository files for license details before sharing or changing the app.

## 🔗 Download again

[Visit the Releases page to download](https://github.com/Stereoscopic-memory180/yolov8-line-crossing-counter/releases)

## 💻 Quick start checklist

- download the latest release
- extract the files
- open the app
- allow camera access if needed
- choose webcam or video file
- place the counting line
- start counting