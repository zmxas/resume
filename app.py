import os
from flask import Flask, request, render_template
from siusti import send_email, ContactForm
from dotenv import load_dotenv
from atsisiusti import atsisiusti
from istraukti import cv

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["RECAPTCHA_PUBLIC_KEY"] = os.getenv("RECAPTCHA_PUBLIC_KEY")
app.config["RECAPTCHA_PRIVATE_KEY"] = os.getenv("RECAPTCHA_PRIVATE_KEY")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    message_sent = False
    cv_info = cv()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        result = send_email(name, email, subject, message)
        if result:
            message_sent = True

    return render_template('index.html', form=form, message_sent=message_sent, pareigos=cv_info[0] if cv_info else "", imone=cv_info[1] if cv_info else "", trukme=cv_info[2] if cv_info else "")


@app.route("/download")
def download():
    return atsisiusti()


if __name__ == '__main__':
    app.run(debug=True)
