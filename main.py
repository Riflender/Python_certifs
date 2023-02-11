from concurrent.futures import ThreadPoolExecutor
from time import time

from Data import Data
from Certificate import Certificate
from utils import *


data = Data()
part_list = data.get_part_list(100)

cert_list = []
with ThreadPoolExecutor(MAX_THREAD()) as executor:
    start = time()
    futures = [executor.submit(Certificate, url) for url in part_list]

for future in futures:
    cert_list.append(future.result())

print(f"Temps = {(time() - start) / 60:.2f} minutes")
print(f"{len([x for x in cert_list if x.error is not None])} erreurs sur {len(part_list):_} URLs")
