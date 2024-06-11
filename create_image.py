from file_data_parser import FileParser
from data_type import Fallacy

file_parser = FileParser()

for fallacy in file_parser.get_next_fallacy():
    ### TODO: To create image from data

    fallacy = Fallacy(**fallacy)

    print(fallacy.title)
    print(fallacy.desc[:20])
    print(fallacy.ext_desc[:20])
    print(fallacy.example[:20])
    print("--"*50)
