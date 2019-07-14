import requests
import random
from django.shortcuts import render

response = requests.get('https://opentdb.com/api.php?amount=1')
data = response.json()

def quiz():
    for item in data['results']:
        correct = item['correct_answer']
        choices = item['incorrect_answers']
        print(item['question'])
        
        answers = []

        for choice in choices:
            answers.append(choice)      # this adds the wrong answers to the list "answers"
        answers.append(correct)         # this adds the right answer to he list "answers"
        random.shuffle(answers)         # this randomizes all the answers from the list "answers"
        
        print(answers)
        
        user_answer = input("Type your answer here: ")
        if user_answer in item['correct_answer']:
            print("You got it!")
        else:
            print("Sorry. The answer is", correct, ".")
quiz()

# i = 0
# while i < 3:
#     quiz()
#     i += 1
# Create your views here.
