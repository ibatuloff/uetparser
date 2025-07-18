from sqlalchemy.orm import mapped_column, Mapped, declared_attr, DeclarativeBase
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
import enum
import uuid
from sqlalchemy import TIMESTAMP, func
from datetime import datetime

class Status(str, enum.Enum):
    FAILED = "FAILED"
    PROCESSING = "PROCESSING"
    FINISHED = "FINISHED"
    PENDING = "PENDING"

class Base(DeclarativeBase):
    __abstract__ = True
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4())
    itemcode: Mapped[str]
    jobid: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("jobs.id"), nullable=False)
    status: Mapped[Status] = mapped_column(nullable=False, default=Status.PENDING)
    urls: Mapped[str] = mapped_column(nullable=True)
    scraped_data: Mapped[str] = mapped_column(nullable=True)
    extracted_sections: Mapped[str] = mapped_column(nullable=True)
    openai_response: Mapped[dict] = mapped_column(JSONB, nullable=True) 
    prompt: Mapped[str] = mapped_column(nullable=True) 

class Job(Base):
    __tablename__ = "jobs"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    status: Mapped[Status] = mapped_column(nullable=False, default=Status.PENDING)
    filename: Mapped[str]
    input_file_json: Mapped[dict] = mapped_column(JSONB)
    output_file_json: Mapped[dict | None] = mapped_column(JSONB, nullable=True)


    