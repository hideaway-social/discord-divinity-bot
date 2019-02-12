from orator.migrations import Migration


class CreateSchoolsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('schools') as table:
            table.increments('id')
            table.string('name')
            table.string('string')
            table.string('description')
            table.string('primary_stat')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('schools')
