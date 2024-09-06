
base_name = "prompts/"

base_prompt_filenames = {
    "iso20022/fully_struct/cbpr_fully_struct_fields.md": True,
    "iso20022/hybrid/cbpr_hybrid_struct_fields.md": True,
    "iso20022/fully_struct/shopping_centre_build_name.md": True,
    "unstruct_to_struct/GB/1_hsbc_hq.md": True,
    "unstruct_to_struct/GB/2_cardiff_hospital.md": True,
    "unstruct_to_struct/GB/3_heywood_hill.md": True,
    "unstruct_to_struct/GB/4_casarotto.md": True,
    "unstruct_to_struct/GB/5_suite.md": True
}


def system_prompt():
    with open("prompts/system/system_unstruct_to_struct.md", "r") as sys_prmpt_file:
        return sys_prmpt_file.read()


def unstruct_to_struct_prompt():

    struct_filenames = base_prompt_filenames.copy()
    struct_filenames["iso20022/hybrid/cbpr_hybrid_struct_fields.md"] = False

    prompt_base = ""
    for filename, should_read in struct_filenames.items():
        if should_read:
            with open(f"{base_name}{filename}", "r") as file_handle:
                prompt_base += file_handle.read()

    return prompt_base


def msg_from_prompt(prompt, type="assistant"):
    return {
      "role": f"{type}",
      "content": [
        {
          "type": "text",
          "text": f"{prompt}"
        }
      ]
    }


if __name__ == "__main__":
    prompt = unstruct_to_struct_prompt()
    print(prompt)
