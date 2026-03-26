import json
import os
import sys

def test_json_validity():
    filename = "工业yolo识别加框加置信度.json"
    print(f"Testing validity of {filename}...")
    
    if not os.path.exists(filename):
        print(f"Error: {filename} does not exist.")
        sys.exit(1)
        
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print("JSON is valid.")
            
            # Check for essential ComfyUI keys
            if "nodes" not in data or "links" not in data:
                print("Error: JSON is missing 'nodes' or 'links' keys.")
                sys.exit(1)
            
            print(f"Found {len(data['nodes'])} nodes and {len(data['links'])} links.")
            sys.exit(0)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_json_validity()
