from dotenv import load_dotenv
import os
from langgraph.func import task
from langchain.retrievers.tavily_search_api import TavilySearchAPIRetriever

# Load environment variables
load_dotenv()

# Retrieve the Tavily API key from the environment
tavily_api_key = os.getenv("TAVILY_API_KEY")


@task
def perform_retrieval(student_profile: dict) -> dict:
    """
    Uses TavilySearchAPIRetriever to search for documents based on a combined query that includes:
      - Learning Topic (from 'progress')
      - Domain
      - Learning Style
    Returns a dictionary with 'combined_text' (concatenated text from the retrieved documents)
    and 'relevant_links' (a list of source URLs).
    """
    queries = {
        "Learning Topic": student_profile.get("progress"),
        "domain": student_profile.get("domain") + f" with respect to {student_profile.get('progress')}",
        "learning_style": student_profile.get("learning_style") + f" with respect to {student_profile.get('progress')}"
    }
    
    retriever = TavilySearchAPIRetriever(k=5)
    all_docs = []
    all_links = []
    
    for field, query in queries.items():
        print(f"Performing retrieval for {field}: {query}")
        retrieved_docs = retriever.invoke(query)
        all_docs.extend(retrieved_docs)
        field_links = [doc.metadata.get("source") for doc in retrieved_docs if doc.metadata.get("source")]
        all_links.extend(field_links)
    
    # Remove duplicate links
    all_links = list(set(all_links))
    
    # Combine text from all retrieved documents.
    document_texts = [doc.page_content for doc in all_docs]
    combined_text = "\n\n".join(document_texts)

    print("Relevant Links: \n\n ", all_links)
    print("Document Text: \n\n ", document_texts)
    print("\n" + "=" * 50 + "\n")
    
    return {"combined_text": combined_text, "relevant_links": all_links}
