from requests import get
from os import listdir


class Data:
    def __init__(self):
        self.link = "https://raw.githubusercontent.com/Alvir4/url/main/urls"
        self._urls_name = "urls.txt"
        self._sorted_urls_name = "sorted_urls.txt"

        self.url_list = []
        self.sorted_urls = []

        if self._urls_name not in listdir("."):
            self._download()

        self._let()

        if self._sorted_urls_name not in listdir("."):
            self._sort()
        
        self._let_sort()

    def _download(self):
        with open(self._urls_name, "wb") as f:
            f.write(get(self.link, allow_redirects=True).content)

    def _let(self):
        with open(self._urls_name, "r") as f:
            self.url_list = [x.replace("\n", "") for x in f.readlines()[1:]]

    def _sort(self):
        tmp = "\n".join(sorted(self.url_list))
        with open(self._sorted_urls_name, "w") as fw:
            fw.write(f"Domain\n{tmp}\n")

    def _let_sort(self):
        with open(self._sorted_urls_name, "r") as f:
            self.sorted_urls = [x.replace("\n", "") for x in f.readlines()[1:]]

    def get_part_list(self, nb_urls):
        return self.url_list[:nb_urls]

    @property
    def get_minute_list(self):
        return self.url_list[:234]
