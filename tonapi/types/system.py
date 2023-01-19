from pydantic import BaseModel


class Time(BaseModel):
    time: int
