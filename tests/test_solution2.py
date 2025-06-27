from src.task2.solution import get_data_from_site, write_data
from pathlib import Path
import csv


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        return [
            {'letter': row['letter'], 'count': int(row['count'])}
            for row in reader
        ]


def test_get_data_from_site(tmp_path):
    data = get_data_from_site()

    fp = tmp_path / 'beasts.csv'
    write_data(str(fp), data)

    temp_data = read_csv(fp)
    assert temp_data == data
