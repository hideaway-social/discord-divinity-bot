from orator.migrations import Migration


class CreateSkillsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("skills") as table:
            table.increments("id")
            table.string("name")
            table.string("school")
            table.string("string")
            table.string("description")
            table.string("url")
            table.string("thumbnail")
            table.string("icon")
            table.string("effects")
            table.string("armor_check")
            table.string("notes")
            table.string("spell_book_locations")
            table.string("scroll_crafting")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("skills")
