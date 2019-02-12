from orator.migrations import Migration


class CreateBuildsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("builds") as table:
            table.increments("id")
            table.string("name")
            table.string("string")
            table.string("description")
            table.string("url")
            table.string("image")
            table.timestamps()

        with self.schema.create("build_schools") as table:
            table.integer("build_id").unsigned()
            table.integer("school_id").unsigned()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("build_schools")
        self.schema.drop("builds")
