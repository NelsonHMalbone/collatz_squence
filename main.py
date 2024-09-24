# creating the function
print('keep going till you hit the value of 1')
def collatz(number):
    if number % 2 == 0:
        ret_val = number // 2 # if even
    else:
        ret_val = 3 * number + 1 # if odd
    print(ret_val)
    return ret_val

# so user does not get a error for ending program
try:
    # write a program feeds the collatz
    while True: # setting up main loop
        try:
            number = int(input('Enter a seed number: ')) # having user enter a random number
            while collatz(number) != 1: # if not equal to one will run till equal to one
                number = collatz(number) # calling number to call the function
        except ValueError: # error for user entering a non number
            print("numbers only!")
except KeyboardInterrupt:
    print("program ended")
