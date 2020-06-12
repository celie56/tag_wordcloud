"""Generate wordcloud for all tags in directory.

$ python main.py ~/notes
"""
import click

import graphic
import get_tag_files
import pull_tags


@click.command()
@click.argument('root_dir', required=True)
def generate_wordcloud(root_dir: str) -> None:
    """Generate wordcloud for all tags in root_dir."""
    file_list = get_tag_files.from_root(root_dir)
    tags = pull_tags.from_file_list(file_list)
    graphic.generate_graphic_from_tags(tags)


if __name__ == '__main__':
    # This parameter is handled by click
    # pylint: disable=no-value-for-parameter
    generate_wordcloud()
