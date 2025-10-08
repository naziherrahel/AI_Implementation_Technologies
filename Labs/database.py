# Import the Database class from the 'databases' library for async database operations.
# This allows us to interact with PostgreSQL asynchronously, which is efficient for web apps.
from databases import Database
# Import sqlalchemy for defining and creating database tables.
# SQLAlchemy is a powerful ORM and query builder for Python.
import sqlalchemy
# Import metadata from models.py, which contains the table definitions for our database.
from models import metadata

# Define the database connection URL for PostgreSQL.
# We're using the asyncpg driver for async operations, connecting to a local database named 'dust_detection'.
# Replace 'postgres:admin@localhost' with your actual credentials if needed.
DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost/dust_detection"

# Create a Database instance for async operations.
# This object will handle connections and queries to the PostgreSQL database.
database = Database(DATABASE_URL)

# SQLAlchemy’s create_all() method is synchronous
# Create a synchronous SQLAlchemy engine for creating tables.
# We replace '+asyncpg' with an empty string to use the standard PostgreSQL driver (psycopg2) for table creation.
engine = sqlalchemy.create_engine(DATABASE_URL.replace("+asyncpg", ""))

# Create all tables defined in the metadata object (from models.py).
# This runs when the script is imported, ensuring the 'new_detections' table exists before the API starts.
metadata.create_all(engine)