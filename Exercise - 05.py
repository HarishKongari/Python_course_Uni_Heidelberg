#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import random
def shuffle_list(list_to_shuffle: list) -> list:
    """
    Not sure, I hope this will shuffle the list... 😕 TODO improve text

    :param list_to_shuffle: TODO improve text here
    :type list_to_shuffle: list
    :return: TODO improve text here
    :rtype: list
    """
    #list_to_shuffle.reverse()
    random.shuffle(list_to_shuffle)
    return list_to_shuffle
#ANSWER IS:shuffle_list([4,5,6,7,8])
#Out[30]: [6, 7, 8, 5, 4]
#############################################################

def create_question():
    # Counter forcounting the number of questions, total correct and wrong answers
    count_correct = 0
    count_wrong = 0
    count_question = 1
    # Defining questions, right answers and wrong_answers
    questions = ["Benjamin Blümchen ist ein ...", "Welches Tier kann mit seinen Zähnen Bäume \"fällen\"?",
                 "Was ist eine \"Fraktur\"?", "Bei welcher Krankheit tritt ein langsam fortschreitender ",
                 " Wie nennt man eine \"Erinnerungshilfe\"?"]
    
    right_answers = ["Elefant", "Biber", "Konchenbruch", "Parkinson", "Eselsbrücke"]
    
    wrong_answers = [["Zebra", "Löwe", "Affe"], ["Kamel", "Schwein", "Pferd"], 
                     ["Blutung", "Kopfschmerz", "Muttermal"], ["Keuchhusten", "Röteln", "Scharlach"],
                     ["Ziegenbrücke", "Schweinebrücke", "Affenfurche"]]
    
    # Introducing the Quiz
    print("\n        Welcome to the Quiz\n")
    begin = input("Would you like to take the Quiz (yes/no)\n\n")
    print("\n")
    
    # while loop for looping the question upto number of questions or till the user stops
    while (begin == "yes" or begin == "Yes" or begin == "YES") and count_question<=5:
    
        
        # mentions the question number in the quiz
        print ( "Question " + str(count_question) + "\n" )
        # generating random question
        random_question = random.choice(questions)
        #taking index of questions
        location_question = questions.index(random_question)
        print(random_question)
        print("\nChoose one of the options from below: ")
        possible_answers = [right_answers[location_question], wrong_answers[location_question][0],
                            wrong_answers[location_question][1],wrong_answers[location_question][2]]
        # shuffling possible answers
        random.shuffle(possible_answers)
        shuffled_answers = possible_answers
        print(" 1." + possible_answers[0] +"\n","2." + possible_answers[1] +"\n",
              "3." + possible_answers[2] +"\n", "4." + possible_answers[3] +"\n")
        # taking user input
        user_option = input("Type 1 or 2 or 3 or 4 to give your answer\n\n") 
    
        #correct_answer_check = {1: possible_answers[0], 2: possible_answers[1],
        #                        3: possible_answers[2], 4: possible_answers[3]}
        
        user_answer = shuffled_answers[int(user_option)-1]
        # checking if answer is correct 
        if user_answer in right_answers:
            print("\nYour answer is correct\n")
            count_correct = count_correct + 1
        else:
            print("\nYour answer is wrong\n")
            count_wrong = count_wrong + 1
        count_question = count_question + 1
        percent = ((count_correct)/(count_correct + count_wrong))*100
        if count_question<=5:
            begin = input("Would you still like to continue the Quiz (yes/no)\n\n")
        
        # ending the program after 5 questions        
        elif count_question>5:
            print("\nThe Quiz is finished and Your total score is {} percent".format(percent))
    # exiting loop if the user wants to stop        
    if (begin == "no" or "No" or "NO") and count_question<5: 
        print("\nThanks for the interest in the Quiz")
        if count_question>=1 and count_question<=5:
            print("\nYour score is {} percent".format(percent))