# EntityBench
## Introduction
EntityBench is a tool for evaluating and generating entity-consistent long-range multi-shot videos.
## Problem Statement
Maintaining consistent characters, objects, and locations across shots in long sequences remains a challenge in video generation.
## Why it Matters
Entity-consistent video generation has various applications in film, gaming, and advertising industries.
## Architecture
```mermaid
graph LR
    A[Video Input] -->|Processed| B[Entity Detector]
    B -->|Detected Entities| C[Consistency Checker]
    C -->|Consistency Score| D[Video Generator]
    D -->|Generated Video| E[Output]
```
## Project Structure
```
entitybench/
|---- README.md
|---- CONTRIBUTING.md
|---- requirements.txt
|---- main.py
|---- src/
|       |---- core.py
|       |---- entity_detector.py
|       |---- consistency_checker.py
|       |---- video_generator.py
```
## Installation Steps
1. Clone the repository: `git clone https://github.com/your-repo/entitybench.git`
2. Install dependencies: `pip install -r requirements.txt`
## Quick Start
1. Run the entity detector: `python src/entity_detector.py -i input_video.mp4`
2. Run the consistency checker: `python src/consistency_checker.py -i detected_entities.json`
3. Run the video generator: `python src/video_generator.py -i consistency_score.json`
## Configuration
Configure the entity detector and consistency checker in `config.json`.
## Design Decisions
The entity detector uses a convolutional neural network (CNN) architecture, while the consistency checker utilizes a graph-based approach.
## Roadmap
1. Improve entity detection accuracy
2. Enhance consistency checking algorithm
3. Optimize video generation performance
## Contribution
See `CONTRIBUTING.md` for guidelines.
## License
EntityBench is licensed under the MIT License.