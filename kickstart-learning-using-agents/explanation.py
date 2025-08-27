from langgraph.func import task
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict, Any, List

@task
def enhance_structured_explanations(structured_pathway: Dict[str, Any], student_profile: dict) -> Dict[str, Any]:
    """
    Enhances the explanation sections of a structured pathway with detailed phase-by-phase explanations.
    Takes the structured pathway and enriches the explanation_and_kickstart_examples with comprehensive content.
    """
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                                   api_key=student_profile.get("google_api_key"))
    
    # Extract phases for reference
    phases_text = ""
    for i, phase in enumerate(structured_pathway.get("phases", []), 1):
        phases_text += f"\n## Phase {i}: {phase['title']}\n"
        phases_text += f"{phase['description']}\n"
        for j, step in enumerate(phase.get("steps", []), 1):
            phases_text += f"  {j}. {step['title']}: {step.get('content', '')}\n"
    
    enhancement_prompt = f"""
    You are an expert educator specializing in creating comprehensive, engaging explanations. 
    
    **Student Profile:**
    - Learning Style: {student_profile.get('learning_style')}
    - Hobbies/Interests: {student_profile.get('hobby')}
    - Domain: {student_profile.get('domain')}
    - Topic: {student_profile.get('progress')}

    **Current Learning Phases:**
    {phases_text}

    **Task:** Create detailed explanation sections that correspond to each phase in the learning pathway. 
    Each explanation should be comprehensive and include:

    1. **Deep Concept Analysis**: Break down complex concepts into digestible parts
    2. **Hobby-Connected Examples**: Use analogies from {student_profile.get('hobby')} to make concepts relatable
    3. **Real-World Applications**: Show practical applications in {student_profile.get('domain')}
    4. **Common Pitfalls**: Explain what learners typically struggle with and how to avoid it
    5. **Progressive Building**: Show how each concept builds on previous knowledge
    6. **Hands-On Insights**: Provide actionable understanding that goes beyond theory

    **Format Requirements:**
    - Create one explanation section for each major concept/phase
    - Each explanation should be 200-400 words
    - Use clear, engaging language that matches the student's learning style
    - Include specific examples from their hobbies throughout
    - Focus on "why" and "how" rather than just "what"
    - Make each section standalone but connected to the overall journey

    Generate 5-7 comprehensive explanation sections that will replace the current basic explanations.
    Return ONLY a JSON array of objects with "title" and "content" fields:

    [
        {{
            "title": "Concept Title",
            "content": "Detailed markdown explanation with hobby examples..."
        }},
        ...
    ]
    """

    try:
        result = model.invoke(enhancement_prompt)
        content = str(result.content) if hasattr(result, 'content') else str(result)
        
        # Try to parse the JSON response
        import json
        try:
            enhanced_explanations = json.loads(content)
            if isinstance(enhanced_explanations, list):
                # Update the structured pathway with enhanced explanations
                enhanced_pathway = structured_pathway.copy()
                enhanced_pathway["explanation_and_kickstart_examples"] = enhanced_explanations
                return enhanced_pathway
        except json.JSONDecodeError:
            # If JSON parsing fails, fall back to creating explanations manually
            pass
            
    except Exception as e:
        print(f"Enhancement failed: {e}")
    
    # Fallback: return original pathway if enhancement fails
    return structured_pathway

@task
def generate_explanation(pathway: str, student_profile: dict) -> str:
    """
    Generates a comprehensive, detailed explanation for each phase in the learning pathway.
    Provides in-depth coverage with hobby-specific examples and practical insights.
    """
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                                   api_key=student_profile.get("google_api_key"))
    
    explanation_template = f"""
    You are an expert educator and learning facilitator. Based on the adaptive learning pathway provided, 
    create a comprehensive, detailed explanation for EACH PHASE mentioned in the pathway.

    **Student Profile:**
    - Learning Style: {student_profile.get('learning_style')}
    - Hobbies/Interests: {student_profile.get('hobby')}
    - Domain: {student_profile.get('domain')}
    - Topic: {student_profile.get('progress')}

    **INSTRUCTIONS:**
    For EACH PHASE in the learning pathway, provide the following detailed structure:

    ## Phase [Number]: [Phase Title]

    ### 🎯 Phase Overview
    - What this phase covers and why it's important
    - How it builds on previous phases (if applicable)
    - What the learner will achieve by the end

    ### 📚 Core Concepts Breakdown
    Break down each concept in this phase with:
    - Clear definitions in simple language
    - Why this concept matters in real-world applications
    - Common misconceptions to avoid

    ### 🎮 Hobby-Connected Examples
    Create detailed examples using the learner's hobbies: {student_profile.get('hobby')}
    - Use analogies from their hobbies to explain complex concepts
    - Show practical connections between their interests and the learning material
    - Make the examples engaging and memorable

    ### 🛠️ Practical Implementation
    - Step-by-step approach to applying the concepts
    - Hands-on exercises or experiments they can try
    - Tools or resources needed for practice

    ### 🏆 Milestones & Success Indicators
    - How to know they've mastered this phase
    - Key deliverables or outcomes expected
    - Self-assessment questions

    ### 🔄 Real-world Applications in {student_profile.get('domain')}
    - Specific use cases in their domain of interest
    - Industry examples and case studies
    - Career relevance and opportunities

    ### 💡 Pro Tips & Advanced Insights
    - Expert-level insights for this phase
    - Common pitfalls and how to avoid them
    - Connections to advanced topics for future learning

    ### 📈 Next Phase Preparation
    - How this phase prepares for the next learning stage
    - Key skills or knowledge to reinforce before moving forward

    **CRITICAL REQUIREMENTS:**
    1. Analyze the pathway and identify ALL distinct phases/topics mentioned
    2. Provide the complete detailed structure above for EACH phase
    3. Make each explanation substantive (minimum 200 words per phase)
    4. Use engaging, conversational tone while maintaining educational depth
    5. Integrate hobby examples throughout, not just in one section
    6. Focus on practical application and real understanding, not just theory
    7. Use proper Markdown formatting with headers, bullet points, and emphasis

    **Learning Pathway to Explain:**
    {pathway}

    Now generate the comprehensive phase-by-phase explanations following the structure above for EVERY phase in the pathway.
    """

    result = model.invoke(explanation_template)
    return str(result.content) if hasattr(result, 'content') else str(result)
