from flask import Flask, render_template, request
import random, copy

app = Flask(__name__)
QUESTIONS = {
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
    "What does dict.get(key) return if key isn't found in dict": [
        "None", "key", "True", "False",
    ]
}
questions = copy.deepcopy(QUESTIONS )

for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    answer_label = input("\nChoice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

@app.route('/')
def quiz():
 return render_template('main.html', q = QUESTIONS , o = questions)


@app.route('/quiz', methods=['POST'])
def quiz_answers():
 correct = 0
 for i in questions.keys():
  answered = request.form[i]
  if QUESTIONS [i][0] == answered:
   correct = correct+1
 return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

if __name__ == '__main__':
 app.run(debug=True)