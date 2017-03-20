"""Server for project"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# raises error if you use an undefined variable in Jinja2
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Landing page"""

    return render_template("index.html")



@app.route('/contact', methods=["GET"])
def contact():
    """Profile page"""

    return render_template("contact.html")



@app.route('/left', methods=["GET"])
def left():
    """Profile page"""

    return render_template("left-sidebar.html")



@app.route('/right', methods=["GET"])
def right():
    """Profile page"""

    return render_template("right-sidebar.html")



@app.route('/no', methods=["GET"])
def no():
    """Profile page"""

    return render_template("no.html")






@app.route('/profile', methods=["GET"])
def profile():
    """Profile page"""

    return render_template("profile.html")



@app.route('/fare-share', methods=["GET"])
def fare_share():
    """Fare Share project page"""

    return render_template("fare-share.html")



@app.route('/skater-workout-generator', methods=["GET"])
def skate():
    """Skate project page"""

    return render_template("skate.html")



@app.route('/amelia', methods=["GET"])
def amelia():
    """Amelia project page"""

    return render_template("amelia.html")



@app.route('/portfolio', methods=["GET"])
def portfolio():
    """Portfolio project page"""

    return render_template("portfolio.html")






if __name__ == "__main__":
#     # We have to set debug=True here, since it has to be True at the point
#     # that we invoke the DebugToolbarExtension
    app.debug = True

#     # Use the DebugToolbar
#     DebugToolbarExtension(app)

    app.run()