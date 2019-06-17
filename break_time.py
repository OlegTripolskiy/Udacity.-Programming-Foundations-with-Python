import webbrowser
import time

print("The program is started at %s" % time.ctime())
for count in range(3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=EIxsPBbZ_b8")
