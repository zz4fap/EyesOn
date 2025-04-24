import threading
import time

# Define the function that the thread will run
def count_to_five():
    for i in range(1, 6):
        print(f"Count: {i}")
        time.sleep(0.2)  # Sleep for 1 second

# Create a Thread object
thread = threading.Thread(target=count_to_five)


thread.start()

for i in range(5):
    print(i)
thread.join()

for i in range(7, 10):
    print(i)

print("Counting finished.")
