from datetime import datetime

def log(message):

    time = datetime.now().strftime("%H:%M:%S")

    with open("data/logs.txt", "a") as f:
        f.write(f"[{time}] {message}\n")