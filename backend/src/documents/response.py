import typing

from main import settings


def make_response_content(
        data: dict[str, typing.Any],
        count: int
    ) -> dict[str, typing.Any]:

        return {
            'count': count,
            'count_per_page': settings.PAGINATION['DEFAULT_COUNT_PER_PAGE'],
            'result': data
        }

