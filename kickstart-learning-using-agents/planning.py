from langgraph.func import task
from model_provider import model

@task
def generate_initial_plan(student_profile: dict, combined_text: str) -> str:
    """
    Generates an adaptive learning pathway in Markdown format based on
    the student profile and retrieved context.
    """
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
    )

    response = model.invoke(prompt)
    return response.content
