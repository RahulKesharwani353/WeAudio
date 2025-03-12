import smtplib, os, json
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()


def sendEmailNotification(message):
    message = json.loads(message)
    mp3_fid = message["audio_fid"]
    sender_address = os.getenv("GMAIL_ADDRESS")
    sender_password = os.getenv("GMAIL_PASSWORD")
    receiver_address = 'rahulkesharwani353@gmail.com'

    msg = EmailMessage()
    msg.set_content(f"mp3 file_id: {mp3_fid} is now ready!\n\nDownload it from the link below:\n\nhttp://localhost:8000/file/download/{mp3_fid}")
    msg["Subject"] = "MP3 Download"
    msg["From"] = sender_address
    msg["To"] = receiver_address

    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.starttls()
    session.login(sender_address, sender_password)
    session.send_message(msg, sender_address, receiver_address)
    session.quit()
    print("Mail Sent")