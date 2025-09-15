from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def get_chat_response(prompt, memory, openai_api_key, openai_api_base):
    model = ChatOpenAI(model='gpt-4-turbo',
                       openai_api_key=openai_api_key,
                       openai_api_base=openai_api_base)
    chain = ConversationChain(llm=model, memory=memory)
    response = chain.invoke({'input': prompt})
    return response['response']

memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response('牛顿提出了哪些定律', memory,
#                   'sk-vuC9H0TWcNIJ0Jokz4cUyWDn6xocPsDDEZtZ72LA25ep6ZqI',
#                   "https://api.aigc369.com/v1"))
# print(get_chat_response('上一个问题是什么', memory,
#                   'sk-vuC9H0TWcNIJ0Jokz4cUyWDn6xocPsDDEZtZ72LA25ep6ZqI',
#                   "https://api.aigc369.com/v1"))