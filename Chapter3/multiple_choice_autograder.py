#DMOJ ccc11s2
#
# input will be X followed by 2X lines.
# the 2X lines are composed of X lines of student responses
# followed by X lines of correct answers

#output the number of instances where the question and answer correspond.


QA = []
correct = 0

N = int(input())

for i in range(2*N):
    QA.append(input())

index = 0
for question in QA[0:N]:
    if question == QA[N + index]:
        correct += 1
    index += 1

print(correct)
