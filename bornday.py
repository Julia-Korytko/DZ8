"""МОДУЛЬ 3"""

# Пользователю предлагается ответить на вопрос. В программе используются условные операторы

bornyear = int(input("В каком году родился А.С. Пушкин? "))
if bornyear ==1799:
    bornday = str(input("В какой день родился А.С. Пушкин? "))
    print(bornday)
    if bornday =="6 июня":
        print("Верно")
    else: print("Неверный день рождения")

else:
    print("Неверный год рождения")

print("end")