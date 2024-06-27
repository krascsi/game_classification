from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n-cls.pt")  # load an official model
model = YOLO("/home/krascsi/Projects/yolov8_game_classification/runs/classify/train2/weights/best.pt")  # load a custom trained model

# Export the model
model.export(format="onnx")
