import os

files = os.listdir("zino.3.txt")
for file in files:
    if os.path.isfile("zino.3.txt\\" + file):
        print(file)
    

