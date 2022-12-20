import certgenerator
import pytest
import os
from io import BytesIO
from PIL import Image


class TestCertificateGenerator:
    @pytest.fixture()
    def client(self):
        os.environ["SMTP_EMAIL"] = "demo@demo.com"
        os.environ["SMTP_PASSWORD"] = "pass"
        os.environ["SMTP_SERVER"] = "smtp.demo.com"
        os.environ["SMTP_PORT"] = "589"

        yield certgenerator.CertificateGenerator(
            "[WORKSHOP FEEVALE] - Certificado de Conclusão",
            "participantes.csv",
            "certificate.png",
            640,
            1000,
            "DejaVuSans.ttf",
            200,
        )

    @pytest.fixture()
    def certificate_image(self):
        file = BytesIO()
        image = Image.new("RGBA", size=(50, 50), color=(155, 0, 0))
        image.save(file, "png")
        file.name = "certificate.png"
        file.seek(0)
        with open("certificate.png", "wb") as f:
            f.write(file.getbuffer())
        yield
        os.remove("certificate.png")

    def test_certificate_generate(self, certificate_image, client):
        filename = client.generate_certificate("NAme HeRE Test")
        assert filename == "name_here_test.png"
        assert os.path.exists(filename)
        os.remove(filename)
