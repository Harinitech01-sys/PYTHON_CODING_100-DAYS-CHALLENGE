
from flask import Flask, request, jsonify, render_template_string
from datetime import datetime
import json

app = Flask(__name__)

# Mock database
subscribers = {}

# HTML Page
HTML = """
<h1>Newsletter Subscription</h1>

<p>Privacy Notice: Your name and email are used only
for sending newsletter updates.</p>

<form action="/subscribe" method="post">
    <input name="name" placeholder="Enter Name" required><br><br>

    <input name="email" type="email"
           placeholder="Enter Email" required><br><br>

    <input type="checkbox" name="consent" value="yes" required>
    I agree to share my details.<br><br>

    <button type="submit">Subscribe</button>
</form>

<hr>

<form action="/export" method="get">
    <input name="email" placeholder="Enter Email" required>
    <button type="submit">Download My Data</button>
</form>

<form action="/erase" method="post">
    <input name="email" placeholder="Enter Email" required>
    <button type="submit">Delete My Data</button>
</form>
"""

# Home page
@app.route("/")
def home():
    return render_template_string(HTML)

# Subscribe
@app.route("/subscribe", methods=["POST"])
def subscribe():
    name = request.form["name"]
    email = request.form["email"].lower()
    consent = request.form.get("consent")

    if not consent:
        return "Consent is required!"

    subscribers[email] = {
        "name": name,
        "email": email,
        "consent": True,
        "date": str(datetime.now())
    }

    return "Subscription successful!"

# Export personal data
@app.route("/export")
def export():
    email = request.args.get("email", "").lower()

    if email not in subscribers:
        return "Subscriber not found!"

    return jsonify(subscribers[email])

# Delete personal data
@app.route("/erase", methods=["POST"])
def erase():
    email = request.form["email"].lower()

    if email in subscribers:
        del subscribers[email]
        return "Your data has been deleted!"

    return "Subscriber not found!"

# Run application
if __name__ == "__main__":
    app.run(debug=True)
