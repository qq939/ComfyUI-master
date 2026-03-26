import subprocess
import time
import socket
import sys
import os

def is_port_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False

def test_6003_port():
    port = 6003
    print(f"Testing port {port}...")
    
    # Start ComfyUI in the background
    # We use --listen 127.0.0.1 to ensure it's local for the test
    cmd = [sys.executable, "main.py", "--port", str(port), "--listen", "127.0.0.1"]
    
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    start_time = time.time()
    timeout = 120  # 120 seconds timeout to be safe
    
    success = False
    try:
        while time.time() - start_time < timeout:
            if is_port_open("127.0.0.1", port):
                print(f"Port {port} is open!")
                success = True
                break
            time.sleep(5) # Increase sleep to reduce overhead
            if process.poll() is not None:
                print("Process exited prematurely")
                break
    finally:
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()

    if success:
        print("Test passed!")
        sys.exit(0)
    else:
        print("Test failed: Port 6003 did not open within timeout.")
        sys.exit(1)

if __name__ == "__main__":
    test_6003_port()
