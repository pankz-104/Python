# download data and pickle it in list format 


import requests
import pickle
# listt = []
r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
with open("file.txt",'w') as f:
    content = f.write(r.text)

with open("file.txt") as f:
    data = f.read().splitlines()
    
with open("file.pkl",'wb') as fileobj:
    pickle.dump(data, fileobj)

with open("file.pkl",'rb') as fileobj:
    read = pickle.load(fileobj)
print(read)
