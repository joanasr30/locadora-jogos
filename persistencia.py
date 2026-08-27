import json


def carregar(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return dados
    except:
        return []


def salvar(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
