# Факториал числа N можно вычислить через рекурсию следующим образом:
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Треугольное число для числа N можно вычислить через рекурсию следующим образом:
def triangular_number(n):
    if n == 1:
        return 1
    else:
        return n + triangular_number(n-1)
