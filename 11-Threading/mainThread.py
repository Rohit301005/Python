# threads are python object of threading.Thread() class
import threading as th

print(th.current_thread())
print(th.current_thread().name)
print(th.current_thread().ident)
print(th.current_thread().is_alive())