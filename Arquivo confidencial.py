import os

seg = str(input("Gostaria de desligar o seu pc em quantos segundos? "))

os.system("shutdown /s /t "+seg)
