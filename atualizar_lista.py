import requests

# Lê o link do arquivo link_m3u.txt
with open('link_m3u.txt', 'r') as f:
    url = f.read().strip()

# Baixa o conteúdo da lista M3U
response = requests.get(url)

# Verifica se o download foi bem-sucedido
if response.status_code == 200:
    with open('listaETflix.m3u', 'wb') as f:
        f.write(response.content)
    print("Lista M3U atualizada com sucesso.")
else:
    print(f"Erro ao baixar a lista. Código de status: {response.status_code}")
