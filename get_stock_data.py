import requests
import configration

stock_code_list = configration.get_stock_code_list()

column_code = [1, 2, 3, 31, 32, 43, 5, 30]

def get_stock_data(stock_code):
    url = f"http://qt.gtimg.cn/q={stock_code}"
    response = requests.get(url)
    data  = response.text
    split_data = data.split("~")
    # print(split_data)
    result = []
    for code in column_code:
        if code in [3,31,32]:
            if eval(split_data[31]) > 0:
                style = "[red]"
            else:
                style = "[green]"
            source_content = split_data[code]
            content = style + source_content
        elif code == 30:
            source_content= split_data[code]
            if ":" in source_content:
                content = source_content[5:].replace("-", "/")
            else:
                content = source_content[4:6]+"/"+source_content[6:8]+" "+source_content[8:10]+":"+source_content[10:12]+":"+source_content[12:14]
        else:
            content = split_data[code]
        result.append(content)

    return result

def get_all_stock_data():
    result = []
    for stock_code in stock_code_list:
        stock_data = get_stock_data(stock_code)
        result.append(stock_data)

    return result

if __name__ == '__main__':
    get_all_stock_data()
