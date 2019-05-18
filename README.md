Dir8urp
==
开发语言python 3.6，它的名字叫Dir8urp，非常de炫酷<br>
功能为扫描后台目录与敏感文件<br>
#依赖库：Simhash requests<br>
命令：<br>
pip install Simhash<br>
pip install requests<br>
<br>

函数接口设计规范：
--
标准示例返回url: http://www.example.com/admin123
<br>
不可随便写变量名，要根据实际意义来写变量和函数名，注意在函数前面加注释，明确函数具有什么功能，要接受什么参数，返回什么数据<br>
冗余代码统一用三个引号包含<br>
程序中已有的功能可在其基础上进行二次开发，以用于你自己的程序，为保证每个函数的可用性，禁止随意修改已经在其他函数中调用的函数<br>
程序中部分基础功能开发时尽量使其具有可移植性和较高的自由性<br>
每个功能需测试后再上线<br>
新功能必须写注释，为防止乱码，用英语<br>
在可用性基础上尽量保证函数的性能，不允许在函数中有初始化后全程未使用的变量出现<br>
所有人请在规定的代码区域书写代码,新建函数放在modules.py line36 之后，并仿照原有格式书写注释和作者名称<br>
>函数注释使用规范<br>
>#-- This is a Note before Functions --#<br>
>#-- ! THIS IS A WARNING NOTE BEFORE IMPORTANT FUNCTIONS ! --#<br>
>#-- * this is a note for one line note in functions * --#<br>
>#-- $variable means $variable is a variable that you used in your notes to explain your functions --#<br>
<br>

颜色类使用方法：
--
位置modules.py line 45 class Display_Color(object)<br>
使用方法<br>
>Display_Color.LOGO(PRIMARY_COLOR_DEFINE,"要更改颜色的数据")
>Display_Color.WRONG(PRIMARY_COLOR_DEFINE,"要更改颜色的数据")
>Display_Color.SUCCESS(PRIMARY_COLOR_DEFINE,"要更改颜色的数据")
>Display_Color.WARING(PRIMARY_COLOR_DEFINE,"要更改颜色的数据")
<br>
注意! :该类仅返回带有颜色的数据，不输出，输出请使用print<br>
例如
`print (Display_Color.LOGO(PRIMARY_COLOR_DEFINE,要改变颜色的数据))`

<br>

公示：
--
主检测函数将进行重写，以模块化类形式优化程序结构并单独封装，将利用hash方法，暂存方式，实现多个不同404页存储比对，来确保文件存在性检测返回结果精确。<br>
主程序位置BDirectory.py <br>
menu.py实现主程序命令交互式菜单.<br>
rely.py中HELP_DOUCUMENT为帮助文档，以后所有帮助文档模块均从rely调用<br>
READ_HELP_DOUCUMENTS()函数将会被优化为多帮助文档形式，用于BDirectory.py进行调用<br>
将会重新一个ADD_DICT函数，以用于添加字典，或涉及文件操作相关知识<br>
<br>

2019/5/16任务分配：
--
#NothingH 负责url输入检测函数开发，要求：用户输入任意url都转换成http://example.com 的形式，函数接收参数一个，函数返回数据为str形式，位置在module.py模块中<br>
测试用例：www.baidu.com - > http://www.baidu.com<br>
测试用例：http：//www.baidu.com - > http://www.baidu.com<br>
测试用例：www.baidu.com/admin -> http://www.baidu.com/admin<br>
<br>

#HC1024 负责404检测函数重定向模块开发，实现module.py中 行57 identify404() 函数错误返回302的重定向，即当服务器返回重定向302跳转请求时，返回跳转的url，回显到用户窗口中。<br>实现方法：新写一个函数接收302跳转信息并提取requests返回的跳转链接，返回标准链接str，进而可通过requests调用。<br>修改identify404函数，添加条件，调用新写的302函数,函数返回标准str<br>
最终效果：<br>返回302跳转时<br>
>[!] 302 redirect from http://example.com/login to http://example.com/admin2
<br>
#Anaz 负责try,except设计，依照目前可用的函数功能，为每个可用的函数添加try,except语句，如request.get语句如果执行不成功，便跳出该函数，并输出错误信息，让用户检查网络连接等。
<br>
