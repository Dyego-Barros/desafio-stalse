import kagglehub
import os 
from pathlib import Path

#Download Datase e-commerce Brasil
path_dataset = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

#Define Path absoluto para aquivo .env
abs_path = Path(__file__).resolve().parent.parent.parent

#Seta o path para arquivo
env_file = abs_path / ".env"

#Variavel
dataset_url = f"DATASET_PATH={path_dataset}\n"

#Procura ser o arquivo existe, adiciona a variavel de ambiente, caso nao exists cria o arquivo na raiz do. projeto
if env_file.exists():
    content = env_file.read_text().splitlines()
    if any(line.startswith("DATASET_PATH=") for line in content):
        print("Arquivo ja possui variavel de ambiente")
    else:
        content.append(dataset_url)
        env_file.write_text("\n" .join(content)+"\n")
        print(f"DATASET_PATH adicionada a arquivo")
else:
    with open(f"{abs_path}/.env", "w") as file :
     file.write(f"DATASET_PATH={path_dataset}\n")
    



print("Caminho do Dataset",path_dataset)