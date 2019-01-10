TapTap 求游戏论坛爬虫。

## 运行爬虫

在Python3 环境下：

`pip install -r requirement.txt`
导入相关库。

``scrapy crawl findgame -o gameforum.csv``
执行脚本，将数据导出成gameforum.csv文件中。


## 分词脚本
在python3环境下：
将分词数据`text.txt`放在`wordCount.py`同目录文件夹中。

执行`python wordCount.py`，生成分词结果。

## 已有数据集
在「数据文件夹」中，一共有五个文件。
- `qiuyouxi1106.csv`：2018年11月6日爬出的数据
- `text.txt`: 爬出数据中的标题复制结果。
- `wordCount.txt`：text分词结果，文本格式
- `wordCount.xls`：text分词结果，表格格式
- `标签透视.xlsx`: 根据TapTap的标签库筛选分词数据的结果。
