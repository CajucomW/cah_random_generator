import requests
from django.shortcuts import render

response = requests.get('https://opentdb.com/api.php?amount=1')
data = response.json()
for item in data['results']:
    print(item['question'])
    print(item['incorrect_answers'])
    print(item['correct_answer'])
# Create your views here.
