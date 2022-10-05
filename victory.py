
q1 = int(input('В каком году родился Лермонтов?'))#1814
q1a = 1814
q2 = int(input('В каком году родился Петр 1'))#1672
q2a = 1672
q3 = int(input('В каком году родился Есенин'))#1895
q3a = 1895
q4 = int(input('В каком году родился Джеки Чан'))#1954
q4a = 1954
q5 = int(input('В каком году родился Брюс Ли'))#1940
q5a = 1940

true_answer = 0
false_answer = 0
true_percent = 0
false_percent = 0

questions = (q1, q2, q3, q4, q5)
answers = (q1a, q2a, q3a, q4a, q5a)

for i in questions:
    if i == (answers, [i]):
        true_answer += 1
    else:
        false_answer += 1

print("true:", true_answer)
print("fals:", false_answer)


#    if items == a in answers:
#         true_answer +=1
#     else:
#         false_answer +=1
#
# print("true:", true_answer)
# print("fals:", false_answer)


