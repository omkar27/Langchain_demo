from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm_openai = ChatOpenAI(model="gpt-4o")
# prompt = [{"role":"system","content":"Act as senior js developer"},
#           {"role":"user","content":"What is difference b/w map and filter?"}]
history = []
while True:
    user_input = input("Enter your query (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    history.append({"role": "user", "content": user_input})
    response = llm_openai.invoke(history)
    history.append({"role": "assistant", "content": response.content})
    print(response.content)