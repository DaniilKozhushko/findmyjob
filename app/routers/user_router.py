from fastapi import APIRouter
from app.models import *
from utils.utils import extract_skills

router = APIRouter(
    prefix="/resume",
    tags=["Resume 📄"]
)

@router.post("/extract_skills", response_model=SkillsResponse)
async def extract_resume_skills(request: ResumeRequest):
    skills = extract_skills(request.text)
    return SkillsResponse(skills=skills)