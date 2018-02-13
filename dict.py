names = {}
names = [('One', 1), ('Two', 2), ('Three', 3), ('Four', 4), ('Five', 5)]

print(names.keys())
print(names.values())

cars = ["Maruti", "Mercedes", "Honda", "Hyundai", "Chevrolet", "Renalt"]

for car in cars:
    print(car, " is a car")

cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
