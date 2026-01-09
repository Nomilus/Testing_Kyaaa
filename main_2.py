import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("../videos/one_last_kiss.mp4")
if not cap.isOpened():
    print("❌ เปิดวิดีโอไม่ได้")
    exit()
unique_ids = set()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model.track(
        frame,
        conf=0.3,
        persist=True,
        verbose=False
    )
    annotated_frame = results[0].plot()
    if results[0].boxes.id is not None:
        ids = results[0].boxes.id.cpu().numpy()
        for obj_id in ids:
            unique_ids.add(int(obj_id))
    total_objects = len(unique_ids)
    cv2.putText(
        annotated_frame,
        f"Total unique objects: {total_objects}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )
    cv2.imshow("YOLO Unique Object Counting", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
