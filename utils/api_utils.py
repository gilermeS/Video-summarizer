import requests
from streamlit import secrets


api_key = secrets.deepseek_key


def generate_summary(text):

    url = "https://openrouter.ai/api/v1/chat/completions"


    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }


    data = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {"role": "system", "content": "Você é um assistente útil que resume os textos fornecidos em bullet points de até 2 linhas. O seu limite de bullet points é 20. Evite ao máximo se aproximar e ultrapassar esse limite."},
            {"role": "user", "content": text}
        ]
    }

    
    response = requests.post(url, headers=headers, json=data)


    if response.status_code == 200:
        
        resposta = response.json()
        
        return resposta['choices'][0]['message']['content']
        

    else:
        
        return "Erro:", response.status_code, response.text



def prettify(text):

    url = "https://openrouter.ai/api/v1/chat/completions"


    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }


    data = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {"role": "system", "content": "Você é um assistente útil que reformata o parágrafo de input e retorna esse texto com as quebras de parágrafo apropriadas dado o contexto e assunto do texto de input. Retorne apenas o texto reformatado e mais nada. Não adicione nada ao texto inicial."},
            {"role": "user", "content": text}
        ]
    }

    
    response = requests.post(url, headers=headers, json=data)


    if response.status_code == 200:
        
        resposta = response.json()
        
        return resposta['choices'][0]['message']['content']
        

    else:
        
        return "Erro:", response.status_code, response.text










