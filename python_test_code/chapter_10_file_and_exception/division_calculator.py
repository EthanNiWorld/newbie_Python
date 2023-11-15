#print(5/0)
"""➜  python_test_code git:(main) ✗ /usr/local/bin/python3 /Users/ethan/Desktop/newbie_Python/python_test_code/chapter_10_file_and_exception/division_calculato
r.py
Traceback (most recent call last):
  File "/Users/ethan/Desktop/newbie_Python/python_test_code/chapter_10_file_and_exception/division_calculator.py", line 1, in <module>
    print(5/0)
          ~^~
ZeroDivisionError: division by zero"""


def division_calculator(a,b):
    try:
        t = int(a)/int(b)
        print(t)     #如果运行没问题，会跳过except
    except ZeroDivisionError:
        print("You cannot divide by Zero")
    except ValueError:
        #print("You need to input integer")
        pass    #让python什么都不做，不暴露问题给客户；
       
        
t = division_calculator(5,'a')

