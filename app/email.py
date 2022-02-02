import app
from threading import Thread
from flask import current_app,render_template
from flask_mail import Message
from datetime import datetime


def send_async_email(app, msg):
    with app.app_context():
        app.mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body,
               attachments=None, sync=False):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    if attachments:
        for attachment in attachments:
            msg.attach(*attachment)
    if sync:
        app.mail.send(msg)
    else:
        Thread(target=send_async_email,
            args=(current_app._get_current_object(), msg)).start()

def send_contact_form(form_json):
    now = datetime.now()
    time = now.strftime(" %H:%M  %d %B, %Y")
    send_email('[Fiore] New Contact Request ' + time,
    sender=app.app.config['ADMINS'][0], recipients=app.app.config['ADMINS'],
    text_body=render_template('email/contact_.txt', contact_data=form_json),
    html_body=render_template('email/contact_.html',contact_data=form_json),            
    sync=True)