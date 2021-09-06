from generator import ps_gen


passwords = ps_gen()
print("password generator")


try:
    pw_num = int(input("How many passwords do you want? "))
    list_pw_num = [i for i in range(pw_num)]
    equal_pw_length = str(input(
        "Do you want all your password of equal length? ")).lower()

    if equal_pw_length == "y":
        pw_length = int(input("Enter length of desired passwords: "))
        if pw_length < 6:
            print("We recommend you use password length more than 6 characters.")
        else:
            for digit in list_pw_num:
                print(ps_gen(pw_length))
    elif equal_pw_length == "n":
        pw_length = int(input("Enter length of password: "))
        if pw_length < 6:
            print("We recommend you use password length more than 6 characters.")
        else:
            for digit in list_pw_num:
                print(ps_gen(pw_length))
    else:
        print("Enter 'Y' or 'N'")
except ValueError:
    print('main.py')
print('Copy the password you want. We recommend you save it somewhere, incase you forget it!')
input('Press ENTER to exit') 

