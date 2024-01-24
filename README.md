# Chatbot_using_LangChain
The development of the Web Research Bot centers around creating a chatbot that can effectively respond to user queries related to a specified website, using the given website link:

URL: https://chettinadvidyashram.org/

Within the main.py file, Langchain is employed to retrieve content from the designated URL. The implementation utilizes methods such as UnstructuredURLLoader and RecursiveCharacterTextSplitter to process and segment the text into manageable chunks. GooglePalmEmbeddings is then applied to convert the text into vectors, and these vectors are stored in a FAISS vector store. The resulting vectors are saved in a local file for subsequent analysis.

In the app.py file, a Streamlit-based chatbot interface is hosted, utilizing Google Palm as a Large Language Model (LLM). The chatbot leverages the Langchain RetrievalQA method to retrieve answers from the vector database generated in the main.py file. End-users are prompted to input queries related to the provided website, and the chatbot responds with relevant information based on the Langchain vector database.

This project evaluates the implementation of a functional chatbot, examining the proper integration of Langchain and Google Palm technologies. A user-friendly interface is presented, and a screenshot showcasing the chatbot in action is attached
