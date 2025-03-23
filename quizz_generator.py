from qcm_chain import QCMGenerateChain
from qa_llm import QaLlm
import asyncio

async def llm_call(qa_chain: QCMGenerateChain, text: str):
    
    print(f"llm call running...")
    batch_examples = await asyncio.gather(qa_chain.aapply_and_parse(text))
    print(f"llm call done.")

    return batch_examples

async def generate_quizz(content: str):
    """
    Generates a quiz from the given content.
    """
    print("✅ Debug: Calling QaLlm()...")  
    qa_llm = QaLlm()  

    llm_instance = qa_llm.get_llm()  
    print(f"✅ Debug: LLM Instance: {llm_instance}")  # Check if LLM is created

    if llm_instance is None:
        raise ValueError("❌ LLM instance is None. Check API key or initialization!")

    qa_chain = QCMGenerateChain.from_llm(llm_instance)
    print(f"✅ Debug: QA Chain Created: {qa_chain}")  

    return await llm_call(qa_chain, [{"doc": content}])

    