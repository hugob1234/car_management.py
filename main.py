car_collection = [
  ["lamboo", "17"], 
  ["", ""]   
]

while True:  
  action = input("Enter action (add, remove, new, check, find, read, or end): ")

  if action == "end":
    break  

  elif action == "add":
    car_name = input("Enter your car's name: ")
    car_info = input("Enter key info of the car: ")
    slot_number = int(input("Enter slot number where you would like to add car info: "))
    if car_collection[slot_number][0] == "":
      car_collection[slot_number][0] = car_name
      car_collection[slot_number][1] = car_info
      print(car_collection)
      x = str(car_collection) + '\n'  # Append new line character
      with open("car.txt" , "a") as file:
        file.write(x)
    else:
      print("Slot unavailable")
      x = '\n' + str(car_collection) + '\n'  # Append new line character
      with open("car.txt" , "a") as file:
        file.write(x)


  elif action == "remove":
    slot = int(input("Enter slot number you would like to empty: "))
    if car_collection[slot][0] != "":
      car_collection[slot][0] = ""
      car_collection[slot][1] = ""
      print(car_collection)
      x = '\n' + str(car_collection) + '\n'  # Append new line character
      with open("car.txt" , "a") as file:
        file.write(x)
    else:
      print("Slot is already empty")

  elif action == "new":
    n = int(input("Enter number of cars you would like to add: "))
    for _ in range(n):
      car_collection.append(["", ""])
      row = len(car_collection)
    print(f"You currently have {row} in database")
    x = '\n' + str(car_collection) + '\n'  # Append new line character
    with open("car.txt" , "a") as file:
      file.write(x)

  elif action == "check":
    c = int(input("Enter slot number you would like to check: "))
    print(car_collection[c])
    x = '\n' + str(car_collection) + '\n'  # Append new line character
    with open("car.txt" , "a") as file:
      file.write(x)

  elif action == "find":
    z = input("Which words you looking for in data base")
    for i in range(len(car_collection)):
      if z in car_collection[i]:
        print("item found")
        x = '\n' + str(car_collection) + '\n'  # Append new line character
        with open("car.txt" , "a") as file:
          file.write(x)

  elif action == "read":
    z = input("Which word are you looking for in the database: ")
    found = False
    for i in range(len(car_collection)):
      if z in car_collection[i]:
        print(f"Item found at index {i}, key info: {car_collection[i][1]}")
        found = True
        x = '\n' + str(car_collection) + '\n'  # Append new line character
        with open("car.txt" , "a") as file:
          file.write(x)
    if not found:
      print("Item not found")
