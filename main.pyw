import os
import subprocess
import shutil
# Shutil para el movimientos mas robustos y sencillos

# Listado de las extensiones de los archivos de la carpeta Download
listadoDir = os.listdir()
extensionImg = [".jpg",".png",".jpeg",".gif",".svg",".webp"]
extensionDocumen = [".word",".xlsx",".docx","pptx",".ppt",".txt",".pdf"]
extensionEjecutables = [".exe",".bat",".cmd",".com",".msi",".ps1",".vbs"]
extensionComprimidos = [".rar",".zip",".xz"]
extensionWeb = [".css",".html",".js"]
extensionFomartTransferData = [".json",".csv",".xml",".yaml"]
# Yaml se utiliza para poetry el gestor de paquetes y dependencias de python 2323fdfksfksfkl

try:
    for i in listadoDir:
        print(i)
        print(os.path.splitext(i))
        if os.path.splitext(i)[1] in extensionImg:
            print(f"Este es una Imagen {i}")
            os.makedirs("Imagenes",exist_ok=True)
            shutil.move(i,f"Imagenes/{i}")
            

        if os.path.splitext(i)[1] in extensionDocumen:
            os.makedirs("Documentos",exist_ok=True)
            shutil.move(i,f"Documentos/{i}")
            
        if os.path.splitext(i)[1] in extensionEjecutables:
            os.makedirs("Ejecutables",exist_ok=True)
            shutil.move(i,f"Ejecutables/{i}")
            
        if os.path.splitext(i)[1] in extensionComprimidos:
            os.makedirs("Comprimidos", exist_ok=True)
            shutil.move(i,f"Comprimidos/{i}")
            
        if os.path.splitext(i)[1] in extensionWeb:
            os.makedirs("Web",exist_ok=True)
            shutil.move(i,f"Web/{i}")
        if os.path.splitext(i)[1] in extensionFomartTransferData:
            os.makedirs("DataTransfer",exist_ok=True)
            shutil.move(i,f"DataTransfer/{i}")
except FileNotFoundError as e:
    raise Exception("Error en directorio")
finally:
    # Aqui un markdown que explique donde esta cada archivo con su extension 🐈‍⬛
    with open("README.md","w") as docu:
        docu.writelines("# El Directorio se divide en diferentes Subdirectorios... \n \nDocumento: Contiene los archivos con las siguientes extensiones:.word,.xlsx,.docx,pptx,.ppt,.txt,.pdf \n \nEjecutable:  Contiene archivos con extension: .ps1, .exe ,.cmd ,.bat, .com , .msi \n \nImagenes: jpg, jpeg, svg, gif, png"  )
    print("Ejecutado con exito")