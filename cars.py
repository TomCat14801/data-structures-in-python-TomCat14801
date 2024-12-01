cars.py
first_name = "Dallas" last_name = "Olsen"
print(f"My name is {Dallas} {Olsen}")
cars = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']
print(cars)
print(len(cars))
cars.append('Buick')
print(cars)
print(cars[3])
cars.insert(2, 'Toyota')
print(cars)
cars = ['Ford', 'Chrysler', 'Toyota', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC', 'Buick']
removed_car = cars.pop(4)
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
my_array_length = len(cars)
print(my_array_length)
array_string = 'The length of my array is '
print(array_string)
print(array_string + str(my_array_length))