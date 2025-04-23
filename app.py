from flask import Flask, render_template, request

app = Flask(__name__)

# Response rules
def get_response(user_input):
    user_input = user_input.lower()

    if "24 hours" in user_input or "operate" in user_input:
        return "Yes, we operate 24 hours every day."
    elif "refund" in user_input or "cancel" in user_input:
        return "Yes, we offer refunds for cancellations made 24 hours before departure."
    elif "contact" in user_input or "driver" in user_input:
        return "For security reasons, we only share driver contact details 2 hours before departure via SMS."
    else:
        return "I'm here to help with booking-related queries. Try asking about operation hours, refunds, or driver contact."

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    bot_response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = get_response(user_input)
    return render_template("index.html", user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
