from flask import Flask, render_template, request
from backend import generate_itinerary as generate_gemini_itinerary
from local_model import generate_local_itinerary
import markdown

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    itinerary = ""
    if request.method == "POST":
        name = request.form["name"]
        present = request.form["present"]
        destination = request.form["destination"]
        interests = request.form["interests"]
        dates = request.form["dates"]
        budget = request.form["budget"]
        model_choice = request.form.get("model")

        if model_choice == "local":
            raw_itinerary = generate_local_itinerary(name, present, destination, interests, dates, budget)
        else:
            raw_itinerary = generate_gemini_itinerary(name, present, destination, interests, dates, budget)

        itinerary = markdown.markdown(raw_itinerary)

    return render_template("index.html", itinerary=itinerary)
