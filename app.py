from flask import Flask, render_template, request
from openai import OpenAI
import json

app = Flask(__name__)
client = OpenAI()


@app.route('/')
def index():
    return render_template('index.html')

# ___________________
@app.route('/techyT')
def techyT():
    return render_template('techyTim.html')
# ___________________
@app.route('/cardJS')
def cardJS():
    # key = os.environ.get('OPENAI_API_KEY')
    # return key
    return render_template("cardJS.html")
@app.route('/JS')
def indexJS():
    # key = os.environ.get('OPENAI_API_KEY')
    # return key
    return render_template("indexJS.html")
@app.route('/comedyJamie')
def comedyJS():
    # key = os.environ.get('OPENAI_API_KEY')
    # return key
    return render_template("comedyJS.html")
@app.route('/triviaJS')
def triviabot():
    # key = os.environ.get('OPENAI_API_KEY')
    # return key
    return render_template("triviabot.html")

@app.route("/chat")
def chat_completion():
    prompt = request.args.get('prompt')
    # parse data
    messages = json.loads(prompt)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return str(completion.choices[0].message.content)


if __name__ == '__main__':
    app.run(debug=True)