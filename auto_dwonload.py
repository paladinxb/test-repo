import subprocess
import time
import threading

# Флаг для остановки скрипта
stop_flag = False

def run_sync():
    global stop_flag
    while not stop_flag:
        print("Запускаю sync.bat...")
        subprocess.run(["D:\\Coding\\work\\test-repo\\sync.bat"], shell=True)
        time.sleep(60)  # Ждём 1 минуту

# Запускаем в отдельном потоке
thread = threading.Thread(target=run_sync)
thread.start()

# Через 10 минут останавливаем
time.sleep(600)
stop_flag = True
thread.join()
print("Автоматическая синхронизация остановлена.")
