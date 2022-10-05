question = input("В каком году родился Пушкин?")
question = int(question)
if question == 1799:
    q2 = int(input("Правильно, он родился в июне 1799 года, а какого числа?"))
    if q2 == 6:
        print('Верно')
    else:
        print("Неверный день рождения")

else:
    print("Неверный год")