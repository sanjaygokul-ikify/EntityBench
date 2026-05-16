import cv2
import torch

class EntityBench:
    def __init__(self):
        self.entity_detector = EntityDetector()
        self.consistency_checker = ConsistencyChecker()
        self.video_generator = VideoGenerator()
    
    def run(self, input_video, output_video):
        detected_entities = self.entity_detector.detect(input_video)
        consistency_score = self.consistency_checker.check(detected_entities)
        generated_video = self.video_generator.generate(consistency_score)
        cv2.imwrite(output_video, generated_video)
