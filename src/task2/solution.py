import csv
from collections import Counter
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://ru.wikipedia.org"
START_URL = BASE_URL + "/w/index.php?title=Категория:Животные_по_алфавиту&from=А"


def get_data_from_site() -> list[dict]:
    url = START_URL
    counts = Counter()

    session = requests.Session()
    while True:
        resp = session.get(url, timeout=5)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "lxml")
        for grp in soup.select(".mw-category-group"):
            letter = grp.h3.text.strip()
            counts[letter] += len(grp.find_all("li"))

        nxt = soup.find("a", string="Следующая страница")
        if not nxt:
            break
        url = urljoin(BASE_URL, nxt["href"])

    return [{"letter": L, "count": counts[L]} for L in sorted(counts)]


def write_data(path: str, data: list[dict]):
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["letter", "count"])
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    data = get_data_from_site()
    write_data("animals_by_letter.csv", data)
