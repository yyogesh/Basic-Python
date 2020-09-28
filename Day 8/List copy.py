import copy

old_list = [1, 2, 3]
new_list = old_list


new_list.append('a')

print('Old list : ', old_list)
print('New list : ', new_list)

print('Old list : ', id(old_list))
print('New list : ', id(new_list))


old_list = [1, 2, 3]
new_list = old_list.copy()

new_list.append('a')

print('Old list : ', old_list)
print('New list : ', new_list)

print('Old list : ', id(old_list))
print('New list : ', id(new_list))


old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
old_list[1][1] = 'AA'
print("Old list:", old_list)
print("New list:", new_list)

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)
old_list[1][1] = 'AA'
print("Old list:", old_list)
print("New list:", new_list)


old_list = [1, 2, 3]
new_list = old_list[:]

new_list.append('a')

print('Old list : ', old_list)
print('New list : ', new_list)
