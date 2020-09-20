n = 0

while n < 10:
    print(n)
    n = n + 1


avaiable_exits = ["east", "north east", "south"]

chosen_exit = ''

# while chosen_exit not in avaiable_exits:
#     chosen_exit = input("Please choose a direction: ")

# print("aren't you glad you got out of there!")

while chosen_exit not in avaiable_exits:
    chosen_exit = input("Please choose a direction: ")
    if(chosen_exit == 'quit'):
        print('Game over')
        break
else:
    print('While loop end')

print("aren't you glad you got out of there!")


for x in range(10):
    pass
