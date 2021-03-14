from sys import argv

name_file, name, time, reward = argv
rate = 10
try:
    time = float(time)
    reward = float(reward)
    print(f"Сотрудник {name} получит зарплату: {rate*time+reward} руб.")
except ValueError:
    print("Параметры заданы не числом")

