from itertools import count, cycle

for el in count(3):
    print(el)
    if el >= 10:
        break

for el in cycle('ABCdef'):
    print(el)
    if el == 'f':
        break
