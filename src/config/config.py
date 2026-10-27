import json

def carregar_settings():
    config = dict({"meta_anual_finalizados": None, "max_jogando_simultaneos": 3})
    try:
        with open("src/config/config.json", encoding="utf-8") as arquivo:
            config.update(json.load(arquivo))
    except FileNotFoundError:
        pass  

    meta = config["meta_anual_finalizados"]
    if meta != None and (not isinstance(meta, int) or meta < 0):
        raise SystemExit("meta_anual_finalizados deve ser um inteiro >= 0")

    limite = config["max_jogando_simultaneos"]
    if not isinstance(limite, int) or limite < 1:
        raise SystemExit("max_jogando_simultaneos deve ser um inteiro >= 1.")

    return config