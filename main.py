# Howard Shin

def encode(password):
    encoded_password = ""
    
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    
    return encoded_password

while True:
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    option = int(input("Please enter an option: "))
    if option == 1:
        password = (input("Please enter your password to encode: "))
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')
        # print(encoded_password)
    if option == 2:
        pass
    if option == 3:
        break

