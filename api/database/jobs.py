from database.db import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import PrimaryKeyConstraint
import uuid
import enum

class JobStatus(str, enum.Enum):
    ISSUED = "ISSUED"
    FINISHED = "FINISHED"

class JobsData(Base):
    __tablename__ = "jobsdata"
    
    id: Mapped[uuid.UUID]
    itemcode: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    data: Mapped[str] 

    __table_args__ = (
        PrimaryKeyConstraint("id", "itemcode", "url"),
    )


class Jobs(Base):
    __tablename__ = "jobs"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    data: Mapped[str] 
    status: Mapped[JobStatus] = mapped_column(nullable=False)
