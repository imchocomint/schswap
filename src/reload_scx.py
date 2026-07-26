import subprocess
def reload_scx(scheduler):
    subprocess.run([f"scxctl switch --sched {scheduler}"], shell=True, check=True)
def showstatus():
    subprocess.run(["scxctl get"], shell=True, check=True)