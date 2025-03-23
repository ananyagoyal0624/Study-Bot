from langchain_community.chat_models import ChatOpenAI  # ✅ FIXED

class QaLlm():
    def __init__(self) -> None:
        self.llm = ChatOpenAI(
            temperature=0, 
            model_name="gpt-3.5-turbo",
            openai_api_key="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"  # Yahan API key daalni hai
        )

    def get_llm(self):
        return self.llm
