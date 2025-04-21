from langgraph.func import task

from langchain_google_genai import ChatGoogleGenerativeAI

@task
def generate_explanation(pathway: str, student_profile: dict) -> str:
    """
    Generates a detailed explanation and kickstart examples in Markdown format.
    """
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                                   api_key=student_profile.get("google_api_key"))
    explanation_template = (
        "Based on the following adaptive learning pathway, generate an extensive yet concise explanation for each topic. "
        "Follow this structure for each topic:\n"
        "1. History: Explain why and when the topic came into picture.\n"
        "2. Milestone Events: List some important milestone events over time.\n"
        "3. Interesting Facts: Provide some interesting and wow facts about the topic.\n"
        f"4. Explanation with Examples: Give a fresh explanation of the topic using examples that incorporate the student's hobbies: {student_profile.get('hobby')}.\n"
        "5. Finally, provide some basic to intermediate case-studies/projects that can be implemented or practiced by the user.\n"
        "Do not repeat what is already explained in the adaptive learning pathway; provide a new perspective.\n\n"
        f"**Adaptive Learning Pathway (Reference)**:\n{pathway}\n\n"
         "Generate an adaptive learning pathway in plain markdown format (WITHOUT markdown code fences). "
    "Organize clearly using #, ##, bullet points, and lists."
    "Make it only till 3 topics."
    )

    
    return model.invoke(explanation_template).content
