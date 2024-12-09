import os
import shutil

# import psutil
# import platform


ruta = f"C:/Users/Usuario/AppData/Local"

try:
    if __name__ == "__main__":
        os.chdir(ruta)
        shutil.rmtree("Temp",ignore_errors=True)
        shutil.rmtree("C:\Windows\Temp",ignore_errors=True)
        os.chdir("temp")
        print(os.listdir())
except Exception as e:
    raise Exception(e)