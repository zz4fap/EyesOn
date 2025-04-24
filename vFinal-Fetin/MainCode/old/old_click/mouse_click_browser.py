import threading
import pyautogui
import time
import l2cs.vis as vis

class MouseMonitor_browser:
    def __init__(self,browse_time=3, browse_on=False, dx=vis.dx_global, dy=vis.dy_global):
        self.browse_time = browse_time
        self.browse_on = browse_on
        self.last_position = pyautogui.position()
        self.idle_start_time = time.time()
        self.dx = dx
        self.dy = dy
        self.running = True

    def monitor_mouse_browser(self):
        while self.running:
            current_position = pyautogui.position()
            current_time = time.time()

            if self.dx <= -50 and self.dy <= 30:
                if current_time - self.idle_start_time >= self.browse_time:
                    pyautogui.click()
                    self.idle_start_time = current_time  # Reset the idle start time after clicking
            else:
                self.last_position = current_position
                self.idle_start_time = current_time

            time.sleep(0.1)  # Check every 100 milliseconds

    def start(self):
        self.thread = threading.Thread(target=self.monitor_mouse_browser())
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()
