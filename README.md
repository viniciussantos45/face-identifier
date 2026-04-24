# face-identifier

A real-time **face detection** application using Python and OpenCV's Haar Cascade classifier.

## Objective

The objective of this project is to detect human faces from a live webcam feed, draw bounding boxes around detected faces, and display the annotated video stream — demonstrating basic computer vision with OpenCV.

## How it works

1. The webcam is opened at 320×240 resolution.
2. Each frame is converted to grayscale.
3. A pre-trained Haar Cascade classifier (`haarcascade_frontalface_alt2.xml`) detects faces.
4. Red rectangles are drawn around each detected face.
5. The annotated frame is displayed in a window. Press `q` to quit.

## Tech Stack

- Python 3
- OpenCV (`cv2`)

## Getting Started

```bash
pip install opencv-python

# Run the detector
python index.py
```
