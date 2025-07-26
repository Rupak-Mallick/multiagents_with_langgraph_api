from langgraph.prebuilt import create_react_agent

def add(a: float, b: float):
    """Add two numbers."""
    return a + b

def subtract(a: float, b: float):
    """Subtract second number from first number."""
    return a - b

def multiply(a: float, b: float):
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float):
    """Divide first number by second number."""
    return a / b


def get_math_agent(llm):
    prompt = (
        "You are a math agent.\n\n"
        "INSTRUCTION:\n"
        "-Assist ONLY with math-related tasks.\n"
        "-After you're done with your tasks, respond to the supervisor directly.\n"
        "-Respond only with the results of your work, do NOT include ANY other text."
    )

    return create_react_agent(
        model=llm,
        tools=[add, subtract, multiply, divide],
        prompt=prompt,
        name="math_agent"
    )