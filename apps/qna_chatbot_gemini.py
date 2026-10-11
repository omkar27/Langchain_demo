import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

#llm = ChatGoogleGenerativeAI(model="gemini-3.7-flash")
#res = llm.invoke("Hello, how are you?")
#print(res.content)
st.title("QnA Chatbot with Gemini")
st.markdown("This is a simple QnA chatbot using Gemini model from Google Generative AI.")
if "messages" not in st.session_state:
    st.session_state.messages = []
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

query = st.chat_input("Ask me anything:")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    llm = ChatGoogleGenerativeAI(model="gemini-3.7-flash")
    response = llm.invoke(query)
    st.chat_message("assistant").markdown(response.content[0]['text'])
    st.session_state.messages.append({"role": "assistant", "content": response.content[0]['text']})
    # with st.chat_message("assistant"):
    #     st.markdown(response.content)
