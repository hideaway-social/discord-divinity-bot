from helpers import boot_database, clean_content
from models.skill import Skill

class SkillResponder():

    def __init__(self, message):
        self.original_message = message
        self.query = clean_content(self.original_message.content, "!skill")

    def getReply(self):
        boot_database()
        # check if we have an exact match
        skills_collection = Skill.where("string", "{}".format(self.query)).get()
        if skills_collection.count() == 1:
            return {'content': '', 'embed': skills_collection.first().generateSingleEmbed()}
        
        # check if we have a fuzzy match
        skills_collection = Skill.where("string", "like", "%{}%".format(self.query)).get()
        if skills_collection.count() == 1:
            return {'content': '', 'embed': skills_collection.first().generateSingleEmbed()}
        elif skills_collection.count() > 1:
            return {'content': '', 'embed': Skill.generateMultiEmbed(skills_collection)}

        # check if there is a typo we can catch
        if(not hobj.spell(self.query)):
            skills_collection = Skill.where("string", "like", "%{}%".format(self.query)).get()
            for suggestion in hobj.suggest(self.query)[:2]:
                print(suggestion)
                skills_collection.merge(Skill.where("string", "like", "%{}%".format(suggestion)).get())
            skills_collection.unique()
        
        if skills_collection.count() == 0:
            return {'content': 'Couldn\'t find any skills similar to "{}".'.format(self.query)}
        elif count == 1:
            return {'content': '', 'embed': skills_collection.first().generateSingleEmbed()}
        else:
            return {'content': '', 'embed': Skill.generateMultiEmbed(skills_collection)}
