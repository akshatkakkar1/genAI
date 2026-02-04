from langchain_core.prompts import ChatPromptTemplate
#here some wierd behavior here this thing not work-->from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms,what is {topic}')
   
])

prompt = chat_template.invoke({'domain': 'AI', 'topic': 'LangChain'})
print(prompt)