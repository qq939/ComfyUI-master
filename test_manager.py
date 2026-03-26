import os
import sys
import time
import subprocess

def check_manager_installed():
    manager_dir = os.path.join("custom_nodes", "ComfyUI-Manager")
    return os.path.isdir(manager_dir)

def test_manager_installation():
    print("Testing for ComfyUI Manager installation...")
    
    if check_manager_installed():
        print("ComfyUI Manager is installed.")
        sys.exit(0)
    else:
        print("ComfyUI Manager is not installed.")
        sys.exit(1)

if __name__ == "__main__":
    test_manager_installation()
