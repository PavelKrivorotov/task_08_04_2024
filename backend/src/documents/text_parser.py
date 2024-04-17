import re

from fastapi import UploadFile


class TextParser:
    _pattern = re.compile(r'[A-Za-zА-Яа-я0-9_-]+')

    def __init__(self, file: UploadFile) -> None:
        self._words: dict[str, int] = {}
        self._count: int = 0
        self._parse(file)

    @property
    def words(self) -> dict[str, int]:
        return self._words
    
    @property
    def count(self) -> int:
        return self._count

    def _parse(self, file: UploadFile) -> None:
        text = file.file.read().decode()
        words = self._pattern.findall(text)

        for word in words:
            count = self._words.get(word, 0)
            self._words[word] = count + 1

            self._count += 1

    def change_key(self, old_key: str, new_key: str):
        value = self._words.pop(old_key)
        self._words[new_key] = value

