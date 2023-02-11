import threading
from time import time

from Data import Data
from utils import *


def get_cert(url: str, cert_list: list, error_list: list, cert_lock: threading.Lock, error_lock: threading.Lock):
    try:
        cert = get_DER_cert(url)
        with cert_lock:
            cert_list.append(cert)
    except Exception as e:
        with error_lock:
            error_list.append((url, e))


data = Data()
part_list = data.get_minute_list()

cert_list = []
error_list = []

a = time()

# cert_locks = [threading.Lock() for i in range(8)]
cert_lock = threading.Lock()
error_lock = threading.Lock()
threads = [threading.Thread(target=get_cert, args=(url, cert_list, error_list, cert_lock, error_lock), name=f"th{i % 8}") for i, url in enumerate(part_list)]
while threads:
    for i in range(min(len(threads), 8)):
        thread = threads.pop(0)
        thread.start()
        thread.join()

"""
for url in part_list:
    try:
        cert_list.append(ssl.PEM_cert_to_DER_cert(ssl.get_server_certificate((url, 443), timeout=5)))
    except Exception as e:
        error_list.append((url, e))
"""

print(f"{time() - a:.2f}")

print(f"{len(error_list)} erreurs sur {len(part_list):_} URLs")
