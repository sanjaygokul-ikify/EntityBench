import cv2
import torch

class EntityDetector:
    def __init__(self):
        self.model = torch.load('entity_detector.pth')
    
    def detect(self, input_video):
        # detect entities using the loaded model
        return detected_entities
