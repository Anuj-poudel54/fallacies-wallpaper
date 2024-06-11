""" Parser for data in files """

from pathlib import Path
import json
from typing import Generator

class FileParser:
    """ Parser for file """
    def __init__(self, file_path: None | str | Path = None) -> None:
        """ accepts file_path and not given searches for ./data/fallacies.txt file """

        self.file_path = file_path or Path("./data/fallacies.txt")

    def get_next_fallacy(self) -> Generator[dict[str, str]]:
        """ Generator for returning next line from the file """
        with open(self.file_path, "r") as f:
            while fallacy := f.readline(): ## f.readlines() returns "" at eof
                fallacy = json.loads(fallacy)
                yield fallacy


if __name__ == "__main__":
    parser = FileParser()

    for idx, fallacy in enumerate(parser.get_next_fallacy()):
        print(idx, fallacy)
        print("--"*50)
