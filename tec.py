import os
from flask import Flask, request, render_template
import speech_recognition as sr
import random
import json
app = Flask(__name__)
global question
# Define a list of questions and answers
questions = {
    "What are the access specifiers in Java?": "Public",
    "What is a class?": "blueprint",
    "Is Java 100% object oriented?": "No",
    "Explain the “InstanceOf” operator in Java": "compares",
    "What is Deadlock?":"wait for each other",
    "What is normalization in a Database?":"abstracting",
    "What is TCP?":"Transmission Control Protocol",
    "Explain DNS?":"Domain name system",
    "Is string class final? ":"yes",
    "What are multiple inheritances in Java?":"one child more parent"
}

# Define a list of keywords for each question
keywords = {
    "What are the access specifiers in Java?": ["Public", "Protected", "Private", "Default"],
    "What is a class?": ["blueprint", "template","creating objects","object-oriented programming"],
    "Is Java 100% object oriented?": ["No", "primitive data types","Use of Static","Wrapper class",""],
    "Explain the “InstanceOf” operator in Java": ["comparison operator", "compares","instance of a class","subclass","interface","Downcasting"],    
    "What is Deadlock?":[ "two or more processes","wait for each other","wait for resources","held by other","two or more processes hold some resources","mutual exclusion","hold and wait","no preemption ","circular set"],
    "What is normalization in a Database?":["abstracting","simplifying","easier to understand","dividing by"],
    "What is TCP?":["Transmission Control Protocol","networking protocol ","Transport layer","transfer data","connection-oriented ","two computers connected","three way handshaking","connection establishment","connection termination"],
    "Explain DNS?":["Domain Name System","mapping","domain names to IP addresses","used by email services","computer sends a request to the DNS server","DNS server then returns a response"],
    "Is string class final? ": ["Yes","is final","cannot subclass","cannot override its methods",],
    "What are multiple inheritances in Java?":["single child class","multiple superclass","java doesn’t support multiple inheritance","diamond problem","Interface"]}

# Define a function to check if the audio contains keywords in the answer
def check_answer(audio_text, keywords):
    count=0
    for keyword in keywords:
        if keyword in audio_text:
            count=count+1
    return count

# Define the index route to render the home page
@app.route('/')
def index():
    return render_template('index1.html')

# Define the question route to get a random question
@app.route('/question', methods=['GET'])
def get_question():
    # Get a random question
    global question
    question = random.choice(list(questions.keys()))
    # Return the question as a JSON object
    return {"question": question}

# Define the score route to get the score for the answer
@app.route('/processc/<string:Content>',methods=['POST'])
def processc(Content):
    content=json.loads(Content)
    print(content)
    audio_text=content
    # Get the question from the request
    global question
    # Get the answer for the question
    answer = questions[question]
    print(question)
    # Check if the audio contains keywords in the answer
    contains_keywords = check_answer(audio_text, keywords[question])
    # Calculate the score
    global score
    score = contains_keywords
    # Return the score as a JSON object
    print(score)
    return render_template("score.html",score=score,question=question)

@app.route('/scorep',methods=['post'])
def scorep():
    global score
    return render_template("score.html",score=score,question=question)

if __name__ == '__main__':
    app.run()
