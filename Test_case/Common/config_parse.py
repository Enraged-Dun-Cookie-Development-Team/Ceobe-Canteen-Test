import json

def config_parse():
    with open ('../config.json') as f:
        cfg = json.loads(f)['testpara']
        return cfg