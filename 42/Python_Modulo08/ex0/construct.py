# ejectc python /home/dalopez3/python08/ex0/construct.py
# python3 -m venv matrix_env install entorn
# source matrix_env/bin/activate activate
import sys
import os
import site

in_venv = sys.prefix != sys.base_prefix
env_path = sys.prefix
env_name = os.path.basename(env_path)

if in_venv:
    print("MATRIX STATUS: Welcome to the construct")
    print("Current Python:", sys.executable)
    print("Environment Path:", sys.prefix)
    print("Virtual Environment:", env_name)
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path:")
    print()
    for path in site.getsitepackages():
        if "site-packages" in path:
            print(path)
            break

else:
    print("MATRIX STATUS: You're still plugged in")
    print("Current Python:", sys.executable)
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
