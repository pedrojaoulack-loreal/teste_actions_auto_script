import datetime

# ... (seu código de web scraping ou outra tarefa aqui)

# Dados a serem adicionados ao arquivo:
dados_atuais = f"Dados coletados em: {datetime.datetime.now()}\n"

# Abre o arquivo em modo 'a' (append) para adicionar os novos dados ao final:
with open("dados.txt", "a") as arquivo:
    arquivo.write(dados_atuais)

print(f"Dados adicionados a dados.txt: {dados_atuais}")

# ... (resto do seu script, se houver)
