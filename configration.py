import json
import os

def get_config():
    """读取配置文件，如果不存在则初始化"""
    if not os.path.exists("config.json"):
        # 初始化一个默认配置
        default_config = {"stock_code_list": []}
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(default_config, f)

    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)


def update_config(config):
    """更新整个配置文件"""
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
    return config


def get_stock_code_list():
    """获取股票代码列表"""
    config = get_config()
    return config["stock_code_list"]


def update_stock_code_list(new_codes):
    """更新股票代码列表"""
    config = get_config()
    config["stock_code_list"] = new_codes
    update_config(config)
    return new_codes