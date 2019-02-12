from orator import Model
from orator.orm import belongs_to_many
from .school import School
from discord import Embed

class Build(Model):

    CONFIG = {"color": 0xEF952C}

    @belongs_to_many("build_schools")
    def schools(self):
        return School

    def generateSingleEmbed(self):
        build_embed = Embed(
            title="Build - {}".format(self.name),
            description="{}".format(self.description),
            url="{}".format(self.url),
            color=self.CONFIG.get("color"),
        )
        build_embed.set_image(url="{}".format(self.image))
        schools_string = ""
        for school in self.schools:
            schools_string += "{}, ".format(school.name)
        if schools_string != "":
            build_embed.add_field(
                name="Schools", value="{}".format(schools_string[:-2]), inline=False
            )
        return build_embed

    def generateMultiEmbed(builds):
        build_embed = Embed(
            title="Builds Matching Search",
            description="There are a few builds matching your search. Try a more detailed search.",
            color=0xEF952C,
        )
        schools_string = ""
        for build in builds:
            build_embed.add_field(
                name="{}".format(build.name), value="{}".format(build.description[:220] + "..."), inline=False
            )
        return build_embed
