# SIH24
It is a group based project

# Plant Health Detection App

## Overview

The Plant Health Detection App is a Flask-based web application that utilizes YOLOv6 for object detection and plant health analysis. Users can upload images of plants, and the application will detect objects in the images and provide detailed information about detected classes, including precautions, avoidance measures, and cures for plant health issues.

## Features

- Upload and process images to detect plant-related objects.
- Display detailed information about detected classes.
- View images with bounding boxes around detected objects.
- Resize images on-the-fly.

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)
- OpenCV (`cv2`)
- YOLOv6 model file (`best_ckpt.onnx`)

### Clone the Repository

```bash
git clone https://github.com/yourusername/plant-health-detection-app.git
cd plant-health-detection-app
