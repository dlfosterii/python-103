#PPrint a NxN square of * characters. Prompt the user for N

#setup
side = (input('Enter a number to print a square of that size: ')
y = 0

#Code to make it work

while(y < side):
    x = 0
    while(x < side):      
        x = x + 1
        print('*', end = ' ')
    y = y + 1
    print('')


#end