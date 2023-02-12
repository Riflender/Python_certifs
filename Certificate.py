from ssl import get_server_certificate
import OpenSSL
from cryptography import x509
from time import time


class Certificate:

    def __init__(self, url):
        self.url = url
        self.PEM = None
        self.cert = None
        self.algorithm = None
        self.error = None

        try:
            self.PEM = get_server_certificate((url, 443), timeout=5)
            self.cert = x509.load_pem_x509_certificate(self.PEM.encode())
            self.algorithm = self.cert.signature_algorithm_oid._name
        except Exception as e:
            self.error = e

    def __len__(self):
        return len(self.PEM)
