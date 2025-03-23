import asyncio
from langchain_community.document_loaders import PyPDFLoader
from quizz_generator import generate_quizz
from ui_utils import transform

async def pdf_to_quizz(pdf_file_name):
    try:
        # Load PDF and split pages
        loader = PyPDFLoader(pdf_file_name)
        pages = loader.load_and_split()

        sem = asyncio.Semaphore(10)  # Limit parallel tasks

        async def process_page(page):
            async with sem:
                result = await generate_quizz(page.page_content)
                return result if result else []  # Ensure it's not None

        tasks = [process_page(page) for page in pages]
        questions = await asyncio.gather(*tasks)

        all_questions = []
        for question_set in questions:
            if question_set:  # Ensure question_set is not None
                transformed_questions = transform(question_set[0]) if question_set[0] else []
                all_questions.extend(transformed_questions)

        return all_questions

    except Exception as e:
        print(f"Error processing PDF: {e}")
        return []