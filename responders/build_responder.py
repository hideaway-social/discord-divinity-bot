from helpers import boot_database, clean_content
from models.build import Build

class BuildResponder():

    def __init__(self, message):
        self.original_message = message
        self.query = clean_content(self.original_message.content, "!build")

    def getReply(self):
        boot_database()
        # check if we have an exact match
        builds_collection = Build.where("string", "{}".format(self.query)).get()
        if Build.count() == 1:
            return {'content': '', 'embed': builds_collection.first().generateSingleEmbed()}
        
        # check if we have a fuzzy match
        builds_collection = Build.where("string", "like", "%{}%".format(self.query)).get()
        if builds_collection.count() == 1:
            return {'content': '', 'embed': builds_collection.first().generateSingleEmbed()}
        elif builds_collection.count() > 1:
            return {'content': '', 'embed': Build.generateMultiEmbed(builds_collection)}

        # check if there is a typo we can catch
        if(not hobj.spell(self.query)):
            builds_collection = Build.where("string", "like", "%{}%".format(self.query)).get()
            for suggestion in hobj.suggest(self.query)[:2]:
                print(suggestion)
                builds_collection.merge(Build.where("string", "like", "%{}%".format(suggestion)).get())
            builds_collection.unique()
        
        if builds_collection.count() == 0:
            return {'content': 'Couldn\'t find any skills similar to "{}".'.format(self.query)}
        elif count == 1:
            return {'content': '', 'embed': builds_collection.first().generateSingleEmbed()}
        else:
            return {'content': '', 'embed': Skill.generateMultiEmbed(builds_collection)}
