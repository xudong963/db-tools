import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def plot_distribution(csv_file, column_index):
    # 读取 CSV 文件，并按 | 分隔
    try:
        data = pd.read_csv(csv_file, delimiter='|', header=None)
    except FileNotFoundError:
        print(f"File {csv_file} not found.")
        return
    except pd.errors.EmptyDataError:
        print(f"File {csv_file} is empty.")
        return
    except pd.errors.ParserError:
        print(f"File {csv_file} is not a valid CSV.")
        return

    # 检查列索引是否在范围内
    if column_index < 0 or column_index >= data.shape[1]:
        print(f"Column index {column_index} is out of range.")
        return

    # 获取指定列的数据
    column_data = data.iloc[:, column_index]

    # 绘制分布图
    plt.figure(figsize=(10, 6))
    sns.histplot(column_data, kde=True, bins=30)
    plt.title(f'Distribution of Column {column_index}')
    plt.xlabel(f'Column {column_index}')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <csv_file> <column_index>")
    else:
        csv_file = sys.argv[1]
        try:
            column_index = int(sys.argv[2])
            plot_distribution(csv_file, column_index)
        except ValueError:
            print("Column index must be an integer.")
