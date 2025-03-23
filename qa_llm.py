from langchain_community.chat_models import ChatOpenAI  # ✅ FIXED

class QaLlm():
    def __init__(self) -> None:
        self.llm = ChatOpenAI(
            temperature=0, 
            model_name="gpt-3.5-turbo",
            openai_api_key=""  # Yahan API key daalni hai
        )

    def get_llm(self):
        return self.llm
