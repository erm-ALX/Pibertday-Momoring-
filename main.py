import time

# Ask the user
print("Hello there!")
time.sleep(1.5)
response = input("Are you a once? (yes/no) = ")

if response.lower() == 'no':
    print("Then this is not for you, thank you for answering")

elif response.lower() == 'yes':
    print("Hello co-onceu! I just have a question for you :D")
    time.sleep(1)
else:
    print("Invalid response. Please enter 'yes' or 'no'.")

response = input("Do you know what day it is today? (yes/no) = ")

if response.lower() == 'no':
    print("Edi hindi, shupi")
    time.sleep(1)
    print("Try again accla")

elif response.lower() == 'yes':
    print("weh, hindi nga?")
    time.sleep(1)
    response = input("Sige nga, sino may birthday ngayon?")
    if response.lower() == 'momo':
        print("YAY! IT'S MOMORING DAY")
        time.sleep(1)
        # Print the customized happy birthday song for Momo
        print("Happy birthday Momo")
        time.sleep(1.5)
        print("Happy birthday Momo")
        time.sleep(1.5)
        print("Happy birthday, uri Momoring!")
        time.sleep(2)
        print("Happy birthday Momo!")
        time.sleep(1.5)

else:
    print("Invalid response. Please enter 'yes' or 'no'.")

# Get the user's answer
response = input("Before anything else, do you know how old Momo is today? (yes/no) = ")
if response.lower() == 'no':
    print("It's either baby once ka pa o ang pangit mo kabonding :<")

elif response.lower() == 'yes':
    print("Galing ah, lodi na kita ><")

else:
    print("Invalid response. Please enter 'yes' or 'no'.")

# Print the personalized message
print("Happy 27th birthday Hirai Momo!")
time.sleep(2)
print("Enjoy your day! We love you!")
