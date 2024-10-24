#Eva Bechtol
def encode(code):
    new_code = ""
    for digit in range(len(code)):
        if int(code[digit]) <= 6 :
            new_code += str(int(code[digit]) + 3)
        else:
            new_code += str(int(code[digit] - 7))

    return new_code

def decode(enc_password):
    res = ""
    for dig in enc_password:
        dig = int(dig)
        if dig == 2:
            dig = 9
        elif dig == 1:
            dig = 8
        elif dig == 0:
            dig = 7
        else:
            dig -= 3
        res += str(dig)
    return res

if __name__ == "__main__":
    password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print(f"Your password has been encoded and stored!")
        elif choice == "2":
            print(f"The encoded password is {encode(password)}, and the original password is {password}.")
        elif choice == "3":
            break
        else:
            print("Invalid option, please try again.")