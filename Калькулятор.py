
x = float(input('Перше число: '))
y = float(input('Друге число: '))
operation = input('Знак: ')
result = None
if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
elif operation == '^':
    result = x ** y  
else:
    print('Ошибочка')
print('Результат: ', result)


