from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import os

DATA_DIR = "./everything_cli/data"


def build_index():
  """Loads documents from a directory and builds an index.""" 
  print("\n[INFO] Loading documents and building index...") 

  if not os.path.exists(DATA_DIR):
    print(f"[WARNING] {DATA_DIR} does not exist. Creating it now...")
    os.makedirs(DATA_DIR)

    # ensure directory has documents
  if not os.listdir(DATA_DIR):
    print("[ERROR] No documents found in the data directory. Please upload files before indexing.")
    return None
    

  documents = SimpleDirectoryReader(DATA_DIR).load_data()
  
  vectorIndex = VectorStoreIndex.from_documents(documents)

  query_engine = vectorIndex.as_query_engine()

  query_question = input("Enter your prompt for retrieval: ").strip()

  response = query_engine.query(
    query_question
  )
  print(response)
  
