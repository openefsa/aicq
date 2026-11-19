from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from sqlalchemy import Identity, String, BigInteger, BIGINT,Column
from aicq.model import StructuredOutputSchema,PromptTemplate

class Prompt(SQLModel,table=True):
    __tablename__ = "prompts"
    id: int | None = Field(
        default=None,
        sa_column=Column(BigInteger, Identity(), primary_key=True),
    )
    output_schema: str
    prompt_template: str
    



    
    