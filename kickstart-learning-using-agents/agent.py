from langgraph.func import entrypoint
from retrieval import perform_retrieval
from structured_agent import generate_structured_pathway

@entrypoint()
def adaptive_learning_agent(student_profile: dict) -> dict:
    """
    Main entrypoint for the adaptive learning pathway generation agent.
    Returns complete structured learning pathway matching React frontend expectations.
    """
    # 1. Retrieve context
    retrieval_result = perform_retrieval(student_profile).result()
    combined_text = retrieval_result["combined_text"]
    relevant_links = retrieval_result["relevant_links"]
    
    # 2. Generate complete structured learning pathway
    structured_pathway = generate_structured_pathway(student_profile, combined_text).result()
    
    # 3. Add retrieved links to the structured pathway
    structured_pathway["relevant_links"] = relevant_links
    
    # 4. Return the complete structured response
    return structured_pathway
