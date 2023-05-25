import openai
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings


def load_faiss_index(path):
    """
    Loads a FAISS index from a local file.

    Parameters:
        path (str): The path to the file containing the FAISS index.

    Returns:
        faiss_index: The loaded FAISS index.
    """
    faiss_index = FAISS.load_local(path, OpenAIEmbeddings())
    return faiss_index


def search_in_index(faiss_index, question):
    """
    Searches for relevant text in a FAISS index based on a given question.

    Parameters:
        faiss_index: The FAISS index to search in.
        question (str): The question or query to search for.

    Returns:
        str: The concatenated text content from the relevant pages in the index.
    """
    docs = faiss_index.similarity_search(question, k=2)
    results = ""
    for doc in docs:
        results += doc.page_content
    return results


# Using gpt-3.5-turbo model for search

# def generate_exact_answer(result, question):
#     """
#     Generates an exact answer to a given question based on the provided text.

#     Parameters:
#         result (str): The text containing relevant information to generate the answer from.
#         question (str): The question to generate an answer for.

#     Returns:
#         str: The generated exact answer to the question.
#     """
#     prompt = """You are an AI assistant in a conversation with a human. \n Answer their questions as truthfully as possible using the provided text. If the answer is not contained within the text, say "I haven't that knowledge.". """ + \
#         result + "\n\n Q:" + question + "\n"
#     answer = openai.Completion.create(
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=300,
#         model="text-davinci-003",
#         top_p=1,
#     )["choices"][0]["text"].strip(" \n")
#     return answer


def generate_exact_answer(result, question):
    """
    Generates an exact answer to a given question based on the provided text.

    Parameters:
        result (str): The text containing relevant information to generate the answer from.
        question (str): The question to generate an answer for.

    Returns:
        str: The generated exact answer to the question.
    """
    prompt = """You are an AI assistant in a conversation with a human. \n Answer their questions as truthfully as possible using the provided text. If the answer is not contained within the text, say "I haven't that knowledge.". """ + \
        result
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": question},
        ]
    )

    return completion.choices[0].message.content


def ask_question(question):
    """
    Asks a question and generates an exact answer using the loaded FAISS index.

    Parameters:
        question (str): The question to be asked.

    Returns:
        str: The generated exact answer to the question.
    """
    faiss_index = load_faiss_index("index")
    result = search_in_index(faiss_index, question)
    answer = generate_exact_answer(result, question)
    return {
        "answer": answer,
        "status": 200,
    }
