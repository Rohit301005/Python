# import a thread class
from threading import Thread,current_thread

# create a function and write code to exectue parallaly
def display(n,msg):
    print("t1 thread details :" , current_thread())
    print("t1 thread details :" , current_thread().name)
    print("t1 thread details :" , current_thread().ident)
    print("t1 thread details :" , current_thread().is_alive())
    for i in range(n):
        print(msg)

# creat a new thread
# t1 = Thread(target=display,args=(4, "Hello!"))
t1 = Thread(target=display, kwargs={'n' : 6, 'msg' : "Rohit"})

# start the new thread
t1.start()



# for i in range(4):
#     print('vc')