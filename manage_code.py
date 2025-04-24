import configration

stock_code = ["sh600519"]

def add_code(code):
    stock_code_list = configration.get_stock_code_list()
    if code in stock_code_list:
        print("代码已存在，请勿重复添加")
        return
    else:
        stock_code_list.append(code)
        configration.update_stock_code_list(stock_code_list)

def del_code(code):
    stock_code_list = configration.get_stock_code_list()
    if code in stock_code_list:
        stock_code_list.remove(code)
        configration.update_stock_code_list(stock_code_list)
    else:
        print("代码不存在，无法删除")
        return

print(configration.get_config())
add_code("sh600521")
print(configration.get_config())