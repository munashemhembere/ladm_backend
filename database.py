from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Your actual database credentials
DATABASE_URL = "postgresql://postgres:fall20back01@localhost:5432/ladm_uz"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Session factory for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
