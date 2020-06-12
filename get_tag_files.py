"""Get all tag files.

Tag files follow the format:
    {root_dir}/.../.ts/.../{file_name}.md.json
"""
from typing import List
from pathlib import Path
import click

GLOB = '*.md.json'


@click.command()
@click.argument('root_dir', required=True)
def from_root(root_dir: str) -> List[str]:
    """Return all tag filepaths under root_dir.

    >>> from_root('~/notes/bad_example')
    []

    >>> from_root('~/notes/weekly')
    [
    '/home/chris/notes/weekly/.ts/May 22nd This week with Chris.md.json',
    '/home/chris/notes/weekly/.ts/June 5th This week with Chris.md.json',
    '/home/chris/notes/weekly/.ts/May 26th This week with Chris.md.json',
    '/home/chris/notes/weekly/.ts/May 15th This week with Chris.md.json',
    '/home/chris/notes/weekly/.ts/June 8th This week with Chris.md.json'
    ]
    """
    root = Path(root_dir)
    print(list(map(str, root.rglob(GLOB))))


if __name__ == '__main__':
    # This parameter is handled by click
    # pylint: disable=no-value-for-parameter
    from_root()
