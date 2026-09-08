# PHANES // Vision System

A futuristic, high-performance web-based computer vision dashboard and real-time object tracking environment. Running completely client-side in modern web browsers, the system provides instantaneous geometric tracking overlays, spatial metrics, and automated market valuation logic directly from raw camera streams.

Live Environment: https://hpd666.github.io/phanes/

## Key System Architecture

* **Accelerated Browser Inference**: Employs client-side WebGL pipelining via TensorFlow.js to run hardware-accelerated computer vision models smoothly on desktop and mobile browsers.
* **Dual-Model Processing Pipeline**: Optimized to ingest a secondary hidden viewport resolution (640x480) to maximize real-time structural and feature classification matrix accuracies.
* **Dynamic Spatial HUD**: Real-time bounding data rendered via low-latency Canvas API execution paths paired with responsive UI panel alerts based on tracking locks.
* **Valuation & Search Interpolation**: Translates real-time geometric visual targets into programmatic retail classification bounds, establishing automated pricing approximations and context-aware online marketplace redirects.

## Tech Stack & Dependencies

The codebase operates with zero build configurations, retrieving optimized runtimes entirely via official CDN distribution nodes:

* **Core Engine**: TensorFlow.js Core Vector Framework (@tensorflow/tfjs)
* **Detection Matrices**: MobileNet V2 COCO-SSD Pipeline (@tensorflow-models/coco-ssd)
* **Biometric Sub-Engine**: BlazeFace Landmark Predictor Matrix (@tensorflow-models/blazeface)
* **Interface Layer**: Modern HTML5 Semantic Structures, Canvas API Intermediary, CSS3 Root Variables Architecture

## Production Structure

The application is structured inside a highly optimized, localized single-file architecture to eliminate server-side routing overhead and CORS blocks on standard pipelines:

├── index.html       # Combined core markup, real-time UI styles, and logic processing scripts
└── LICENSE          # AGPL v3 / GPL v3 Open Source Distribution Terms

## Local Execution and Development

Because the platform operates entirely client-side, you do not need complex backend local environments, node stacks, or configuration trees to run it locally.

### 1. Retrieve Project File Assets
Save your index file locally or pull the assets directory structure directly using Git:
```bash
git clone https://github.com/HPD666/phanes.git
cd phanes
```

### 2. Launch Local Port Runtime
Due to browser camera access permissions, executing files via standard filepaths (file:///) may cause hardware blockages. Launch using any lightweight static file runner:

**Using Python 3:**
```bash
python -m http.server 8000
```
Open your browser and direct traffic to: http://localhost:8000

**Using Node.js (http-server):**
```bash
npx http-server -p 8000
```
Open your browser and direct traffic to: http://localhost:8000

## System Operations & HUD Controls

1. **Camera Permissions**: Grant standard hardware webcam input access requests when prompted by the web UI runtime.
2. **System Initialization**: The top-left HUD state monitor displays INITIALIZING SYSTEM... while loading remote target model weight structures into storage.
3. **Locking Target Profiles**: Position an object or face into clear camera frame orientation lines. Once model prediction thresholds clear, the interface instantly initializes a bright tracking boundary.
4. **Data Analytics Monitoring**: The real-time bottom-right analytical pane populates contextual parameters detailing classifications, precision percentages, dimensions, and estimated market values.
5. **Market Integrations**: Selecting the highlighted SEARCH / FIND ITEM ONLINE button instantly launches targeted marketplace index search operations mapping directly to the tracked entity target profile.
