# INERACT With VECTORDB

import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

import openai
import os
from dotenv import load_dotenv
load_dotenv()

def get_collection():
    try:
        client = chromadb.Client(Settings(chroma_api_impl="rest",
                                            chroma_server_host="localhost",
                                            chroma_server_http_port="8000"
                                        ))
        openai_embedder = embedding_functions.OpenAIEmbeddingFunction(
            api_key=os.getenv("OPENAI_API_KEY"), # Replace with your own OpenAI API key
            model_name="text-embedding-ada-002"
        ) 
        # client.delete_collection("programmgergpt")
        collection = client.get_or_create_collection(name="programmgergpt", embedding_function=openai_embedder)
        return collection 
    except Exception as e:
        return None


def store(collection, code, description):
    try:
        if(collection is None):
            raise Exception("Chroma collection not found.")
        collection_length = collection.count()
        collection.add(
            ids=[f"{collection_length+1}"],
            documents = [description],
            metadatas = [{"code": code}],
            embeddings = None
        )
        return
    except Exception as e: 
        return  

def retrieve(collection, task):
    try:
        if(collection is None):
            raise Exception("Chroma collection not found.")
        result = collection.query(
            query_texts = [task],
            n_results = 1,
            include = ["metadatas", "distances"]
        )
        max_distance = 0.25
        if(result["distances"][0][0]<max_distance):
            return result["metadatas"][0][0]["code"]
        return None
    except: 
        return None 