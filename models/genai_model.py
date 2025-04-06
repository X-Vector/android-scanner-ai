from google import genai
from google.genai import types
from config import *



def scan_code(API, MODEL, instruction, code):
    result = ""
    count = 1
    client = genai.Client(api_key=API,)

    model = MODEL
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=code),
            ],
        ),
    ]
    tools = [
        types.Tool(google_search=types.GoogleSearch())
    ]
    generate_content_config = types.GenerateContentConfig(
        tools=tools,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text=instruction),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        result += chunk.text
        count += 1
    return result
