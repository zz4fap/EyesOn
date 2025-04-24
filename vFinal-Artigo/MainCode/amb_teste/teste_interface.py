import threading
from MainCode.interfacev4 import new_interface



t = threading.Thread(target=new_interface.main)
t.start()