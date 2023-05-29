import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
import os


class ContactForm(FlaskForm):
    name = StringField('Vardas', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired()])
    subject = StringField('Tema')
    message = TextAreaField('Žinutė', validators=[DataRequired()])
    recaptcha = RecaptchaField()


def send_email(name, email, subject, message):
    sender_email = 'zygimantas@mozuraitis.lt'
    sender_password = os.getenv("EMAIL_PASSWORD")
    receiver_email = 'as@lordas.lt'

    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = receiver_email
    email_message['Subject'] = subject

    message_with_email = f"Siuntėjo paštas: {email}\n\n{message}"
    email_message.attach(MIMEText(message_with_email, 'plain'))

    smtp_server = 'dusia.serveriai.lt'
    smtp_port = 587

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(email_message)

    return True
