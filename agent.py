from langgraph.func import entrypoint
from retrieval import perform_retrieval
from structured_agent import generate_structured_pathway
from explanation import enhance_structured_explanations

@entrypoint()
def adaptive_learning_agent(student_profile: dict) -> dict:
    """
    Main entrypoint for the adaptive learning pathway generation agent.
    Uses enhanced structured approach with detailed phase-by-phase explanations.
    """
    # 1. Retrieve context
    retrieval_result = perform_retrieval(student_profile).result()
    combined_text = retrieval_result["combined_text"]
    relevant_links = retrieval_result["relevant_links"]
    
    # 2. Generate structured learning pathway
    structured_pathway = generate_structured_pathway(student_profile, combined_text).result()
    
    # 3. Enhance explanations with detailed phase-by-phase content
    enhanced_pathway = enhance_structured_explanations(structured_pathway, student_profile).result()
    
    # 4. Add retrieved links to the enhanced pathway
    enhanced_pathway["relevant_links"] = relevant_links
    
    # 5. Return the enhanced structured response
    return enhanced_pathway
