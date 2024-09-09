import os
import argparse
from dicttoxml import dicttoxml
import xml.dom.minidom
import msg_builder as msgb
from openai import OpenAI

import schemas.structured as ss


parser = argparse.ArgumentParser(
    description="Structure addresses in line with ISO 20022")
parser.add_argument('--file',
                    type=str,
                    help='file_name of input',
                    default="test_examples/simple_suite_1.txt")
parser.add_argument('--root_name',
                    type=str,
                    help='Name of root element when XML',
                    default="Cdtr")
parser.add_argument('--format',
                    type=str,
                    choices=['json', 'xml'],
                    help='Output format (json or xml)', default='json')

args = parser.parse_args()

api_key = os.getenv("OPENAI_API_KEY")
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

with open(args.file, "r") as test_data:
    user_prompt = test_data.read()

user_msg = msgb.msg_from_prompt(user_prompt, type="user")

msgs_all.append(user_msg)

response = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=msgs_all,
    temperature=0,
    max_tokens=4095,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format=ss.Address
)

addr_mdl = response.choices[0].message.parsed


if args.format == "json":

    addr_resp_json = addr_mdl.model_dump_json(
        indent=4,
        exclude_none=True)
    print(addr_resp_json)

else:
    addr_resp_dict = addr_mdl.model_dump(exclude_none=True)
    person_xml = dicttoxml(
        addr_resp_dict,
        custom_root=args.root_name, attr_type=False)

    xml_str = xml.dom.minidom.parseString(person_xml).toprettyxml()
    print(xml_str)
