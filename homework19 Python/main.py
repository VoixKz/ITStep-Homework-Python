import time
import threading

def create_file(filename):
    time.sleep(1)
    with open(filename, 'w') as f:
        f.write("English or Spanish?")
    print(f"Файл {filename} создан.")

start_time = time.time()
for i in range(100):
    create_file(f"./homework19 Python/files/file_{i}.txt")
end_time = time.time()
print(f"Время выполнения без многопоточности: {end_time - start_time} секунд.")

start_time = time.time()
threads = []
for i in range(100):
    thread = threading.Thread(target=create_file, args=(f"./homework19 Python/files/file_{i}.txt",))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
end_time = time.time()
print(f"Время выполнения с многопоточностью: {end_time - start_time} секунд.")