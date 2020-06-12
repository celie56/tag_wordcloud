"""Extract tags from json tag files."""
from typing import List

import json
import codecs
import click

TAGS_KEY = 'tags'
TITLE_KEY = 'title'


def _extract_data_from_file(filepath: str) -> dict:
    try:
        return json.load(codecs.open(filepath, 'r', 'utf-8-sig'))

    # pylint: disable=broad-except
    except Exception as exc:
        print(f'error opening {filepath}: {exc}')

    return None


def from_file(filepath: str) -> str:
    """Returns space joined string of all tags in single file.

    >>> from_file('file_1')
    'tag_1 tag_2'

    >>> from_file('file_2')
    'tag_1 tag_3'
    """
    data = _extract_data_from_file(filepath)

    # unable to extract data, exit
    if not data:
        return ''

    tags = [
        tag_data[TITLE_KEY] for tag_data in data.get(TAGS_KEY)
        if tag_data.get(TITLE_KEY)
    ]
    return ' '.join(tags)


@click.command()
@click.argument('filepath', required=True)
def _from_file_cli(filepath: str) -> None:
    """CLI for from_file."""
    tags = from_file(filepath)
    print(tags)


def from_file_list(files: List[str]) -> str:
    """Returns space joined string of all tags in files.

    >>> from_file_list(['file_1', 'file_2'])
    'tag_1 tag_2 tag_1 tag_3'
    """
    return ' '.join(from_file(tag_file) for tag_file in files)


if __name__ == '__main__':
    # This parameter is handled by click
    # pylint: disable=no-value-for-parameter
    _from_file_cli()
