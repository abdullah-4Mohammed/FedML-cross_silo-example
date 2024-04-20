import sys
import os
import subprocess

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

print(sys.executable)
print(sys.version)

# Construct the path to torch_server.py
torch_server_path = os.path.join(current_dir, "server", "torch_server.py")

# Run torch_server.py with subprocess
subprocess.run([sys.executable, torch_server_path, "--cf", "config/fedml_config.yaml", "--rank", "0", "--run_id", "123"])
