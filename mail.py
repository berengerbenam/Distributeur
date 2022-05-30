from flask import Flask
from flask_mail import Mail, Message
app =Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'berengerbenam@gmail.com'
app.config['MAIL_PASSWORD'] = 'mot de passe '
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
@app.route("/mail/<string:destinataire>/<string:objet>/<string:message>")
def index(destinataire,objet,message):
    msg = Message(objet, sender = 'berengerbenam@gmail.com', recipients = [destinataire])
    msg.body = message
    mail.send(msg)
    return "Envoye"
if __name__ == '__main__':
    app.run(debug = True)
