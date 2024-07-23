import time, threading
from random import randint

filename = './homework20 Python/file.txt'
open(filename, 'w').close()
print(f'File {filename} created')
def create_file_with_randint():
    time.sleep(1)
    with open(filename, 'a') as file:
        file.write(str(randint(1, 100))+'\n')
    
start_time = time.time()
for i in range(100): #сори, ну ждать 1000 секунд для обычного - слишком долго, 
                     #а delay в 1 секунду я уменьшать не хочу
    create_file_with_randint()
end_time = time.time()
print(f"Время выполнения без многопоточности: {end_time - start_time} секунд.")

start_time = time.time()
threads = []
for i in range(100):
    thread = threading.Thread(target=create_file_with_randint)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
end_time = time.time()
print(f"Время выполнения с многопоточностью: {end_time - start_time} секунд.")