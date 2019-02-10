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
            table.string("skillbook_icon")
            table.string("effects").nullable()
            table.string("armor_check").nullable()
            table.string("points")
            table.string("cooldown")
            table.string("spell_book")
            table.string("spell_scroll").nullable()
            table.string("notes")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("skills")
