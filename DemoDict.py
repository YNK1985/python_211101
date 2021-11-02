# DemoDict.py
device={"iphone":5,"ipad":10,"windows":20}

print(type(device))
print(device)
device["macbook"]=15
print(device["iphone"])
device["iphone"]= 6
del device["ipad"]
print(device)


device2=device
print(device2)
device2["gram"]=40
print(device2,id(device),id(device2),device)

