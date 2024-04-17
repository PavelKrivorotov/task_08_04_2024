from fastapi import Query

from main import settings


class Filter:
    def __init__(self, page: int = Query(default=1, ge=1)) -> None:
        self._page = page
    
    @property
    def page(self) -> int:
        return self._page
    
    def limit(self) -> int:
        return settings.PAGINATION['DEFAULT_COUNT_PER_PAGE']
    
    def offset(self) -> int:
        return (self._page - 1) * settings.PAGINATION['DEFAULT_COUNT_PER_PAGE']

