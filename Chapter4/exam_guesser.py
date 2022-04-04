# coci08c1p2

# Adrian, Bruno, and Goran have an exam coming up they didnt study for, so
# they determined to guess the answers based on a repeating set of answers:

# Adrian: ABC
# Bruno: BABC
# Goran: CCAABB

# Find which student's sequence gets them the best score.

# Inputs:
#    Number of items on the Exam
#    Exam answers

# Output:
#   The high score
#   The name of the student with the high score.
#   In the case of a tie, return the student names alphabetically

# inputs
N = int(input())
Exam = input()

# set student answer patterns
A = 'ABC'
B = 'BABC'
G = 'CCAABB'
scores = {}

def student_correct(student, N):
    '''function to determine the number of correct answers from a student
    :student: student answer pattern string
    :N: number of items on the exam
    '''
    answers = ""
    correct = 0
    for i in range(N):
        if Exam[i] == student[i%len(student)]:
            correct += 1
    return(correct)

scores["Adrian"] = student_correct(A, N)
scores["Bruno"] = student_correct(B, N)
scores["Goran"] = student_correct(G, N)

# the high score
high_score = max((list(scores.values())))
print(high_score)

# put the name(s) of the high scoring student(s) in a list, sort it
# alphabetically, and return the items on that list.
names =[]
for k,v in scores.items():
    if v == high_score:
        names.append(k)
names.sort()
for name in names:
    print(name)
