# PHANES // Vision System

![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)
![Technology](https://img.shields.io/badge/Tech-TensorFlow.js-orange.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)

PHANES is a web-based computer vision and real-time object tracking system built using TensorFlow.js. It runs client-side inside modern web browsers, detecting target geometries, track boundaries, and biometric inputs through a web camera feed.

---

## Key Features

- **Real-Time Detection Engine**: Powered by client-side WebGL acceleration using TensorFlow.js (`mobilenet_v2`).
- **Integrated Biometric Tracking**: BlazeFace module for facial landmarking and continuous tracking.
- **HUD Interface**: Futuristic heads-up display overlay rendered via Canvas API with smooth spatial interpolation.
- **Zero-Dependency Installation**: Runs completely client-side in standard modern web browsers without complex server setups or dependencies.

---

## Tech Stack

- **Frontend**: HTML5, Modern Canvas API, CSS3
- **Machine Learning**: TensorFlow.js
- **Detection Models**: MobileNet V2 (COCO-SSD), BlazeFace
- **Typography**: Google Fonts (Share Tech Mono)

---

## Quick Start / Installation

1. Clone or download this repository:
   ```bash
   git clone [https://github.com/your-username/phanes-vision-system.git](https://github.com/your-username/phanes-vision-system.git)
