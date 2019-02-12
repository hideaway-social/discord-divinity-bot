import sqlite3
from orator import DatabaseManager, Model
import re

TAG_RE = re.compile(r'<[^>]+>')

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

def cleanhtml(text):
    return TAG_RE.sub('', str(text))