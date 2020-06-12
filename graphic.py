"""Generate graphic wordcloud."""
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_graphic_from_tags(tags: str) -> None:
    """Given a space seperated string of tags, show a wordcloud."""
    cloud = WordCloud(background_color="white").generate(tags)
    plt.axis("off")
    plt.imshow(cloud)
    plt.show()
