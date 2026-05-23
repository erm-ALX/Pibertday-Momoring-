import time

# INTRO
print("Hello there!")
time.sleep(1.5)

# FIRST QUESTION
while True:
    response = input("Are you a once? (yes/no) = ").strip().lower()

    if response == 'yes':
        print("Hello co-onceu! I just have a question for you :D")
        time.sleep(1)
        break

    elif response == 'no':
        print("Then this is not for you, thank you for answering")
        exit()

    else:
        print("Invalid response. Please enter yes or no.")
        time.sleep(1)

# SECOND QUESTION
while True:
    response = input("Do you know what day it is today? (yes/no) = ").strip().lower()

    if response == 'yes':
        print("weh, hindi nga?")
        time.sleep(1)
        break

    elif response == 'no':
        print("Edi hindi, shupi")
        time.sleep(1)
        print("Try again accla")
        exit()

    else:
        print("Invalid response. Please enter yes or no.")
        time.sleep(1)

# BIRTHDAY QUESTION
while True:
    response = input("Sige nga, sino may birthday ngayon? ").strip().lower()

    # safer check (accepts momo, momo with spaces, etc.)
    if "momo" in response:

        print("YAY! IT'S MOMORING DAY")
        time.sleep(1)

        # 🎵 SONG (REPLACED & GUARANTEED SHOW)
        song = [
            "Happy birthday Momo",
            "Happy birthday Momo",
            "Happy birthday, uri Momoring!",
            "Happy birthday Momo!"
        ]

        for line in song:
            print(line)
            time.sleep(1.5)

        break

    else:
        print("Mali ka accla, try again 😭")
        time.sleep(1)

# FINAL QUESTION
while True:
    response = input(
        "Before anything else, do you know how old Momo is today? (yes/no) = "
    ).strip().lower()

    if response == 'yes':
        print("Galing ah, lodi na kita ><")
        time.sleep(2)
        break

    elif response == 'no':
        print("It's either baby once ka pa o ang pangit mo kabonding :<")
        time.sleep(2)
        break

    else:
        print("Invalid response. Please enter yes or no.")
        time.sleep(1)

# FINAL MESSAGE
print("Happy birthday Hirai Momo!")
time.sleep(2)

print("Enjoy your day! We love you!")
