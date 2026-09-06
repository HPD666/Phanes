import cv2
from ultralytics import YOLO
from duckduckgo_search import DDGS
import numpy as np

# Load local open-source vision model
model = YOLO('yolov8n.pt')
ddgs = DDGS()

def get_product_info(query):
    """Scrapes free public info/prices without paid APIs."""
    try:
        results = list(ddgs.text(f"{query} buy price description", max_results=1))
        if results:
            snippet = results[0]['body']
            title = results[0]['title']
            return title[:40], snippet[:80]
    except Exception:
        pass
    return f"{query.upper()} DETECTED", "Target locked. No pricing data available."

cap = cv2.VideoCapture(0)
cache = {}

print("Starting Cyberpunk Scanner... Press 'q' to exit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO real-time visual detection
    results = model(frame, conf=0.5, verbose=False)

    for r in results:
        for box in r.boxes:
            # Extract coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            item_name = model.names[cls_id]

            # Fetch product details if not already cached
            if item_name not in cache:
                cache[item_name] = get_product_info(item_name)
            
            title, desc = cache[item_name]

            # --- Draw Cyberpunk HUD Interface ---
            # Neon Cyan Bounding Box & Corner Accents
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
            cv2.circle(frame, (x1, y1), 5, (0, 255, 255), -1)
            cv2.circle(frame, (x2, y2), 5, (0, 255, 255), -1)

            # Floating HUD Banner
            overlay = frame.copy()
            cv2.rectangle(overlay, (x1, y1 - 60), (x1 + 320, y1), (15, 15, 15), -1)
            cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)

            # Yellow/Cyan Cyberpunk Text Overlay
            cv2.putText(frame, f"[SCAN]: {title}", (x1 + 5, y1 - 38),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 255), 1)
            cv2.putText(frame, f"INFO: {desc}...", (x1 + 5, y1 - 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)

    cv2.imshow("PHANES // HUD SCANNER v1.0", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
