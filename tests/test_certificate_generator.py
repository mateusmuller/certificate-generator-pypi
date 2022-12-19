import certgenerator
import pytest
import os


class TestCertificateGenerator():

    @pytest.fixture()
    def client(self):
        os.environ["SMTP_EMAIL"] = "demo@demo.com"
        os.environ["SMTP_PASSWORD"] = "pass"
        os.environ["SMTP_SERVER"] = "smtp.demo.com"
        os.environ["SMTP_PORT"] = "589"

        yield certgenerator.CertificateGenerator(
            '[WORKSHOP FEEVALE] - Certificado de Conclusão',
            'participantes.csv',
            'certificate_template.png',
            640,
            1000,
            'DejaVuSans.ttf',
            200
        )

    def test_certificate_generate(self, client):
        filename = client.generate_certificate("NAme HeRE Test")
        assert filename == "name_here_test.png"
        assert os.path.exists(filename)
        os.remove(filename)

    def test_send_email(self, client):
        pass
