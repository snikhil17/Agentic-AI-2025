from langgraph.func import entrypoint
from retrieval import perform_retrieval
from planning import generate_initial_plan
from explanation import generate_explanation

@entrypoint()
def adaptive_learning_agent(student_profile: dict) -> dict:
    """
    Main entrypoint for the adaptive learning pathway generation agent.
    Returns:
      - initial_plan: The adaptive learning pathway in Markdown.
      - explanation: Detailed explanation in Markdown.
      - relevant_links: List of source links from retrieval.
    """
    # 1. Retrieve context
    retrieval_result = perform_retrieval(student_profile).result()
    combined_text = retrieval_result["combined_text"]
    relevant_links = retrieval_result["relevant_links"]
    
    # 2. Generate initial adaptive learning pathway (Markdown)
    initial_plan = generate_initial_plan(student_profile, combined_text).result()
    
    # 3. Generate detailed explanation (Markdown)
    explanation = generate_explanation(initial_plan, student_profile).result()
    
    # 4. Return everything needed for the UI
    return {
        "initial_plan": initial_plan,
        "explanation": explanation,
        "relevant_links": relevant_links
    }
