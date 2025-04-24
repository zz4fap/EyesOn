import threading
import pyautogui
import time

class MouseMonitor:
    def __init__(self, region, idle_time=3):
        self.region = region
        self.idle_time = idle_time
        self.idle_start_time = None
        self.running = True

    def monitor_mouse(self):
        while self.running:
            current_position = pyautogui.position()
            if self.is_within_region(current_position):
                print("WITHIN THE REGION")
                if self.idle_start_time is None:
                    self.idle_start_time = time.time()
                elif time.time() - self.idle_start_time >= self.idle_time:
                    pyautogui.click()
                    self.idle_start_time = None  # Reset the idle start time after clicking
            else:
                self.idle_start_time = None

            time.sleep(0.1)  # Check every 100 milliseconds

    def is_within_region(self, position):
        x, y = position
        x1, y1, width, height = self.region
        return x1 <= x <= x1 + width and y1 <= y <= y1 + height

    def start(self):
        self.thread = threading.Thread(target=self.monitor_mouse)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()
