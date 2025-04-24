import threading
import pyautogui
import time
import l2cs.vis as vis

class MouseMonitor_teste:
    def __init__(self, general_time=3, browse_time=3, browse_on=False, dx=vis.dx_global, dy=vis.dy_global):
        self.general_time = general_time
        self.browse_time = browse_time
        self.browse_on = browse_on
        self.dx = dx
        self.dy = dy
        self.last_position = pyautogui.position()
        self.idle_start_time = time.time()
        self.running = True

    def monitor_mouse(self):
        while self.running:
            current_position = pyautogui.position()
            current_time = time.time()

            if current_position == self.last_position and self.browse_on == False:
                if current_time - self.idle_start_time >= self.general_time:
                    pyautogui.click()
                    self.idle_start_time = current_time  # Reset the idle start time after clicking
            elif self.browse_on:
                if self.dx <= -50 and self.dy <= 30:
                    print(self.dx, self.dy)
                    if current_time - self.idle_start_time >= self.browse_time:
                        pyautogui.click()
                        self.idle_start_time = current_time  # Reset the idle start time after clicking

            else:
                self.last_position = current_position
                self.idle_start_time = current_time

            time.sleep(0.1)  # Check every 100 milliseconds

    def start(self):
        self.thread = threading.Thread(target=self.monitor_mouse)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()
