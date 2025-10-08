
from databases import Database

import sqlalchemy
# Import metadata from models.py, which contains the table definitions for our database.
from models import metadata


DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost/dust_detection"


database = Database(DATABASE_URL)


engine = sqlalchemy.create_engine(DATABASE_URL.replace("+asyncpg", ""))

metadata.create_all(engine)