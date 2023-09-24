print('калькулятор готов к работе!нажмите Enter, чтобы продолжить')
input()
sequel = 'у'
while sequel == 'у':
    a_num = float(input("введите первое число>"))
    operation = input("введите операцию>")
    b_num = float(input("введите второе число>"))
    if operation == '+':
        print(a_num + b_num)
    elif operation == '-':
        print(a_num - b_num)
    elif operation == '*':
        print(a_num * b_num)
    elif operation == '/':
        print(a_num / b_num)
    else:
        print('ошибка, такой операции не существует')
    sequel = input("введите у, чтобы продолжить, или любую другую клавишу, чтобы завершить>")


    