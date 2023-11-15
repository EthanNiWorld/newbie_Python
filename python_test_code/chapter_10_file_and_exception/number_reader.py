#JSON(JavaScript Object Notation) 格式最初是为JavaScript开发的，随后成为众多语言的数据存储标准；
from pathlib import Path
import json


path = Path('chapter_10_file_and_exception/number.json') #绝对路径
content = path.read_text()
numbers = json.loads(content) #loads()将json格式的字符串作为参数，返回一个Python对象
print(numbers)

