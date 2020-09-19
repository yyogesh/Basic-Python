print('today %d  %s cost ' % (6, 'bananas'))
# %[<flags>][<width>][.<precision>]<type>

str = "Hello my name is %s" % 'Ashish'
print(str)

print('today %d%%  %s cost ' % (6, 'bananas'))

print('today x %7d  %s cost ' % (6, 'bananas'))


for i in range(3):
    w = int(input('enter width: '))
    print('[%*s]' % (w, 'abc'))

print('today %d  %s cost %.2f' % (6, 'bananas', 1.2556))
