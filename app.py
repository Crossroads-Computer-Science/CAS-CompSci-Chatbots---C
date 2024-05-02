from flask import Flask, render_template, request
from openai import OpenAI
import json
import os

app = Flask(__name__)
client = OpenAI()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/progress')
def progress():
    return render_template('progress-chat.html')


@app.route('/dad')
def dad_jokes():
    return render_template('dad-jokes.html')


@app.route('/koala')
def card():
    return render_template('koala.html')


@app.route("/chat")
def chat_completion():
    try:
        prompt = request.args.get('prompt')
        # parse data
        messages = json.loads(prompt)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return str(completion.choices[0].message.content)
    except Exception as e:
        return str(e), 500  # Return error message with status code 500


if __name__ == '__main__':
    app.run(debug=True)
