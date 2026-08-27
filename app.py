from flask import Flask, render_template, request, redirect, url_for, session, abort
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = os.environ.get("AVARIN_SECRET_KEY", "change-this-secret-key")

# Keep these credentials private. In production, use environment variables.
ADMIN_USER = os.environ.get("AVARIN_ADMIN_USER", "admin")
ADMIN_PASSWORD = os.environ.get("AVARIN_ADMIN_PASSWORD", "change-this-password")

PLANTS = {
    "snake-plant-care": {
        "title": "Snake Plant Care for Beginners",
        "category": "Plant Care",
        "summary": "A simple guide to light, watering, soil and drainage for a healthy snake plant.",
        "tips": [
            ("Light", "Bright, indirect light is ideal. Snake plants can tolerate lower light too."),
            ("Water", "Let the soil dry between waterings. Avoid keeping the roots constantly wet."),
            ("Soil", "Use a well-draining potting mix."),
            ("Pot", "Choose a container with drainage holes.")
        ]
    }
}

def admin_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("admin"):
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)
    return wrapped

@app.route("/")
def home():
    return render_template("home.html", plants=PLANTS)

@app.route("/plant/<slug>")
def plant(slug):
    item = PLANTS.get(slug)
    if not item:
        abort(404)
    return render_template("plant.html", plant=item, slug=slug)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("username") == ADMIN_USER and request.form.get("password") == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect(request.args.get("next") or url_for("admin"))
        error = "Invalid login."
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route("/admin")
@admin_required
def admin():
    return render_template("admin.html", plants=PLANTS)

if __name__ == "__main__":
    app.run(debug=True)
