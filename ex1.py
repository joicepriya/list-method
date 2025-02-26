#list methods

cars=["BMW","ferrari","Audi","cadillac","jeep","tesla","toyota"]
cars.append("tata")
print(cars)

cars.extend("hyundai")
print(cars)

cars.insert(2,"mazda")
print(cars)

cars.remove("cadillac")
print(cars)

cars.pop(1)
print(cars)

x=cars.count("jeep")
print(x)

y=cars.index("toyota")
print(y)

cars.reverse()
print(cars)

cars.clear()
print(cars)
