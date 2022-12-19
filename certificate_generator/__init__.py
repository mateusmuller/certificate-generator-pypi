import os
import sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class CertificateGenerator():

    def __init__(
            self, subject, body, spreadsheet, certificate,
            x, y, font
    ):
        try:
            self.email = os.environ["SMTP_EMAIL"]
            self.password = os.environ["SMTP_PASSWORD"]
            self.smtp_server = os.environ["SMTP_SERVER"]
            self.smtp_port = os.environ["SMTP_PORT"]
            self.email_subject = subject
            self.email_body = body
            self.spreadsheet = spreadsheet
            self.certificate = certificate
            self.x = x
            self.y = y
            self.font = font
        except TypeError as e:
            print(e)
            sys.exit(1)
        except KeyError as e:
            print(f'The environment variable {e} is missing.')
            sys.exit(1)

    def generate_certificate(self, student_name):
        file_name = f'{student_name.lower().replace(" ", "_")}.png'

        certificate = Image.open(self.certificate)
        certificate_draw = ImageDraw.Draw(certificate)
        font = ImageFont.truetype(self.font, 200)
        certificate_draw.text((self.x, self.y),
                              student_name,
                              font=font,
                              fill=(0, 0, 0))
        certificate.save(file_name, "PNG", resolution=100.0)
