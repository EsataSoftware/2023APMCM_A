from ultralytics import YOLO
if __name__ == '__main__':

    # 加载模型
    model = YOLO('yolov8l-cls.yaml')  # 从YAML构建新模型
    model = YOLO('yolov8l-cls.pt')  # 加载预训练模型（推荐用于训练）
    model = YOLO('yolov8l-cls.yaml').load('yolov8l-cls.pt')  # 从YAML构建并转移权重

    # 训练模型
    results = model.train(data='/home/yolov8/fruit', epochs=500,imgsz=220)