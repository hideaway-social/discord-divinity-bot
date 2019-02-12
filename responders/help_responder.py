from helpers import clean_content
from discord import Embed
import hunspell


class HelpResponder:
    def __init__(self, message):
        self.original_message = message
        self.query = clean_content(self.original_message.content, "!help")

    def getReply(self):
        help_embed = Embed(title="Bot Help", description="")
        help_embed.add_field(
            name="!build | !builds $query",
            value="Does a lookup of the various builds that have been created for DOS2.",
            inline=False,
        )
        help_embed.add_field(
            name="!skill | !skills $query",
            value="Does a lookup of all skills in the game matching the query.",
            inline=False,
        )
        help_embed.add_field(
            name="!search $query",
            value="Performs a search on the Divinity Orginal Sin 2 Wiki and returns the top 5 results.",
            inline=False,
        )
        help_embed.add_field(
            name="!github",
            value="Returns a link to the GitHub repo for this chat bot.",
            inline=False,
        )
        help_embed.add_field(
            name="!help $query",
            value="Get help on any particular command or for how to use the bot.",
            inline=False,
        )

        return {"content": "", "embed": help_embed}
