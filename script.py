import numpy as np 
import os
from time import sleep

# Errors
errors = {
    "err-scr" : "\n>> Invalid Score !\n",
    "err-inpt" : "\n>> Check your input !\n",
    "err-ttl" : "\n>> ENter a valid total number !\n"
}

############################################# Functions ##################################################################

# Geting score one by one 
def get_score(s): # S = Size = Student't total  *  Subject's total
    scores = []
    while s > 0 :
        score = input("Score : ")
        if score.isnumeric() :
            if 0 <= int(score) <= 20 :
                scores.append(int(score))
                s -= 1
            else :
                print(errors["err-scr"])
        else :
            print(errors["err-inpt"])
    return scores

# Geting information about the scores, students, subjects
def get_info():
    students_t = input("Student's Total : ")
    if students_t.isnumeric() :
        subjects_t = input("Subject's Total : ")
        if subjects_t.isnumeric() :
            size = int(students_t) * int(subjects_t)
            return {
                "student" : int(students_t),
                "subject" : int(subjects_t),
                "size" : size,
                "score" : get_score(size)
            }
        else :
            print(errors["err-ttl"])
    else :
        print(errors["err-ttl"])

# Lists
informations = get_info()
row = informations["student"]
scores = np.array(informations["score"]).reshape(row,-1)

# Dataset -> Informations
def dataset():
    print("\n~ Dataset Analyz\n")
    print("\nStudents :",informations["student"])
    print("Subjects :",informations["subject"])
    print("Scores :",informations["score"])

# Overal informations analyz
def overall():
    global scores
    print("\n~ Overall Analyz\n")
    print("\nAverage :",scores.mean())
    print("\nMaximume :",scores.max())
    print("\nMinimume :",scores.min())
    print("\nStd :",scores.std())

# Students & Subjects informations analyz
def one_by_one(title, q):
    global scores
    print(f"\n~ {title}s Analyz !\n")
    scores_new = scores if q == True else scores.T
    for i,item in enumerate(scores_new,1) :
        print(f"\n>> {title} ({i})\n")
        print("Average :",item.mean())
        print("Maximume :",item.max())
        print("Minimume :",item.min())

# Scores higher than the entrance score
def high_score():
    global scores
    score = input("\n>>> Please enter min score : ")
    if score.isnumeric() :
        if 0 <= int(score) <= 20 :
            print("~ High Scores :\n",scores[scores >= int(score)])
        else :
            print(errors["err-scr"])
    else :
        print(errors["err-inpt"])

############################################# Main #######################################################################

# Main func
def main() :
    os.system("cls")
    print("\n===== INFORMATIONS ANALYZER ======\n")
    dataset()
    overall()
    one_by_one("student",True)
    one_by_one("subject",False)
    high_score()

if __name__ == "__main__" :
    main()

# Created by Exit Zero