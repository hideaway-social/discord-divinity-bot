from orator import Model
from discord import Embed


class Skill(Model):

    CONFIG = {"color": 0xEF952C}

    def generateSingleEmbed(self):
        skill_embed = Embed(
            title="Skill - {} - {}".format(self.school, self.name),
            description="{}".format(self.description),
            url="{}".format(self.url),
            color=self.CONFIG.get("color"),
        )
        skill_embed.set_thumbnail(url="{}".format(self.thumbnail))
        if self.points is not None:
            skill_embed.add_field(name="Points", value="{}".format(self.points))
        if self.cooldown is not None:
            skill_embed.add_field(name="Cooldown", value="{}".format(self.cooldown))
        if self.effects is not None:
            skill_embed.add_field(
                name="Effects", value="{}".format(self.effects), inline=False
            )
        if self.armor_check is not None:
            skill_embed.add_field(
                name="Armour Check", value="{}".format(self.armor_check), inline=False
            )
        if self.spell_book is not None:
            skill_embed.add_field(
                name="Spell Book", value="{}".format(self.spell_book), inline=False
            )
        if self.spell_scroll is not None:
            skill_embed.add_field(
                name="Spell Scroll", value="{}".format(self.spell_scroll), inline=False
            )
        if self.notes is not None:
            skill_embed.add_field(
                name="Notes", value="{}".format(self.notes), inline=False
            )
        skill_embed.set_footer(
            text="{}".format(self.school), icon_url="{}".format(self.skillbook_icon)
        )
        return skill_embed

    def generateMultiEmbed(skills):
        skill_embed = Embed(
            title="Skills Matching Search",
            description="There are a few skills matching your search. Try a more detailed search.",
            color=0xEF952C,
        )
        for skill in skills:
            skill_embed.add_field(
                name="{}".format(skill.name),
                value="{}".format(skill.description),
                inline=False,
            )
        return skill_embed
