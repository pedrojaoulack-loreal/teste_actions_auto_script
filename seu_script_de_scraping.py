import datetime

# Seu código de web scraping ou outra tarefa aqui.
# Exemplo:
dados_atuais = f"Dados coletados em: {datetime.datetime.now()}\n"


# Abre o arquivo em modo append (adiciona ao final)
with open("dados.txt", "a") as arquivo:
    arquivo.write(dados_atuais)

# Adicione aqui o código para salvar outros dados coletados,
# por exemplo, o resultado do web scraping.

print(f"Dados salvos em dados.txt: {dados_atuais}")
