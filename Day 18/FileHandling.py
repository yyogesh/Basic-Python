# open('filename', mode)  # mode(r, a, w, x, t,b)  could be to read, write, update
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

f = open('D:\Ysquare\Python\Paython_2020_Ashish\Day 18\sample.txt')
print(f)  # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
txt = f.readlines()
print(txt)
f.close()

# f = open('C:/Python38/sample.txt')
# txt = f.read()
# print(type(txt))
# print(txt)
# f.close()

# # Instead of printing all the text, let us print the first 10 characters of the text file.

# f = open('./files/reading_file_example.txt')
# txt = f.read(10)
# print(type(txt))
# print(txt)
# f.close()


# # readline(): read only the first line
# f = open('./files/reading_file_example.txt')
# line = f.readline()
# print(type(line))
# print(line)
# f.close()


# # readlines(): read all the text line by line and returns a list of lines

# f = open('./files/reading_file_example.txt')
# lines = f.readlines()
# print(type(lines))
# print(lines)
# f.close()


# # Another way to get all the lines as a list is using splitlines():

# f = open('./files/reading_file_example.txt')
# lines = f.read().splitlines()
# print(type(lines))
# print(lines)
# f.close()


# # After we open a file, we should close it. There is a high tendency of forgetting to close them. There is a new way of opening files using with - closes the files by itself.

# with open('./files/reading_file_example.txt') as f:
#     lines = f.read().splitlines()
#     print(type(lines))
#     print(lines)


# with open('./files/reading_file_example.txt', 'a') as f:
#     f.write('This text has to be appended at the end')


# # The method below creates a new file, if the file does not exist:

# with open('./files/writing_file_example.txt', 'w') as f:
#     f.write('This text will be written in a newly created file')
