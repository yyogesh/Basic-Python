import re

# re.match(substring, string, re.I)
# re.I is case ignore flag

txt = 'I Love to teach python and javaScript. I love to teach sports also'
match = re.match('I love to teach', txt, re.I)
print(match)
print(match.span())
start, end = match.span()
print(txt[start: end])


txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches = re.findall('language', txt, re.I)
print(matches)

matches = re.findall('Python|python', txt)
print(matches)


matches = re.findall('[Pp]ython', txt)
print(matches)


txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''


match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)


txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))


regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)


# this mean the first letter could be Apple or apple
regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']


# []: A set of characters
# [a-c] means, a or b or c
# [a-z] means, any letter from a to z
# [A-Z] means, any character from A to Z
# [0-3] means, 0 or 1 or 2 or 3
# [0-9] means any number from 0 to 9
# [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
# \: uses to escape special characters
# \d means: match where the string contains digits (numbers from 0-9)
# \D means: match where the string does not contain digits


# this square bracket means either A or a
regex_pattern = r'[Aa]pple|[Bb]anana'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)


regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9'], this is not what we want


regex_pattern = r'\d+'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9'], this is not what we want
