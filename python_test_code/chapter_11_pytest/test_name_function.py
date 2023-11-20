from name_function import get_formatted_name

def test_first_last_name():       #pytest会找出test_开头的函数都执行一遍
    """能够正确处理像 ethan ni这样的姓名吗"""
    formatted_name = get_formatted_name('ethan','ni')
    assert formatted_name == 'Ethan Ni'    #断言，就是结果是否与右边匹配；

def test_first_middle_last_name():       #pytest会找出test_开头的函数都执行一遍
    """能够正确处理像 ethan ni这样的姓名吗"""
    formatted_name = get_formatted_name('ethan','ni','xiao')
    assert formatted_name == 'Ethan Xiao Ni'    #断言，就是结果是否与右边匹配；

