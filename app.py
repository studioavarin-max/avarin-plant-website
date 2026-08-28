from flask import Flask, render_template, abort

app = Flask(__name__)

PLANTS = {
    "snake-plant-care": {
        "title": "Snake Plant Care for Beginners",
        "category": "Plant Care",
        "description": "A simple guide to light, watering, soil, drainage and placement for a healthy snake plant.",
        "intro": "Snake plants are resilient indoor plants, but a simple routine helps them stay healthy and produce strong new growth.",
        "sections": [
            ("Light", "Bright, indirect light is a reliable starting point. Snake plants can tolerate lower light, but growth may be slower."),
            ("Watering", "Let the soil dry substantially between waterings. Check the soil rather than following a rigid calendar."),
            ("Soil & drainage", "Use a well-draining mix and a container with drainage holes so excess water can escape."),
            ("Placement", "Keep the plant somewhere with suitable light and reasonably stable indoor temperatures.")
        ]
    },
    "snake-plant-yellow-leaves": {
        "title": "Why Are My Snake Plant Leaves Turning Yellow?",
        "category": "Plant Problems",
        "description": "Learn the common causes of yellow snake plant leaves and what to check before changing your care routine.",
        "intro": "Yellow leaves can have several causes. Start by checking the soil, drainage, light, roots and the age of the affected leaf.",
        "sections": [
            ("Overwatering", "Snake plants store water and prefer the soil to dry between waterings. Constantly wet soil can stress roots and contribute to yellowing."),
            ("Poor drainage", "A pot without drainage holes can keep roots wet for too long. Make sure excess water has a way out."),
            ("Too much direct sunlight", "Intense direct sun can stress or scorch foliage. Bright, indirect light is a safer starting point."),
            ("Natural aging", "One older leaf slowly turning yellow can simply be part of the plant's natural growth cycle."),
            ("Temperature or environmental stress", "Sudden temperature changes or cold drafts can stress a houseplant. Keep conditions reasonably stable."),
            ("Pests", "Inspect both sides of leaves and around leaf joints for unusual marks or insects. Isolate affected plants when necessary.")
        ]
    },
    "snake-plant-watering": {
        "title": "How Often Should You Water a Snake Plant?",
        "category": "Plant Care",
        "description": "A practical guide to knowing when your snake plant actually needs water.",
        "intro": "There is no single watering schedule that works for every home. Soil moisture, light, temperature and the pot all matter.",
        "sections": [
            ("Check the soil first", "Before watering, check whether the soil has dried substantially. Avoid watering simply because a calendar says it is time."),
            ("Water thoroughly", "When it is time to water, moisten the mix thoroughly and allow excess water to drain away."),
            ("Adjust for the season", "Plants often use less water during darker or cooler periods and more during active growth."),
            ("Watch the leaves", "Soft, discolored or declining leaves can be a reason to inspect the roots and watering conditions.")
        ]
    },
    "snake-plant-mistakes": {
        "title": "7 Snake Plant Mistakes Beginners Make",
        "category": "Plant Tips",
        "description": "Avoid common beginner mistakes involving water, drainage, light, soil and placement.",
        "intro": "Snake plants are forgiving, but a few habits can make them struggle. Here are seven to watch for.",
        "sections": [
            ("1. Watering too often", "Check the soil before watering."),
            ("2. Using a pot without drainage", "Excess water needs a route out."),
            ("3. Keeping soil constantly wet", "Allow the mix to dry substantially between waterings."),
            ("4. Harsh direct sun", "Very intense sun can stress foliage."),
            ("5. Heavy soil", "Choose a mix that drains readily."),
            ("6. Unnecessary repotting", "Repot when there is a clear reason rather than too frequently."),
            ("7. Ignoring early warning signs", "Inspect leaves, soil and roots when the plant's appearance changes.")
        ]
    },
    "pothos-care": {
        "title": "Pothos Care for Beginners",
        "category": "Plant Care",
        "description": "A beginner-friendly starting guide to growing pothos indoors.",
        "intro": "Pothos is a versatile indoor plant with trailing growth and straightforward care needs.",
        "sections": [
            ("Light", "Bright, indirect light supports good growth, while pothos can also tolerate lower light."),
            ("Watering", "Check the soil before watering and avoid leaving the plant sitting in water."),
            ("Pruning", "Trim long or sparse growth with clean tools to encourage a fuller appearance."),
            ("Propagation", "Healthy cuttings can be rooted in water or an appropriate growing medium.")
        ]
    },
    "spider-plant-care": {
        "title": "Spider Plant Care for Beginners",
        "category": "Plant Care",
        "description": "Simple indoor care tips for growing a healthy spider plant.",
        "intro": "Spider plants are popular beginner houseplants with arching leaves and easy propagation.",
        "sections": [
            ("Light", "Bright, indirect light is ideal; avoid prolonged harsh direct sun."),
            ("Watering", "Keep a consistent routine while avoiding waterlogged soil."),
            ("Humidity", "Average indoor conditions often work, though dry air can affect leaf tips."),
            ("Propagation", "Mature plants can produce plantlets that are easy to root.")
        ]
    }
}

BOOKS = [
    {"title": "Plant & Gardening Books", "description": "Discover useful reading for beginners who want to understand houseplants, gardening and growing.", "url": "/books"}
]

@app.route("/")
def home():
    featured = [PLANTS["snake-plant-care"], PLANTS["snake-plant-yellow-leaves"], PLANTS["snake-plant-watering"]]
    return render_template("home.html", featured=featured, plants=PLANTS)

@app.route("/plant/<slug>")
def plant(slug):
    item = PLANTS.get(slug)
    if not item:
        abort(404)
    related = [v for k, v in PLANTS.items() if k != slug][:3]
    return render_template("plant.html", plant=item, slug=slug, related=related)

@app.route("/plants")
def plants():
    return render_template("library.html", plants=PLANTS)

@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
