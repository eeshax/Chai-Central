import time
def countdown(time_sec):
    while time_sec:
        mins, sec = divmod(time_sec, 60)
        print(mins, sec)
        time.sleep(1)
        time_sec -= 1

countdown(10)

for i in range(variable_name):
    exec("%s = %d" % (x,2))
