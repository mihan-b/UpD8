import os
import openai
import random

def generate_response(text):
  tones = ["casual tone", "conversational tone", "professional tone", ]
  tone = random.choice(tones)
  prompt = "Reformat, " + tone + ":\n" + text
  openai.api_key = os.environ['openai_key']
  response = openai.Completion.create(engine="text-davinci-003", prompt=prompt,max_tokens=1000)
  print
  return response["choices"][0]["text"]
