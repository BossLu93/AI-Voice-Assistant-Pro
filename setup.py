import subprocess

print("THIS MAY TAKE A WHILE DEPENDING ON YOUR SYSTEM AND INTERNET SPEED\n\nPLEASE WAIT..\n\n")

try:
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
except