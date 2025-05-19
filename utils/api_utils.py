import requests
import config


api_key = config.deepseek_key


def generate_summary(text):

    url = "https://openrouter.ai/api/v1/chat/completions"


    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }


    data = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {"role": "system", "content": "Você é um assistente útil que resume os textos fornecidos em bullet points de até 2 linhas. O seu limite de bullet points é 10. Evite ao máximo passar desse limite."},
            {"role": "user", "content": text}
        ]
    }

    
    response = requests.post(url, headers=headers, json=data)


    if response.status_code == 200:
        
        resposta = response.json()
        
        return resposta['choices'][0]['message']['content']
        

    else:
        
        return "Erro:", response.status_code, response.text













