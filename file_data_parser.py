from pathlib import Path
import json

class FileParser:
    def __init__(self, file_path: None | str | Path = None) -> None:

        self.file_path = file_path or Path("./data/fallacies.txt")

    def get_next_fallacy(self):
        with open(self.file_path, "r") as f:
            while fallacy := f.readline(): ## f.readlines() returns "" at eof
                fallacy = json.loads(fallacy)
                yield fallacy


if __name__ == "__main__":
    parser = FileParser()

    for idx, fallacy in enumerate(parser.get_next_fallacy()):
        print(idx, fallacy)
        print("--"*50)
