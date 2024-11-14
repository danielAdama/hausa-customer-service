from flask import Flask, request, jsonify
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from flask_cors import CORS
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")
system_message = """
"You are an AI customer support agent fluent in Hausa. 
You will receive messages in Hausa and respond in a natural, conversational tone also in Hausa. 
Your goal is to be polite, helpful, and responsive to each inquiry, answering questions clearly and ensuring the customer feels satisfied with your responses. 
If any information is unclear, ask clarifying questions in Hausa to fully understand the customer's needs. Always maintain a friendly and professional tone. 
Please keep your responses short.
"""

app = Flask(__name__)
CORS(app)

@app.post('/api/assistant/')
def assistant():
    data = request.json
    message = data.get('message')

    llm = ChatGroq(
        model="llama3-70b-8192",
        temperature=0
    )
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            ("human", human)
        ]
    )
    translator = prompt | llm

    if message:
        response = translator.invoke({"text": message}).content
    else:
        response = "No message provided."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)