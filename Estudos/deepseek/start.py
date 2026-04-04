import requests

# Substitua pela sua chave de API do OpenRouter
API_KEY = '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'
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

# Defina os cabeçalhos para a requisição da API
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Defina o payload da requisição (dados)
""" data = {
    "model": "deepseek/deepseek-chat:free",
    "messages": [{"role": "user", "content": "Qual é o significado da vida?"}]
} """
""" data = {
    "model": "deepseek/deepseek-chat:free",
    "messages": [{"role": "user", "content": "Qual a funcionalidade do programa {PD4000} do módulo de {MPD - Pedidos} no produto TOTVS {Linha Datasul} ?  P.S: gerar um resumo unico maximo 400 caracteres"}]
} """
data = {
    "model": "deepseek/deepseek-chat:free",
    "messages": [{"role": "user", "content": "Qual a funcionalidade do programa bas_acerto_cta_eec_inv_autom - Consulta Abatimento Contra Antecipação do módulo de ACR - Contas a Receber no produto TOTVS Linha Datasul ?(Objetivo e Principais Funcionalidades em 600 caracteres, sem resumos no final )"}]
}

# Envie a requisição POST para a API DeepSeek
response = requests.post(API_URL, json=data, headers=headers)

# Verifique se a requisição foi bem-sucedida
if response.status_code == 200:
    # print("Resposta da API:", response.json())
    # Extrair o conteúdo da mensagem do assistente
    content = response.json()['choices'][0]['message']['content']

    # Imprimir o conteúdo
    print(content)

else:
    print("Falha ao buscar dados da API. Código de Status:", response.status_code)