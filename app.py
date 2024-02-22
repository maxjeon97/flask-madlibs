from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import set_templates

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def index():

    return render_template('index.html')


@app.get("/questions")
def questions():
    """Homepage that shows form prompting user for words in Madlibs story"""
    story_type = request.args["story_select"]
    story = set_templates[story_type]

    return render_template("questions.html", prompts=story.prompts)


@app.get("/results")
def result():
    """Displays result text from user Madlibs input"""
    story = set_templates["excited"].get_result_text(request.args)
    return render_template("results.html", story=story)
