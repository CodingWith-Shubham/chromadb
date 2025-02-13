import chromadb
from fastapi import FastAPI

app = FastAPI()
chroma_client = chromadb.PersistentClient(path="./chroma_db")  

# Load all collections
collections = {
    "beginner": chroma_client.get_collection("coursera_beginner"),
    "intermediate": chroma_client.get_collection("coursera_intermediate"),
    "advanced": chroma_client.get_collection("coursera_advanced")
}

@app.get("/recommend/{level}")
def recommend_courses(level: str, query: str):
    if level not in collections:
        return {"error": "Invalid level. Choose beginner, intermediate, or advanced."}
    
    collection = collections[level]

    results = collection.query(
        query_texts=[query],
        n_results=5
    )
    
    return {"recommendations": results["documents"][0]}

# import chromadb

# chroma_client = chromadb.PersistentClient(path="./")  
# collections = chroma_client.list_collections()

# print("Available Collections:")
# for collection in collections:
#     print(collection)  # Just print collection (it already contains the name)
# to start the server use : python -m uvicorn server:app --host 127.0.0.1 --port 8000 --reload