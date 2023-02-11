import threading
from time import time

from Data import Data
from Certificate import Certificate
from utils import *


def get_cert(url: str, cert_list: list[list[Certificate]], cert_lock: list[threading.Lock]):
    for i in range(MAX_THREAD()):
        if not cert_lock[i].locked():
            cert_lock[i].acquire(timeout=5)
            cert_list[i].append(Certificate(url))
            cert_lock[i].release()
            return


data = Data()
part_list = data.get_minute_list()

cert_list = [[] for x in range(MAX_THREAD())]
cert_lock = [threading.Lock() for y in range(MAX_THREAD())]

a = time()

threads = [threading.Thread(target=get_cert, args=(url, cert_list, cert_lock)) for i, url in enumerate(part_list)]
while threads:
    for i in range(min(len(threads), 8)):
        thread = threads.pop(0)
        thread.start()
        thread.join()

print(f"{time() - a:.2f}")

print(f"{0} erreurs sur {len(part_list):_} URLs")
