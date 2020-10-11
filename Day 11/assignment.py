# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

N = int(input())
the_list = list()

for item in range(N):
    query = input().split()
    print('Query is ', query)
    if query[0] == 'print':
        print(the_list)
    elif query[0] == 'insert':
        the_list.insert(int(query[1]), int(query[2]))
    elif query[0] == 'remove':
        the_list.remove(int(query[1]))


print(the_list)


def fn(a, b):
    temp = 1
    for iter in range(b):
        temp = temp*a
    return temp


print(fn(2, 4))

# print(temp) # error : can not access 'temp' out of scope of function 'fn'
# print(iter) # error : can not access 'iter' out of scope of function 'fn'
