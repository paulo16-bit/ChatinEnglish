# agent/agent.py
from app.agent.memory import get_memory, save_message
from app.service.llm import call_llm
from app.agent.prompt import SYSTEM_PROMPT

def run_agent(chat_id, user_message):
    try:
        history = get_memory(chat_id)

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            *history,
            {"role": "user", "content": user_message},
        ]

        response = call_llm(messages)

        save_message(chat_id, "user", user_message)
        save_message(chat_id, "assistant", response)

        return response
    
    except Exception as e:
        print("⚠️ LLM ERROR:", e)

        return (
            "⚠️ I'm having a short break right now 😅\n"
            "Let's continue practicing English in a moment!\n\n"
            "Try sending a simple sentence like:\n"
            "👉 *I like studying English* 🇺🇸"
        )