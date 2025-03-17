import psutil 
import matplotlib.pyplot as plt 
import time 

iterations = 30 
cpu_usage = []
mem_usage = []
timestamps = []

for i in range(iterations):
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    cpu_usage.append(cpu)
    mem_usage.append(mem)
    timestamps.append(i)

    print(f"секунда {i+1}: CPU {cpu}% | Memory {mem}%")

plt.figure(figsize=(10, 5))
plt.plot(timestamps, cpu_usage, label='Cpu usage (%)')
plt.plot(timestamps, mem_usage, label='Memory usage (%)')
plt.xlabel('Время (сек)')
plt.ylabel('Загруузка (%)')
plt.title ('Сбор метрик системы')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

