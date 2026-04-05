import sys
import os
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import deepl

load_dotenv()
api_key = os.getenv("DEEPL_API_KEY")

if len(sys.argv) > 1:
    # individual: process specific file at once
    filename = sys.argv[1]
    input_path = os.path.join("input", filename + ".xml")
    tree = ET.parse(input_path)
    root = tree.getroot()
    headline = root.find("headline").text
    lead = root.find("lead").text
    body = root.find("body").text
    tail = root.find("tail").text

    translator = deepl.Translator(api_key)
    result = translator.translate_text(
        [headline, lead, body, tail],
        target_lang="EN-US"
    )
    root.find("headline").text = result[0].text
    root.find("lead").text = result[1].text
    root.find("body").text = result[2].text
    root.find("tail").text = result[3].text

    output_path = os.path.join("output", filename + " (EN).xml")
    tree.write(output_path, encoding="UTF-8", xml_declaration=True)

    

else:
    # batch: process all XML files in input/