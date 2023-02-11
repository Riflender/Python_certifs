from os import cpu_count
from ssl import get_server_certificate, PEM_cert_to_DER_cert

MAX_CPU = cpu_count()


@property
def MAX_THREAD():
    return 2 * MAX_CPU


def get_DER_cert(url):
    return PEM_cert_to_DER_cert(get_server_certificate((url, 443), timeout=5))


del cpu_count
del get_server_certificate, PEM_cert_to_DER_cert
