from orator import Model
from discord import Embed
from helpers import boot_database


class Skill(Model):

    CONFIG = {
        'color':                         0xef952c,
    }

    def generateEmbed(self):
        skill_embed=Embed(title="Skill - {} - {}".format(self.school, self.name), description="{}".format(self.description), url="{}".format(self.url), color=self.CONFIG.get('color'))
        skill_embed.set_thumbnail(url="{}".format(self.thumbnail))
        skill_embed.add_field(name="Points", value="{}".format(self.points), inline=True)
        skill_embed.add_field(name="Cooldown", value="{}".format(self.cooldown), inline=True)
        skill_embed.add_field(name="Effects", value="{}".format(self.effects), inline=False)
        if self.armor_check is not None:
            skill_embed.add_field(name="Armour Check", value="{}".format(self.armor_check), inline=False)
        skill_embed.add_field(name="Spell Book Locations", value="{}".format(self.spell_book_locations), inline=False)
        if self.scroll_crafting is not None:
            skill_embed.add_field(name="Scroll Crafting", value="{}".format(self.scroll_crafting), inline=False)
        skill_embed.add_field(name="Notes", value="{}".format(self.notes), inline=False)
        skill_embed.set_footer(text="{} Skill".format(self.school), icon_url="{}".format(self.icon))
        return skill_embed
