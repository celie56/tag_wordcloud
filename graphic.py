"""Generate graphic wordcloud.

$ python graphic.py "xyz abc def"
"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import click


def generate_graphic_from_tags(tags: str) -> None:
    """Given a space seperated string of tags, show a wordcloud."""
    cloud = WordCloud(background_color="white").generate(tags)
    plt.axis("off")
    plt.imshow(cloud)
    plt.show()


@click.command()
@click.argument('tags', required=True)
def _graphic_cli(tags: str) -> None:
    generate_graphic_from_tags(tags)


if __name__ == '__main__':
    # This parameter is handled by click
    # pylint: disable=no-value-for-parameter
    _graphic_cli()
