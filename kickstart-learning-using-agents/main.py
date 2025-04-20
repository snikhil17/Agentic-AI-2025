from agent import adaptive_learning_agent

if __name__ == "__main__":
    print("Welcome to the Adaptive Learning Agent!")
    print("Please provide the following information to generate a personalized learning pathway.\n")
    
    # Explanation for each input:
    # 1. Learning Style: Describe how you prefer to learn (e.g., "intuitive and real-world examples").
    # 2. Learning Topic (Progress): What subject or topic are you currently working on? (e.g., "Angentic AI using Langgraph").
    # 3. Hobby: Mention any hobbies that might help tailor examples (e.g., "Cricket, watching Friends on Netflix, taking care of my new-born daughter").
    # 4. Domain: The field or domain of interest (e.g., "health care").

    learning_style = input("Enter your preferred learning style (e.g., 'intuitive and real-world examples'): ")
    progress = input("Enter your learning topic or subject (e.g., 'Angentic AI using Langgraph'): ")
    hobby = input("Enter your hobbies (e.g., 'Cricket, watching Friends on Netflix, taking care of my new-born daughter'): ")
    domain = input("Enter your domain or field of interest (e.g., 'health care'): ")

    student_profile = {
        "learning_style": learning_style,
        "progress": progress,
        "hobby": hobby,
        "domain": domain
    }
    
    # Call the adaptive learning agent with the provided student profile.
    result = adaptive_learning_agent.invoke(student_profile)
    
    print("\n### Final Output:")
    print("Relevant Links:")
    for link in result["relevant_links"]:
        print(link)
    
    print("\nExplanation and Kickstart Examples:")
    print(result["explanation"])
