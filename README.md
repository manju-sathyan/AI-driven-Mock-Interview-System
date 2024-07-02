## Overview
This project walks through how to provide a comprehensive platform for job seekers to enhance their interview skills. By offering technical knowledge testing, simulating HR interview scenarios, and facilitating group discussions, the website aims to improve users' interview skills, boost their confidence, and enhance their chances of success in real-world job interviews. This mock interview website is developed using Flask and Python.

## Quick start

There is an overview video on [YouTube](https://www.youtube.com/watch?v=is9ZzgbGSdM).

This project is a mock interview application. The website consists of three main components: a technical knowledge checking session, an HR round, and a group discussion platform. Let's dive into each component:

1. Technical Knowledge Checking Session:
   - This feature allows users to test their technical knowledge by providing a set of questions related to the CSE field.
   - The questions will be displayed and can record the response as voice.
   - The website evaluates the answers and provides instant feedback.

2. HR Round:
   - This component focuses on simulating an HR interview experience.
   - User is asked about questions across various industries.
   - The website can provide a emotional analysis and grammar analysis of the user.
   - Users can record their responses or practice through video conferencing.
   - The system can provide feedback on the user's body emotional analysis, communication skills, and overall performance.
   - Users can review their recorded sessions and receive tips for improvement.

3. Group Discussion Platform:
   - This feature enables users to participate in group discussions to enhance their communication and interpersonal skills.
   - Users can join discussion groups based on their interests or industry preferences.
   - The website can provide discussion prompts or topics to facilitate conversations.
   - Users can engage in text-based discussions or opt for audio/video conferencing for a more immersive experience.
   - Moderators or AI algorithms can monitor discussions and provide constructive feedback on participants' communication style, collaboration, and critical thinking skills.
   - Users can receive badges or achievements based on their participation and performance in group discussions.

Overall, the interview practice website provides a comprehensive and interactive platform for job seekers to prepare for interviews. 

## Technologies

The technologies used in this demo are:
The following tools were used to create the application:
- [Flask web python framework](https://flask.palletsprojects.com/en/2.3.x/)
- [Python](https://www.python.org/)
- [javascript](https://devdocs.io/javascript/)
- [Agora](https://docs.agora.io/en/)


## Setting up the web application

To run locally:

- install python  
- install python3 
- install virtualenv
- virtualenv -p python3 venv
- source venv/bin/activate 
- pip install -r requirements.txt
- flask run
App is running on http://127.0.0.1:5000.

