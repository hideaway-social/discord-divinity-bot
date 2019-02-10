import sqlite3
from orator import DatabaseManager, Model


def boot_database():
    config = {
        "default": "sqlite",
        "sqlite": {
            "driver": "sqlite",
            "database": "divinity.db",
            "prefix": "",
            "log_queries": True,
        },
    }

    db = DatabaseManager(config)
    Model.set_connection_resolver(db)
