#!/usr/bin/python3
#
# Sliver extension manifest generator
# Red Skal / 2021
#

import os
import sys


entry_object = """
        {{
            "name": "{}",
            "entrypoint": "Main",
            "help": "changeme",
            "longHelp": "[[.Bold]]{}[[.Normal]] changeme",
            "allowArgs": true,
            "extFiles": [
                {{
                    "os": "windows",
                    "files": {{
                        "x64": "{}",
                        "x86": "{}"
                    }}
                }}
            ],
            "isReflective": false,
            "isAssembly": true
        }},"""

header = """
{{
    "extensionName": "{}",
    "extensionCommands": [
"""

footer = """
    ]
}"""


def main():
    if len(sys.argv) < 2:
        print("[!] Usage: gen.py <path> <ext_name>")
        os.exit(1)

    print(f"[+] Generating Sliver extension manifest file for: {sys.argv[1]}")
    output_string = header.format(sys.argv[2])

    os.chdir(sys.argv[1])
    ls = os.listdir()
    for entry in ls:
        output_string = output_string + \
            entry_object.format(entry.split(".")[0], entry.split(".")[0],
                                entry, entry)

    output_string = output_string[:-1] + footer

    with open(sys.argv[1]+"/manifest.json", "w") as f:
        f.write(output_string)


if __name__ == "__main__":
    main()
