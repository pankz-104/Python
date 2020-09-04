import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris//iris.data").text
print(data)

l1 = data.split("\n")
print(l1)

l2 = [item.split(",") for item in l1 if len(item) != 0]
print(l2)

with open("myiris.pkl","wb") as f:
    pickle.dump(l2, f)

# To read the file
import pickle
with open("myiris.pkl","rb") as f:
    print(pickle.load(f))
