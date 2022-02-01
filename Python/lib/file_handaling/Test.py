import subprocess

with open("output.txt", "w") as f:
    subprocess.check_call(["python", "File.py"], stdout=f)
    print(f.fileno())
