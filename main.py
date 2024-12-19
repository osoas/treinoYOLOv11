from ultralytics import YOLO

model = YOLO('yolo11n.pt') 

model.train(data='acne04-1/data.yaml', epochs=50, imgsz=640)

results = model.val()

