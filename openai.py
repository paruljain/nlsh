import requests
from config import config

def __getCmdPayload(prompt):
    return {
        'model': "text-davinci-003",
        'prompt': prompt,
        'temperature': 0,
        'max_tokens': 50,
        'top_p': 1.0,
        'n': 1,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0,
        'stop': '\n'
    }

def __getHelpPayload(prompt):
    return {
        'model': "text-davinci-003",
        'prompt': prompt,
        'temperature': 0,
        'max_tokens': 200,
        'top_p': 1.0,
        'n': 1,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0
    }

def __callApi(payload):
    url = 'https://api.openai.com/v1/completions'
    headers = {
        'Authorization': f'Bearer {config["open_ai_api_key"]}'
    }
    payload = payload
    text = None
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=5)
    except:
        raise ConnectionError('Timed out waiting for GPT-3 to respond')
    
    if response.ok and len(response.json()['choices']) > 0:
        text = response.json()['choices'][0]['text']
    else:
        raise ConnectionError(f'GPT-3 error: {response.status_code}: {response.text}')

    return text

def getCmd(prompt):
    return __callApi(__getCmdPayload(prompt)).split('\n')[0].strip()

def getHelp(prompt):
    return __callApi(__getHelpPayload(prompt))
