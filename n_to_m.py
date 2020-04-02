#Same as the previous problem, except you will prompt the user for the number to 
# start on and the number to end on. 

#setup

start_num = int(input('Enter a number to begin with: ' ))
end_num = int(input('Enter a numbert to end with: '))
num = start_num

#code to add and print numbers to console
while num <= end_num:
    print(num)
    num += 1

