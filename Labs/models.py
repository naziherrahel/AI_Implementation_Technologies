
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, MetaData

metadata = MetaData()


new_detections = Table(
    "new_detections",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("filename", String, nullable=False),

    Column("bbox", sqlalchemy.JSON, nullable=False),
    
    Column("confidence", Float, nullable=False),
    
    Column("timestamp", DateTime(timezone=True), nullable=False)
)

