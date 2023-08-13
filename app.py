from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

# Load env variables
load_dotenv()

llm = ChatOpenAI(temperature=0, tags=["tag-source-app-py"])
print(llm.predict("Why do we finish a setup with hello, world!"))
