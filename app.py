import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from flask import Flask, render_template, Response, request,jsonify
from urllib import request
from flask_sqlalchemy import SQLAlchemy
import cv2
import urllib
import numpy as np
from tensorflow.keras.models import model_from_json  
from tensorflow.keras.preprocessing import image  
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from string import punctuation
import re 
from gingerit.gingerit import GingerIt
import pprint
import json
global text
global gf
model = model_from_json(open("fer.json", "r").read())  

#load weights  
model.load_weights('fer.h5')  
face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
var_list=[]
import os
from flask import Flask, request, render_template
import speech_recognition as sr
import random
import json
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///remos.db'
#db = SQLAlchemy(app)
#class Remos(db.Model):
 #   name = db.Column(db.String(25))
  #  password=  db.Column(db.String(25))
   # def __repr__(self):
    #    return '<Name %r>' % self.name
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
hrq={"Tell me something about yourself?":"2",

"Where do you see yourself in the next 5 years?":"2",

"Would you like to work overtime or odd hours?":"7",

"What are your strengths?":"5",

"Why did you decide to apply to this role?":"0",
"What do you know about our company’s product/services?":"8",
"What are your salary expectations?":"0",
"Explain the difference between group and team. Are you a team player?":"0",
"What is your ideal company or workplace?":"8",
"What is the most difficult thing that you’ve ever accomplished?":"2",
"Do you have any questions?":"2"}
@app.route('/questionhr', methods=['GET'])
def get_questionhr():
    # Get a random question
    global question
    questionss = random.choice(list(hrq.keys()))
    # Return the question as a JSON object
    #pprint(questionss)
    return {"question": questionss}




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
    "Is string class final? ": ["Yes","is final","cannot subclass","Cannot subclass","cannot override its methods","Cannot override its methods"],
    "What are multiple inheritances in Java?":["single child class","multiple superclass","java doesn’t support multiple inheritance","diamond problem","Interface"]}

# Define a function to check if the audio contains keywords in the answer
def check_answer(audio_text, keywords):
    count=0
    for keyword in keywords:
        if keyword in audio_text:
            count=count+1
    return count



# Define the question route to get a random question
@app.route('/question', methods=['GET'])
def get_question():
    # Get a random question
    global question
    question = random.choice(list(questions.keys()))
    # Return the question as a JSON object
    return {"question": question}

# Define the score route to get the score for the answer
@app.route('/processce/<string:Content>',methods=['POST'])
def processce(Content):
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

    per=format(score*10,".2f")
    return render_template("score.html",score=per,question=question)

def gen_frames():  # generate frame by frame from camera 
    # print(len(cv2.VideoCapture()))
    camera = cv2.VideoCapture(0)
    while True:
        # Capture frame by frame
        success, frame =  camera.read()
        if not success:
            break
        else:
            gray_img= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
            faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)  
            for (x,y,w,h) in faces_detected:
                #print('WORKING')
                #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),thickness=7)  
                roi_gray=gray_img[y:y+w,x:x+h]          #cropping region of interest i.e. face area from  image  
                roi_gray=cv2.resize(roi_gray,(48,48))  
                img_pixels = image.img_to_array(roi_gray)  
                img_pixels = np.expand_dims(img_pixels, axis = 0)  
                img_pixels /= 255  
                #print(img_pixels.shape)
                predictions = model.predict(img_pixels) 
                #find max indexed array  
                max_index = np.argmax(predictions[0])  
                emotions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']  
                predicted_emotion = emotions[max_index]  
                if predicted_emotion=='angry':
                    gen_frames.countC=gen_frames.countC+1
                    #print(gen_frames.countA)
                if predicted_emotion=='disgust':
                    gen_frames.countC=gen_frames.countC+1
                    #print(gen_frames.countB)
                if predicted_emotion=='fear':
                    gen_frames.countC=gen_frames.countC+1
                if predicted_emotion=='happy':
                    print(gen_frames.countD)
                    gen_frames.countD=gen_frames.countD+1
                if predicted_emotion=='sad':
                    gen_frames.countA=gen_frames.countA+1
                if predicted_emotion=='neutral':
                    #print(gen_frames.countF)
                    gen_frames.countF=gen_frames.countF+1   
                if predicted_emotion=='surprise':
                    #print(gen_frames.countF)
                
                    gen_frames.countA=gen_frames.countA+1
                #cv2.putText(frame, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)  
            resized_img = cv2.resize(frame, (1000, 700))  
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
    




@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


def grammer(text):
    ginger_parser = GingerIt()
    ginger_grammar_results = ginger_parser.parse(text)
    pprint.pprint(ginger_grammar_results)
    ginger_corrections = ginger_grammar_results['corrections']
    pprint.pprint(ginger_corrections)
    print("\nNumber of grammar issues found with Ginger: " + str(len(ginger_corrections)) + "\n")
    global gf
    gf=len(ginger_corrections)
    for correction in ginger_corrections:
        print("\t(Char #    " + str(correction['start']) + ") Use '" + correction['correct'] + "' instead of '" + correction['text'] + "'")

@app.route('/')
def  index():
    return render_template('finalhome.html')
@app.route('/tutorial')
def tutorial():
     return render_template('tutorial.html')
@app.route('/signin')
def signin():
    return render_template('session.html')
@app.route('/nonhr')
def nonhr():
    return render_template('index1.html')
@app.route('/hr')
def hr():
    return render_template('non_tech.html')    
@app.route('/session')
def session():
    return render_template('session.html')
@app.route('/emotion',methods=['GET','POST'])
def emotion():
    return render_template('emotion.html')

@app.route('/gd')
def gd():
    return render_template('gdfinal.html')
@app.route('/submit',methods=['GET','POST'])
def submit():
    cv2.destroyAllWindows()
    global gf
    emotype=""
    maximum=max(gen_frames.countA,gen_frames.countB,gen_frames.countC,gen_frames.countD,gen_frames.countE,gen_frames.countF,gen_frames.countg)
    if(maximum==gen_frames.countA):
        emotype="FRUSTATION"
    if(maximum==gen_frames.countB):
        emotype="ANXIOUS"    
    if(maximum==gen_frames.countC):
        emotype="NERVOUS" 
    if(maximum==gen_frames.countB):
        emotype="GLOOMY" 
    if(maximum==gen_frames.countD):
        emotype="PLEASANT" 
    if(maximum==gen_frames.countE):
        emotype="GLOOMY" 
    if(maximum==gen_frames.countF):
        emotype="NEUTRAL" 
    if(maximum==gen_frames.countg):
        emotype="EXCITEMENT" 


    data = {'Task' : 'Hours per Day','FRUSTATION':gen_frames.countA, 'ANXIETY':gen_frames.countB, 'NERVOUS':gen_frames.countC, 'PLEASANT':gen_frames.countD, 'GLOOMY':gen_frames.countE,'EXCITEMENT':gen_frames.countg, 'NEUTRAL' :gen_frames.countF}
    #print(data)
    global gf
    return render_template('pie_chart.html',n1=gf,data=data,emot=emotype)

@app.route('/processc/<string:Content>',methods=['POST'])
def processc(Content):
    content=json.loads(Content)
    global text
    text=content
    grammer(text)
    return render_template('emotion.html')

if __name__=='__main__':
    gen_frames.countA=0
    gen_frames.countB=0
    gen_frames.countC=0
    gen_frames.countD=0
    gen_frames.countE=0
    gen_frames.countF=0
    gen_frames.countg=0
    app.run()