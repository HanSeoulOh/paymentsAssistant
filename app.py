from flask import Flask
import requests
from flask import request, render_template
import openai
import os
import random as rd
import markdown

app = Flask(__name__)

# Get API key
with open('secret', 'r') as file:
    secret = file.read()

openai.api_key = secret

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_data = request.form['input_data']
        content = input_data
        # while True:
        chatgptR = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a software engineer lead who works in payments teaching junior engineers how to code."},
            {"role": "user", "content": content + " Assume that the banking API can only perform simple transactions such as send payment and show balance, but doesn't have a schedule recurring payment function so you will have to use Python to schedule it. Also create the corresponding plantUML code snippet to show the payment flow for the Python script you give me. Don't forget that plantUML names with spaces in them require double quotes to be escaped. Make sure to wrap any code examples in <code></code> blocks"}
            ]
        )
            # plantUMLString = ""
            # flag = 0
            # worked = 0
            # break
        
        retchunks = markdown.markdown(chatgptR.choices[0]['message']['content'], extensions=['fenced_code'])
        print(retchunks)
        # print(pythonString)

        return render_template('result.html', retchunks = retchunks)
    # If the request is a GET request, render the form for the user to fill out
    return render_template('form.html')

app.run(host='0.0.0.0', port=81)
