from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    games = [
        {"name": "FC Mobile VN", "icon": "FC", "bg": "#f34a2d"},
        {"name": "Liên Quân", "icon": "LQ", "bg": "#ffb703"},
        {"name": "Free Fire", "icon": "FF", "bg": "#00a8e8"},
        {"name": "Delta Force", "icon": "DF", "bg": "#ff6b35"},
        {"name": "Nạp Số", "icon": "S", "bg": "#26b5a6"},
        {"name": "FC Online (VN)", "icon": "FC", "bg": "#0ea5e9"},
        {"name": "FC Online M", "icon": "M", "bg": "#00c49a"},
    ]
    return render_template("index.html", games=games)

if __name__ == "__main__":
    app.run(debug=True)