def fact(n):
    a = 1
    for el in range(1, n + 1):
        a = a * el
        yield a


n = input("Введите n: ")
try:
    n = int(n)
except ValueError:
    print("Введено не число")
for el in fact(n):
    b = el
    print(el)
print(f"Результат: {n}!={b}")
