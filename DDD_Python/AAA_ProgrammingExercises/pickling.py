import pickle
import requests

# PRoblem Solution 5
pkl_file = open('banner.p', 'rb')
data = pickle.load(pkl_file)
print(sorted(data))

for i in data:
    line = ""
    for a,b in i:
        line = line + (a * b)
    print(line)