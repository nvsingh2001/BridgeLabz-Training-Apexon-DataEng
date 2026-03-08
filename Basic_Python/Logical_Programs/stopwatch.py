import time

input("Press Enter to Start the stopwatch...")
start_time = time.time()

print("Stopwatch Started")

input("Press Enter to Stop the stopwatch...")
end_time = time.time()

elapsed_time = end_time - start_time

hours = int(elapsed_time // 3600)
minutes = int((elapsed_time % 3600) // 60)
seconds = elapsed_time % 60

print(f"Elapsed Time: {hours:02} : {minutes:02} : {seconds:05.2f}")
