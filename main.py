from ultralytics import YOLO
import cv2

# 1. โหลดโมเดล (เบา + เร็ว เหมาะสาธิต)
model = YOLO("yolov8n.pt")

# 2. โหลดภาพ
img = cv2.imread("../image/majo.png")

# 3. ตรวจจับวัตถุ
results = model(img)

# 4. วาดผลลัพธ์ลงบนภาพ
annotated_img = results[0].plot()

# 5. แสดงผล
cv2.imshow("YOLO Detection", annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. บันทึกภาพผลลัพธ์
cv2.imwrite("result.jpg", annotated_img)
