from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from prompt import create_prompt

load_dotenv()

def split_text(text: str) -> list:
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=4000, #4000 characters
        chunk_overlap=200, #overlap of 200 characters
    )
   
    text_arr = text_splitter.split_text(text)
    return text_arr

def summarize_text(text: str) -> str:
    # Initialize the OpenAI LLM with the API key
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # Split the text into smaller chunks
    text_arr = split_text(text)
    summaries = []
    for chunk in text_arr:
        summary = llm.invoke(create_prompt(chunk))
        summaries.append(summary.content)
    return " ".join(summaries)
   
