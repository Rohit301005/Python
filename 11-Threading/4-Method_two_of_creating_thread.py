from time import sleep
from threading import Thread

videos = ["OOPS","Constructor","Destructor","File Handling"]

class MyClass(Thread):

    def __init__(self):
        # super().__init__() #this is also correct
        Thread.__init__(self) #also correct
        print("this is a constructor call")

    def run(self):
        for vid in videos:
            print(f"{vid} start  uploading")
            sleep(3)
            print(f"{vid} uploaded")

t1 = MyClass()
t1.start()

for i in range(4):
    sleep(0.5)
    print("checking copyrights")





