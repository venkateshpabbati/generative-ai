import streamlit as st
import os  # Import the os module
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Directly set the OpenAI API key here
openai_api_key = "OPEN_API_KEY"

# Set OpenAI API key for langchain
os.environ["OPENAI_API_KEY"] = openai_api_key

st.title('RAG App: Talk to Your Documents')

# File uploader for text files
uploaded_file = st.file_uploader("Upload a text file", type="txt")

if uploaded_file is not None:
    # Read the content of the uploaded file
    file_contents = uploaded_file.read().decode("utf-8")
    
    st.write("Uploaded Document:")
    st.write(file_contents)

    # Load the document content into LangChain
    # Here we create a list of documents instead of trying to access attributes
    documents = [file_contents]

    # Create embeddings and vector store
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(documents, embeddings)

    # Set up the RetrievalQA chain
    llm = OpenAI()
    retrieval_qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())

    # User input for querying the document
    user_query = st.text_input("Ask a question about the document:")

    if st.button("Get Answer"):
        if user_query:
            # Get the answer from the model
            answer = retrieval_qa.run(user_query)
            st.write("Answer:")
            st.write(answer)
        else:
            st.error("Please enter a question.")