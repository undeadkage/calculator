a = int(input('первое число'))
b = int(input('второе число'))
operation = input('operation')
if operation == '+':
    result = (a + b)
elif operation == '-':
    result = (a - b)
elif operation == '*':
    result = (a * b)
elif operation == '/':
    result = (a / b)
print(result)
