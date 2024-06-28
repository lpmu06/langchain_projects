from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
openai_model=ChatOpenAI()
# ollama llama3
ollama_model=Ollama(model="llama3")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 50 words")

add_routes(
    app,
    prompt1|openai_model,
    path="/essay"
)

add_routes(
    app,
    prompt2|ollama_model,
    path="/poem"
)

if __name__=='__main__':
    uvicorn.run(app,host="localhost",port=8000)