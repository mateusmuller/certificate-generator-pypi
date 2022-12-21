import os
import smtplib
import sys
import csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class CertificateGenerator:
    def __init__(self, subject, spreadsheet, certificate, x, y, font, font_size):
        try:
            self.email = os.environ["SMTP_EMAIL"]
            self.password = os.environ["SMTP_PASSWORD"]
            self.smtp_server = os.environ["SMTP_SERVER"]
            self.smtp_port = os.environ["SMTP_PORT"]
            self.email_subject = subject
            self.spreadsheet = spreadsheet
            self.certificate = certificate
            self.x = x
            self.y = y
            self.font = font
            self.font_size = font_size
        except TypeError as e:
            print(e)
            sys.exit(1)
        except KeyError as e:
            print(f"The environment variable {e} is missing.")
            sys.exit(1)

    def generate_certificate(self, student_name):
        try:
            file_name = f'{student_name.lower().replace(" ", "_")}.png'

            certificate = Image.open(self.certificate)
            certificate_draw = ImageDraw.Draw(certificate)
            font = ImageFont.truetype(self.font, self.font_size)
            certificate_draw.text(
                (self.x, self.y), student_name, font=font, fill=(0, 0, 0)
            )
            certificate.save(file_name, "PNG", resolution=100.0)
            return file_name
        except FileNotFoundError as e:
            print(f"The location of the file is wrong or not exist: {e}")
            sys.exit(1)

    def smtp_connection(self) -> smtplib.SMTP:
        try:
            smtp_connection = smtplib.SMTP(self.smtp_server, self.smtp_port)
            # smtp_connection.set_debuglevel(2)
            smtp_connection.starttls()
            smtp_connection.login(self.email, self.password)
            return smtp_connection
        except smtplib.SMTPAuthenticationError as e:
            print(f"Username or password are wrong, check exception: {e}")
            sys.exit(1)

    def send_email(self, email, smtp_connection, certificate):
        msg = MIMEMultipart()
        msg["From"] = self.email
        msg["To"] = email
        msg["Subject"] = self.email_subject
        body = "Segue em anexo seu certificado de conclusão."
        msg.attach(MIMEText(body, "plain"))
        attachment = open(certificate, "rb")
        part = MIMEBase("image", "png")
        part.set_payload(attachment.read())
        part.add_header("Content-Disposition", "attachment", filename=certificate)
        encoders.encode_base64(part)
        msg.attach(part)
        email_body = msg.as_string()
        smtp_connection.sendmail(self.email, email, email_body)

    def read_spreadsheet(self):
        try:
            with open(self.spreadsheet, "r") as spreadsheet:

                csv_reader = csv.reader(spreadsheet, delimiter=",")
                line_count = 0
                smtp_connection = self.smtp_connection()

                for row in csv_reader:
                    if line_count == 0:
                        pass
                    else:
                        full_name = row[0].title()
                        email = row[1]

                        certificate = self.generate_certificate(full_name)
                        self.send_email(email, smtp_connection, certificate)
                    line_count += 1

        except FileNotFoundError as e:
            print(f"The location of the file is wrong or not exist: {e}")
            sys.exit(1)

    def run(self):
        self.read_spreadsheet()
