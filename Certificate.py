from ssl import get_server_certificate, PEM_cert_to_DER_cert


class Certificate:

    def __init__(self, url):
        self.url = url
        self.PEM = None
        self.error = None

        try:
            self.PEM = get_server_certificate((url, 443), timeout=5)
        except Exception as e:
            self.error = e

        self.DER = PEM_cert_to_DER_cert(self.PEM)


del get_server_certificate, PEM_cert_to_DER_cert
