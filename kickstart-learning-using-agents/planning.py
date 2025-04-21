from langgraph.func import task
from langchain_google_genai import ChatGoogleGenerativeAI


@task
def generate_initial_plan(student_profile: dict, combined_text: str) -> str:
    """
    Generates an adaptive learning pathway in Markdown format based on
    the student profile and retrieved context.
    """
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                                   api_key=student_profile.get("google_api_key"))
    prompt = (
        f"Generate an adaptive learning pathway in Markdown format for a student with the following profile:\n\n"
        f"**Learning Style:** {student_profile.get('learning_style')}\n"
        f"**Learning Topic:** {student_profile.get('progress')}\n"
        f"**Interests/Domain:** {student_profile.get('domain')}\n\n"
        "Organize the content with headings (e.g., #, ##, ###), bullet points, and numbered lists. "
        "Use a friendly, concise style similar to ChatGPT. Provide relevant examples or references where needed.\n\n"
        "Use the following context to enrich the plan:\n\n" +
        combined_text +
        "Generate an adaptive learning pathway in Markdown format (do NOT use markdown code fences like ```markdown).\n"
    "Organize clearly using #, ##, ### headings, bullet points, numbered lists, bold (**text**), and italics (*text*).\n"
    "Make it easy to read, similar to ChatGPT style."
    "Make it only till 3-Phase or Heading"
    )

    
    return model.invoke(prompt).content
