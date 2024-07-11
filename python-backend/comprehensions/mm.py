import threading

def my_callback():
    print("Timer expired! Callback executed.")

# Schedule the callback to be called after 2 seconds
timer = threading.Timer(2.0, my_callback)
timer.start()

