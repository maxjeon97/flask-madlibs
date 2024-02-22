from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def questions():
    """Homepage that shows form prompting user for words in Madlibs story"""
    return render_template("questions.html", prompts=excited_story.prompts)


@app.get("/results")
def result():
    """Displays result text from user Madlibs input"""
    story = excited_story.get_result_text(request.args)
    return render_template("results.html", story=story)
