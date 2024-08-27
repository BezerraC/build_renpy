import os

def verify_or_create_directory(path):
    if not os.path.exists(path):
        print(f"Erro: O diretório '{path}' não foi encontrado. Criando...")
        os.makedirs(path)
