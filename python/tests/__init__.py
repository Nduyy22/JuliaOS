# DeFi Guardian Swarm Tests Package
import sys
import os

# Add project paths to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
python_src_path = os.path.join(project_root, 'python', 'src')
python_scripts_path = os.path.join(project_root, 'python', 'scripts')

if python_src_path not in sys.path:
    sys.path.insert(0, python_src_path)
if python_scripts_path not in sys.path:
    sys.path.insert(0, python_scripts_path)
