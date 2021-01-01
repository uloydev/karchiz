from flask import Flask, render_template

app = Flask("__main__", static_url_path="/assets", template_folder="frontend/html", static_folder="frontend/assets")

@app.route('/')
@app.route('/home')
def index():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/orders')
def orders():
    return render_template("orders.html")

@app.route('/events')
def events():
    return render_template("events.html")


if __name__ == "__main__":
    app.run(debug=True)