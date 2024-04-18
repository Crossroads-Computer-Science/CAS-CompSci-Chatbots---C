from flask import Flask, render_template, request
from openai import OpenAI
import json
import os

app = Flask(__name__)
client = OpenAI()


@app.route('/')
def index():
    key = os.environ.get('OPENAI_API_KEY')
    print(key)
    return render_template('index.html')

# ___________________
@app.route('/techyT')
def techyT():
    return render_template('techyTim.html')
# ___________________


@app.route('/aboBot')
def abobot():
    key = os.environ.get('OPENAI_API_KEY')
    print(key)
    return render_template("aboBot.html")

@app.route('/cardJS')
def cardJS():
    return render_template("cardJS.html")
@app.route('/harry')
def harry():
    return render_template("harry.html")
@app.route('/comedyJS')
def comedyJS():
    return render_template("comedyJS.html")
@app.route('/triviabot')
def triviabot():
    return render_template("triviabot.html")
@app.route("/GuessWho")
def guesswho():
    return render_template("GuessWhoBot.html")
@app.route("/animate")
def animate():
    return render_template("animate.html")

@app.route("/techHelp")
def techhelp():
    return render_template("techHelp.html")

@app.route("/language")
def language():
    return render_template("language.html")

@app.route("/WiseOldManChat")
def WiseOldManChat():
    return render_template("WiseOldManChat.html")

@app.route("/twenty")
def TwentyQuestions():
    return render_template("twentyquestions.html")

@app.route("/fun")
def have_fun():
    return render_template("fun.html")

@app.route('/song')
def song():
    return render_template("SongBot.html")

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