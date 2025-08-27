from langgraph.func import task
from langchain_google_genai import ChatGoogleGenerativeAI
from data_models import LearningPathway
from typing import Dict, Any
import json

@task  
def generate_structured_pathway(student_profile: dict, combined_text: str) -> Dict[str, Any]:
    """
    Generates a complete structured learning pathway matching React frontend expectations
    """
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=student_profile.get("google_api_key")
    )
    
    # Use structured output with Pydantic model
    structured_model = model.with_structured_output(LearningPathway)
    
    prompt = f"""
    Create a personalized, adaptive learning pathway for a user with the following preferences:
    - Preferred Learning Style: {student_profile.get('learning_style')}
    - Learning Topic/Subject: {student_profile.get('progress')}
    - Hobbies: {student_profile.get('hobby')}
    - Domain/Field of Interest: {student_profile.get('domain')}

    Your goal is to act as an "Agentic AI Learning Assistant". Curate the best resources, design a comprehensive personalized "Adaptive Learning Pathway", and explain each step clearly.

    Use the following extensive context to enrich the plan with diverse perspectives and comprehensive coverage:
    {combined_text}

    The pathway should include:
    1. **Engaging History & Milestones:** A comprehensive history of the topic with 5-7 key milestones.
    2. **Customized Examples:** Rich examples customized around the user's hobbies throughout all explanation sections.
    3. **Real-world Projects:** Multiple real-world project ideas and use-cases relevant to their domain.
    4. **Handpicked Links:** A curated list of reference links for deeper dives.
    5. **Progressive Learning:** Each phase should build upon the previous one, creating a logical learning progression.
    6. **Comprehensive Coverage:** Utilize the extensive retrieved information to cover the topic from multiple angles.

    Structure the response with:
    - A catchy title and welcoming introduction
    - At least 7 comprehensive learning phases, each with 3-4 detailed steps
    - 5-6 explanation sections with hobby-specific analogies
    - 5-7 historical milestones
    - A next steps section with 4-5 actionable recommendations
    - A list of relevant links from the retrieved context

    Generate a comprehensive, well-structured learning plan. The tone should be encouraging, clear, and highly personalized.
    Use markdown formatting in content fields for better readability.
    """
    
    # Get structured response
    structured_response = structured_model.invoke(prompt)
    
    # Convert to dict if it's a Pydantic model, otherwise return as dict
    if isinstance(structured_response, LearningPathway):
        return structured_response.model_dump()
    else:
        # If it's already a dict, return as is
        return dict(structured_response)
