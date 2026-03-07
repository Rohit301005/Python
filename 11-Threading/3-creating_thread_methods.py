import threading   #ya bi correct h
# from threading import Thread #ya bi correct h

class Example:

    def display(self,n):
        print("t1 details:", threading.current_thread())

        for i in range(n):
            print("Rohit")
# creating object of Example class
e1 = Example()

# creating a new thread
t1 = threading.Thread(target=e1.display,args=(4,))

# startinng the new thread
t1.start()

# print(threading.current_thread()) #main thread details


for i  in range(4):
    print("WELLCOME!")
