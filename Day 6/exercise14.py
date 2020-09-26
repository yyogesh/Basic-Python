# In this challenge, the user enters a string and a substring. You have to print the number of
# times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

str = 'ABCDCDC'
strSub = 'CDC'
count = 0
for i in range(len(str)):
    print(str[i: i + len(strSub)])
    if str[i: i + len(strSub)] == strSub:
        count += 1
print(count)
