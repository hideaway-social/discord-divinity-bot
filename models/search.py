from bs4 import BeautifulSoup
import urllib.parse
import requests
import re
from discord import Embed
from helpers import cleanhtml


class Search:

    CONFIG = {"color": 9989819}

    def __init__(self, query):
        self.query = query
        self.url_encoded_query = urllib.parse.urlencode(
            {"q": "site:divinityoriginalsin2.wiki.fextralife.com {}".format(query)}
        )
        self.results = self.performSearch()

    def performSearch(self):
        page_data = requests.get(
            "https://www.google.com/search?{}".format(self.url_encoded_query)
        )
        soup = BeautifulSoup(page_data.text)

        search_embed = Embed(
            title='Search Results - "{}"'.format(self.query),
            description="",
            url="https://www.google.com/search?{}".format(self.url_encoded_query),
            color=self.CONFIG.get("color"),
        )
        EM_RE = re.compile(r"<em>|</em>|<b>|</b>")
        BR_RE = re.compile(r"<br>|</br>|<br/>")
        GOOGLE_RE = re.compile(
            r'<span class="st">\S\S\S \S?\S, \S\S\S\S \*\*...\*\*|<\/span>'
        )
        DIVINITY_RE = re.compile(r" \| Divinity Original Sin 2 Wiki")

        image_box = soup.find(text=re.compile(r"^Images for.*"))

        if image_box is not None:
            image_box.parent.parent.parent.decompose()
        for result in soup.findAll("div", class_="g", id_=None)[:5]:
            link_tree = result.find("h3", class_="r")
            description = result.find("span", class_="st")
            description = EM_RE.sub("**", str(description))
            description = BR_RE.sub("", str(description))
            description = GOOGLE_RE.sub("", str(description))
            title = DIVINITY_RE.sub("", cleanhtml(link_tree))
            search_embed.add_field(
                name="{}".format(title),
                value="[{}]({})\n{}".format(
                    link_tree.a["href"][7:-83],
                    link_tree.a["href"][7:-83],
                    cleanhtml(description),
                ),
                inline=False,
            )
        return search_embed


def has_class_but_no_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")
