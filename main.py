def encoder(password):
    encoder = ''
    password = list(password)
    for i in range(len(password)):
        password[i] += 3
        encoder += i
        str(password)
    return encoder

def main():
    is_valid_input = True
    while is_valid_input:
        print('Menu\n-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        option = int(input('\nPlease enter an option:'))
        password = int(input('Please enter your password to encode:'))

if __name__ == '__main__':
    main()