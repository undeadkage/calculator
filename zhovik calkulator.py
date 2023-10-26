operation= input('выберите тип операции')
a = int(input('первое число'))
b = int(input('второе число'))
#сложение
if operation == '+':
    result = (a + b)
#вычитание    
elif operation == '-':
    result = (a - b)
#умножение
elif operation == '*':
    result = (a * b)
#деление
elif operation == '/':
    result = (a / b)
#возведение в квадрат
elif operation == '**':
    result = (a**b)
    
#вывод результата 
print('Ответ:')
print(result)
