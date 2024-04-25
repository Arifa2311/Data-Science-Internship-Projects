import streamlit as st
import chromadb
from chromadb.utils import embedding_functions

# initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="my_chromadb")

# distilbert-base-nli-mean-tokens model for embedding function
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="distilbert-base-nli-mean-tokens")

# get or create the collection
collection = chroma_client.get_or_create_collection(name="my_collection", embedding_function=sentence_transformer_ef, metadata={"hnsw:space": "cosine"})

def main():
    st.title("A.I SEARCH ENGINE🤖🔍")

    # getting the user input
    user_query = st.text_input("Hey there, pal! 🎥 Drop your query and I'll scout some flicks for you: 🍿")

    if st.button("Search"):
        if user_query:
            # query the collection
            results = collection.query(
                query_texts=[user_query],
                n_results=10,
                include=['documents', 'distances', 'metadatas']
            )

            # display user input
            st.write(f"Your search query: {user_query}")

            # display output documents
            st.write("Search Results:")
            for i, document in enumerate(results['documents'][0], 1):
                st.write(f"{i}. {document}")

if __name__ == "__main__":
    main()
