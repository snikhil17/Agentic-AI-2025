from typing import List, Optional, Literal
from pydantic import BaseModel, Field

class PathwayStep(BaseModel):
    title: str = Field(description="The title of the learning step")
    type: Literal['concept', 'example', 'project', 'resource'] = Field(description="Type of the learning step")
    content: str = Field(description="Detailed content of the step in markdown format")
    benefit: Optional[str] = Field(None, description="The specific benefit of this step for the user's domain")
    practical_focus: Optional[str] = Field(None, description="A practical action item or thought experiment")

class PathwayPhase(BaseModel):
    title: str = Field(description="Title of the learning phase")
    description: str = Field(description="Brief overview of what this phase covers")
    steps: List[PathwayStep] = Field(description="Individual learning steps within the phase")

class ExplanationSection(BaseModel):
    title: str = Field(description="The concept being explained")
    content: str = Field(description="Detailed explanation using analogies from user's hobbies")

class Milestone(BaseModel):
    year: int = Field(description="The year of the milestone")
    description: str = Field(description="Description of the milestone")

class NextStepItem(BaseModel):
    title: str = Field(description="Short title for the next step")
    description: str = Field(description="Detailed description of the suggested next step")

class NextStepsSection(BaseModel):
    title: str = Field(description="Title for the next steps section")
    steps: List[NextStepItem] = Field(description="List of actionable next steps")

class LearningPathway(BaseModel):
    """Complete structured learning pathway matching React frontend expectations"""
    title: str = Field(description="Catchy and relevant title for the learning pathway")
    introduction: str = Field(description="Brief, welcoming introduction to the learning pathway")
    phases: List[PathwayPhase] = Field(description="Main learning phases, broken down into logical sections")
    explanation_and_kickstart_examples: List[ExplanationSection] = Field(description="Detailed explanations with hobby-specific examples")
    history_and_milestones: List[Milestone] = Field(description="Key historical moments and milestones")
    next_steps: NextStepsSection = Field(description="Suggestions for what to do after completing the pathway")
    relevant_links: List[str] = Field(description="List of useful URLs for further reading")
