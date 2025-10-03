from pydantic import BaseModel

class ResumeRequest(BaseModel):
    text: str

class SkillsResponse(BaseModel):
    skills: list[str]