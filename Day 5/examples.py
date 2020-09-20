# Set Integers
Temperature = int(input("Enter temperature:"))
Humidity = int(input("Enter humidity percentage:"))

# statements

if Temperature >= 100:
    print("Cancel School, and recommend a good movie")
elif Temperature >= 92 and Humidity > 75:
    print("Cancel schoool")
elif Temperature > 88 and Humidity >= 85:
    print("Cancel school")
elif Temperature == 75 and Humidity <= 65:
    print("Encourage students to skip school and enjoy the great outdoors")
elif Temperature <= -25:
    print("You had better panic, because the world is clearly ending")
elif Temperature < 0:
    print("Cancel school")
else:
    print("School is in session")
