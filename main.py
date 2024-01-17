import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Set up the SMTP server
smtp_server = "smtp-relay.brevo.com"
smtp_port = 587
smtp_username = "muhammadosama0121@gmail.com"
smtp_password = "nQA0tbRPkBWVSEfT"

# Set up the email message
message = MIMEMultipart()
message["From"] = "mcs.nust@gmail.com"
message["To"] = "haa227844@gmail.com"
message["Subject"] = "Security Alert Immediate Action Required for Your Server"
body = """Dear Arsal jadoon,

I hope this email finds you in good health. I am writing to express my concerns about your recent performance in the lab assessments. Your marks indicate a deviation from your usual standard, and I wanted to check in with you to ensure everything is okay.

I understand that various factors can impact academic performance, and I want to offer my support. If there are any challenges you are facing, whether personal or academic, that are affecting your results, please feel free to share them with me. I am here to assist you and explore potential solutions together.

Additionally, if you feel that you need extra help or clarification on any lab concepts, please don't hesitate to reach out. I am more than willing to provide guidance or recommend additional resources to aid in your understanding.

Remember that your academic success is important to us, and we are here to support you throughout your learning journey. If there's anything specific you would like to discuss or if you have questions about the recent assessments, please reply to this email, and we can schedule a time to talk.

I believe in your capabilities, and I am confident that with the right support, you can overcome any challenges you may be facing. Looking forward to hearing from you soon.

Best regards,

Engineer Kinza Abidin"""

message.attach(MIMEText(body, "plain"))

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    text = message.as_string()
    server.sendmail(message["From"], message["To"], text)
    print("Email sent!")