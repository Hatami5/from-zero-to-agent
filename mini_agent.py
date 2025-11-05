# agent.py
import datetime

memory = []

def get_time():
    return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

def calculate(expression):
    try:
        result = eval(expression)
        return f"The result is {result}"
    except:
        return "Sorry, I couldn’t calculate that."

def plan_task(user_input):
    if "meeting" in user_input.lower():
        return ["check calendar", "set reminder", "send confirmation"]
    elif "study" in user_input.lower():
        return ["open notes", "summarize topics", "plan schedule"]
    else:
        return ["analyze request", "take best action"]

def think(user_input):
    memory.append(user_input)
    
    if "history" in user_input.lower():
        return f"Past inputs: {memory[:-1]}"
    elif "time" in user_input.lower():
        return get_time()
    elif "calculate" in user_input.lower():
        expression = user_input.lower().replace("calculate", "").strip()
        return calculate(expression)
    else:
        steps = plan_task(user_input)
        return f"🧩 Plan for your task: {steps}"

def agent_loop():
    print("🤖 Intelligent Agent Ready! Type 'exit' to quit.")
    while True:
        user = input("You: ")
        if user.lower() == "exit":
            print("Agent: Goodbye 👋")
            break
        print("Agent:", think(user))

if __name__ == "__main__":
    agent_loop()
