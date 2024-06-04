import os

locations = os.scandir("/Users/kevin")

for i in locations:
    if os.path.isdir(i):
        print("DIR:", i)
    if os.path.isfile(i):
        print("FILE:", i)