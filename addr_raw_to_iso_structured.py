import os
import msg_builder as msgb
from openai import OpenAI
from pprint import pprint 


api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No API key found.")


client = OpenAI(api_key=api_key)
msgs_all = []

system_prompt = msgb.system_prompt()
system_msg = msgb.msg_from_prompt(system_prompt, type="system")
msgs_all.append(system_msg)

assist_prompt = msgb.unstruct_to_struct_prompt()
assist_msg = msgb.msg_from_prompt(assist_prompt)
msgs_all.append(assist_msg)

user_prompt = """
Extract the address and return in structured form:

Crown & Law Solicitors

Suite 121 Riverpark Business Centre 
Riverpark Road
Manchester

M40 2XP
"""

user_msg = msgb.msg_from_prompt(user_prompt, type="user")

msgs_all.append(user_msg)

print(msgs_all)

response = client.chat.completions.create(
  model="gpt-4o-2024-08-06",
  messages=msgs_all,
  temperature=0,
  max_tokens=4095,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "json_object"
  }
)

print(response.choices[0].message.content)
