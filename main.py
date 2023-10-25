# Howard Shin

def encode(password):
    encoded_password = ""
    
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    
    return encoded_password


def decode(encoded_password):
    decoded_password = ''
    for x in encoded_password:
        x = int(x)
        x -= 3
        x = str(x)
        decoded_password += x
    return decoded_password

while True:
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    option = int(input("Please enter an option: "))
    if option == 1:
        password = (input("Please enter your password to encode: "))
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')
        # print(encoded_password)
    if option == 2:
        decoded_password = decode(encoded_password)
        print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
    if option == 3:
        break

