# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

a = input()
if a.isdigit():
    print('Verification of the phone number for numbers was successful')
    if len(a) == 10:
        print("Checking the phone number for the number of characters was successful")
    else:
        print("Checking the phone number for the number of characters failed")
else:
    print('Digit phone number verification failed')