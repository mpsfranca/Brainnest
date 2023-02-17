import os
import json
import time
import logging
import schedule
from smtplib import SMTP
from datetime import datetime
from email.message import EmailMessage

# Global Constants
CWD = os.getcwd()
DAILY_TIME = "10:57"
SRC_FOLDER = os.path.join(CWD, "src")
ATTACHMENT_FOLDER = os.path.join(CWD, "Reports")
FORMAT = "%(asctime)s : %(levelname)s - %(message)s"

# Logger configuration
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

file_handler = logging.FileHandler(os.path.join(SRC_FOLDER,
                                                "Automatic Email.log"))
file_handler.setFormatter(logging.Formatter(FORMAT))

logger = logging.getLogger("AES")
logger.addHandler(file_handler)


def create_email(subject, sender, receiver):
    '''
    Returns a string representing the email created.
            Parameters:
                    subject (str): The subject of the email
                    sender (str): The email address of the sender
                    receiver (str): The email address of the receiver
            Returns:
                    e.as_string() (str): String representation of the email.
    '''
    # Keeps track of the time the email was sent.
    time_stamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # Email creation
    e = EmailMessage()
    e["To"] = receiver
    e["From"] = "Brainnest - Automatic Email Sending"
    e["Subject"] = subject
    e.set_content(f"""
    This is an automatic email sent @ {time_stamp}.
    This email was sent from {sender} to {receiver}
    This email will be sent every 24 hours.
    """)

    # Attaching files
    for file in os.listdir(ATTACHMENT_FOLDER):
        try:
            with open(os.path.join(ATTACHMENT_FOLDER, file), "rb") as f:
                e.add_attachment(f.read(), maintype='application',
                                 subtype="txt", filename=file)
                logger.info(f"{file} has been attached to the email.")
        except Exception as ex:
            logger.exception(f"Error attaching {file}: {ex}.")

    return e.as_string()


def send(smtp, sender, receiver, email_obj):
    '''
    Sends the email to a given receiver.
            Parameters:
                    smtp : The SMTP server being used.
                    sender (str): The email address of the sender.
                    receiver (str): The email address of the receiver.
                    email_obj (str): The email to be sent.
            Returns:
                    None
    '''
    try:
        smtp.sendmail(sender, receiver, email_obj)
        logger.info(f"Email from {sender} has been sent to {receiver}")
    except Exception as ex:
        logger.exception(f"Email from {sender} was "
                         f"not sent to {receiver}: {ex}.")


def main():
    with SMTP("smtp.gmail.com", 587) as smtp:
        try:
            smtp.starttls()
            logger.info("Successfully started TLS.")
        except Exception as ex:
            logger.exception("Error starting TLS: {ex}.")

        try:
            # Getting information about sender and receivers
            with open(os.path.join(SRC_FOLDER, "settings.json"), "r") as rf:
                data = json.load(rf)
                logger.info("Successfully loaded settings.")
        except Exception as ex:
            logger.exception("Error while opening settings.json: {ex}")

        sender_email = data["SenderEmail"]
        sender_password = data["SenderPassword"]

        receiver_list = data["ReceiverList"]

        logger.debug(f"The sender email is: {sender_email}")
        logger.debug(f"The receiver's email list is: {receiver_list}")

        try:
            smtp.login(sender_email, sender_password)
            logger.info("Successfully logged into SMTP server.")
        except Exception as ex:
            logger.exception(f"Could NOT login to email {sender_email}: {ex}.")

        subject = "Automatic mail."
        for receiver in receiver_list:
            email_obj = create_email(subject, sender_email, receiver)
            send(smtp, sender_email, receiver, email_obj)


schedule.every().day.at(DAILY_TIME).do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
