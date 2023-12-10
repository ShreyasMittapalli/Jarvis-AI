import os
import openai
import pyttsx3  
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Explain the rules of cricket?",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

text_result = response["choices"][0]["text"]

print(text_result)

engine = pyttsx3.init()
engine.say(text_result)
engine.runAndWait()
