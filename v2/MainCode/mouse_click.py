import threading
import pyautogui
import time

class MouseMonitor:
    def __init__(self, idle_time=2):
        self.idle_time = idle_time
        self.last_position = pyautogui.position()
        self.idle_start_time = time.time()
        self.running = True

    def monitor_mouse(self):
        while self.running:
            current_position = pyautogui.position()
            current_time = time.time()

            if current_position == self.last_position:
                if current_time - self.idle_start_time >= self.idle_time:
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
