def add(a, b):
    answer = a + b
    print(str(a) + '+' + str(b) + '=' + str(answer))


def sub(a, b):
    answer = a - b
    print(str(a) + '-' + str(b) + '=' + str(answer))


def mult(a, b):
    answer = a * b
    print(str(a) + '*' + str(b) + '=' + str(answer))


def div(a, b):
    answer = a / b
    print(str(a) + '/' + str(b) + '=' + str(answer))

while True:
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')
    print('E. Exit')

    choice = input('input your choice: ')
    if choice == 'a' or choice == 'A':
        print('Addition')
        a = int(input('input first number:'))
        b = int(input('input second number:'))
        add(a, b)
    elif choice == 'b' or choice == 'B':
        a = int(input('input first number:'))
        b = int(input('input second number:'))
        print('Subtration')
        sub(a, b)
    elif choice == 'c' or choice == 'C':
        a = int(input('input first number:'))
        b = int(input('input second number:'))
        print('Multiplication')
        mult(a, b)
    elif choice == 'd' or choice == 'D':
        a = int(input('input first number:'))
        b = int(input('input second number:'))
        print('Divition')
        div(a, b)
    elif choice == 'e' or choice == 'E':
        print('program ended ')
        quit()
