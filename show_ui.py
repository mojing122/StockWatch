import time
from rich import box
from rich.table import Table
from rich.live import Live
from get_stock_data import get_all_stock_data
from console import console

console.clear()

def init_table():
    table = Table(title=None, show_header=True, header_style="bold", box=box.SIMPLE_HEAD)

    # 定义表格列（可自定义颜色）
    table.add_column("股票", style="cyan", width=12)
    table.add_column("代码", style="magenta", justify="left")
    table.add_column("当前价格", style="white", justify="right")
    table.add_column("涨跌", style="white", justify="right")
    table.add_column("涨跌幅", style="bold white", justify="right")
    table.add_column("振幅", style="white", justify="right")
    table.add_column("今开", style="white", justify="right")
    table.add_column("更新时间", style="bold yellow")
    return table


def sync_table(table, data) -> Table:
    """生成带颜色的实时数据表格"""
    # 清空旧数据（保留表头）
    for row in table.rows.copy():
        table.rows.remove(row)

    # 添加新数据（模拟动态数据）
    for row in data:
        table.add_row(*row)
    return table

def show_table():
    table = init_table()
    # 使用 Live 上下文实现实时刷新
    with Live(table, console=console, refresh_per_second=5, vertical_overflow="visible"):
        while True:
            time.sleep(5)  # 控制刷新频率
            data = get_all_stock_data()
            sync_table(table, data)