from flask import *
from stories import *


app = Flask(__name__)



@app.route('/')
def show_form():
    """shows form to enter words for story"""

    prompts = story.prompts

    return render_template("home.html", prompts=prompts)



@app.route('/story')
def show_story():
    """shows story result"""

    text = story.generate(request.args)

    return render_template("story.html", text=text)

