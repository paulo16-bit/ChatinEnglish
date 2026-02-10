from agent.agent import run_agent

def chat_with_agent(user_message: str) -> str:
    try:
        response = run_agent(
            chat_id="test_chat",
            user_message=user_message
        )
        return response
    except Exception as e:
        print("🔥 ERRO AO CHAMAR O AGENTE:", e)
        return (
            "⚠️ Estou um pouco sobrecarregado agora.\n"
            "Tente novamente em alguns segundos 😊"
        )
    

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        agent_response = chat_with_agent(user_input)
        print("Agent:", agent_response)