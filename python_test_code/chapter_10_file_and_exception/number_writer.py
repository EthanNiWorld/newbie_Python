#JSON(JavaScript Object Notation) 格式最初是为JavaScript开发的，随后成为众多语言的数据存储标准；
from pathlib import Path
import json

numbers = [2,3,5,7,11,13]

path = Path('/Users/ethan/Desktop/newbie_Python/python_test_code/chapter_10_file_and_exception/number.json') #绝对路径
path1 = Path('chapter_10_file_and_exception/number1.json')   #相对路径

content = json.dumps(numbers)
path1.write_text(content)
path.write_text(content)


content1 = path1.read_text()
print(content1)