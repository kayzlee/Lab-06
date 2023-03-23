# Kaylee Zamora - Lab 06

def encoder(password):                                                      # encodes and stores the password
    encoder = ''
    password_str = str(password)
    for i in range(len(password_str)):
        encoder += str(int(password_str[i]) + 3)
    return encoder

def decode(code):                                                           # decodes the password
    cList = list(code)
    cList = [int(i) for i in cList]
    cList = [((j+10)-3) % 10 for j in cList]
    cList = [str(k) for k in cList]
    password = "".join(cList)
    return password

def main():
    is_valid_input = True
    new_password = 0
    while is_valid_input:
        print('Menu\n-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        option = int(input('\nPlease enter an option:'))

        if option == 1:
            password = int(input('Please enter your password to encode:'))
            new_password = encoder(password)
            print('Your password has been encoded and stored!')
        elif option == 2:                                               # tells the encoded and original password
            password = decode(new_password)
            print('Your encoded password is ', new_password , ', and the original password is ', password, '.')
        elif option == 3:
            break

if __name__ == '__main__':
    main()
