import ollama
from backend.automation import handle_command
from backend.translator import to_english
#role=system set rules and personality
#role=user your question
#content=user input
def get_response(text):
    text=to_english(text)
    automation_reply = handle_command(text)
    if automation_reply:
        return automation_reply


    response = ollama.chat(
        model="prakashFast",
        messages=[{"role": "user", "content": text}]
    )
    return response["message"]["content"]
