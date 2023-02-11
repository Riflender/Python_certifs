from ssl import get_server_certificate, PEM_cert_to_DER_cert


class Certificate:

    def __init__(self, url):
        self.url = url
        self.PEM = None
        self.DER = None
        self.error = None

        try:
            self.PEM = get_server_certificate((url, 443), timeout=5)
            self.DER = PEM_cert_to_DER_cert(self.PEM)
        except Exception as e:
            self.error = e
