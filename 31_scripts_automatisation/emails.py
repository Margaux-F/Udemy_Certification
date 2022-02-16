import smtplib
import emails_config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# ENVOYER DES EMAILS
# gmail

"""config_email
config_password
config_server
config_server_port"""

def envoyer_email(email_destinataire, sujet, message):

    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = sujet
    multipart_message["From"] = emails_config.config_email
    multipart_message["To"] = email_destinataire

    multipart_message.attach(MIMEText(message, "plain"))

    serveur_mail = smtplib.SMTP(emails_config.config_server, emails_config.config_server_port)
    serveur_mail.starttls()
    serveur_mail.login(emails_config.config_email, emails_config.config_password)
    serveur_mail.sendmail(emails_config.config_email, email_destinataire, multipart_message.as_string())
    serveur_mail.quit()

message_email = """Bonjour,

Comment allez-vous ?

Merci.
"""

envoyer_email("jonathan@codeavecjonathan.com", "Email depuis Python", message_email)




