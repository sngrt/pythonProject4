repeat = True

while repeat != False:

    true_answer = 0
    false_answer = 0
    true_percent = 0
    false_percent = 0


    q1 = int(input('В каком году родился Лермонтов?')) #1814
    q1a = 1814
    if q1 == q1a:
        true_answer += 1
    else:
        false_answer += 1
    q2 = int(input('В каком году родился Петр 1'))#1672
    q2a = 1672
    if q2 == q2a:
        true_answer += 1
    else:
        false_answer += 1
    q3 = int(input('В каком году родился Есенин'))#1895
    q3a = 1895
    if q3 == q3a:
        true_answer += 1
    else:
        false_answer += 1
    q4 = int(input('В каком году родился Джеки Чан'))#1954
    q4a = 1954
    if q4 == q4a:
        true_answer += 1
    else:
        false_answer += 1
    q5 = int(input('В каком году родился Брюс Ли'))#1940
    q5a = 1940
    if q5 == q5a:
        true_answer += 1
    else:
        false_answer += 1


    true_percent = (true_answer/5*100)
    false_percent = (false_answer/5*100)
    print('Правильных ответов:', true_answer)
    print('Неправильных ответов:', false_answer)
    print('% правильных:', true_percent)
    print('% неправильных:', false_percent)

    r = input('Хотите ли попытаться снова?')

    if r == 'Нет':
        break



# questions = (q1, q2, q3, q4, q5)
# answers = (q1a, q2a, q3a, q4a, q5a)
# n = 0





# def vic (q):
#     if q == (answers[n])
#         n +=1
#         true_answer +=1
#     else:
#         n+=1
#         false_answer +=1
#
#
# for q in questions:
#     vic(q)

# for i in questions:
#     if i == (answers, [i]):
#         print([i])
#         true_answer += 1
#     else:
#         false_answer += 1
#
# print("true:", true_answer)
# print("fals:", false_answer)
#

#    if items == a in answers:
#         true_answer +=1
#     else:
#         false_answer +=1
#
# print("true:", true_answer)
# print("fals:", false_answer)


