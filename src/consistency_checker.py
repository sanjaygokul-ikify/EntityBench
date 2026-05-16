import json

class ConsistencyChecker:
    def __init__(self):
        self.graph = {
            'entities': []
        }
    
    def check(self, detected_entities):
        # check consistency using the graph-based approach
        return consistency_score
