import time

seconds = time.time()
print("Seconds since January 1, 1970:", f"{seconds:,}"," or", f"{seconds:e}", "in scientific notation")
print(time.strftime("%b %d %Y"))