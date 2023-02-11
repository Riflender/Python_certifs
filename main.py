from os import listdir, cpu_count
from requests import get
import ssl
import threading

from time import time


def get_cert(url: str, cert_list: list, error_list: list, cert_lock: threading.Lock, error_lock: threading.Lock):
    try:
        cert = ssl.PEM_cert_to_DER_cert(ssl.get_server_certificate((url, 443), timeout=5))
        with cert_lock:
            cert_list.append(cert)
    except Exception as e:
        with error_lock:
            error_list.append((url, e))


MAX_CPU = cpu_count()

if "urls" not in listdir("."):
    with open("urls", "wb") as f:
        r = get("https://raw.githubusercontent.com/Alvir4/url/main/urls", allow_redirects=True)
        f.write(r.content)
if "sorted_urls" not in listdir("."):
    with open("urls", "r") as fr:
        tmp = "\n".join(sorted([x.replace("\n", "") for x in fr.readlines()[1:]]))

        with open("sorted_urls", "w") as fw:
            fw.write(f"Domain\n{tmp}\n")

with open("urls", "r") as f:
    url_list = [x.replace("\n", "") for x in f.readlines()][1:]

part_list = url_list[:234]

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

print(f"{len(error_list)} erreurs sur {len(url_list):_} URLs")

print()
