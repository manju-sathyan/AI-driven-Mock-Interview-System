from flask import Flask, render_template, Response, request
app=Flask(__name__)
@app.route('/')
def index():
     return render_template('indexf.html')

    
if __name__=='__main__':
    app.run()