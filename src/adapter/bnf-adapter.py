from typing import List
from lark import Lark


class Parser:
    pass


class FileParser:

    # Заглушка
    def get_files_list(self, dirname: str) -> List[str]:
        bnf_file_list = []

        for bnf_file in bnf_file_list:
            if bnf_file.lower().endswith(".bnf"):
                bnf_file_list.append(bnf_file)

        return bnf_file_list

    # Заглушка
    def open_file(self, filename: str):
        with open(filename):
            pass


class LarkAdapter:
    pass


