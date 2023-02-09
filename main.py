from multiprocessing import cpu_count
from os import listdir
from requests import get
import ssl

from time import time

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

for url in part_list:
    try:
        pem = ssl.get_server_certificate((url, 443), timeout=5)
        der = ssl.PEM_cert_to_DER_cert(pem)
        cert_list.append(der)
    except Exception as e:
        error_list.append((url, e))

print(f"{time() - a:.2f}")

print(f"{error_list.__len__()} erreurs sur {url_list.__len__():_} URLs")

print()
