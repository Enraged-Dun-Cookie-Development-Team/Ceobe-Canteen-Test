import json


def config_parse():
    # 运行此文件的话要使用相对此文件的路径，由什么文件调用路径应用相对于那个文件的路径
    with open ("config.json") as f:
        jsonstr = str(f.read())
        cfg = json.loads(jsonstr,strict=False)
        return cfg["testpara"]


config_parse()