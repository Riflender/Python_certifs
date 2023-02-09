import requests
import ssl
from urllib3.exceptions import InsecureRequestWarning
from multiprocessing import cpu_count
from os import listdir
from time import time

# noinspection PyUnresolvedReferences
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
MAX_CPU = cpu_count()

if "urls" not in listdir("."):
    with open("urls", "wb") as f:
        r = requests.get("https://raw.githubusercontent.com/Alvir4/url/main/urls", allow_redirects=True)
        f.write(r.content)
if "sorted_urls" not in listdir("."):
    with open("urls", "r") as fr:
        tmp = "\n".join(sorted([x.replace("\n", "") for x in fr.readlines()[1:]]))

        with open("sorted_urls", "w") as fw:
            fw.write(f"Domain\n{tmp}\n")


with open("sorted_urls", "r") as f:
    url_list = [x.replace("\n", "") for x in f.readlines()][1:]

part_list = url_list[:234]

a = time()

cert_list = []
errors = 0
for url in part_list:
    try:
        # r = requests.get(f"https://{url}", timeout=5, verify=False)
        v = ssl.get_server_certificate((url, 443), timeout=5)
        w = ssl.PEM_cert_to_DER_cert(v)
        cert_list.append(w)
    except (requests.Timeout, requests.ConnectionError) as e:
        errors += 1
        print(f"{errors}) {e}")
    except ConnectionRefusedError:
        errors += 1
        print(f"{errors}) {url}")

b = time()
print((b - a) / 60)

print()
