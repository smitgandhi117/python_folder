from flask import Flask, jsonify

app = Flask(__name__)


# Dictionary of Justice League
justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

@app.route("/")
def home():
    return "heythere"


@app.route("/myfavsuperhero")
def jsonified():
    return jsonify(justice_league_members)

if __name__ == "__main__":
    app.run(debug=True)