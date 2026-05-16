import argparse
import json
from src.core import EntityBench

def main():
    parser = argparse.ArgumentParser(description='EntityBench')
    parser.add_argument('--input', type=str, help='input video file')
    parser.add_argument('--output', type=str, help='output video file')
    args = parser.parse_args()
    entity_bench = EntityBench()
    entity_bench.run(args.input, args.output)

if __name__ == '__main__':
    main()