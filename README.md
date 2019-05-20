Dir8urp
==
开发语言python 3.6，它的名字叫Dir8urp，非常de炫酷<br>
现在实现的功能为扫描后台目录与敏感文件<br>
希望在之后能有更多的功能<br>
内测开发者为:<br>JeffyLapter<br>NothingH<br>alazymechnaic<br>HC1024<br>
#依赖库：Simhash requests<br>
命令：<br>
pip install Simhash<br>
pip install requests<br>
测试import simhash,requests<br>
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

模块开发规范：
--
主菜单文件为menu.py,帮助文件在rely.py<br>
在编写新模块时，需要单独创建新的.py文件，并在主菜单导入，并在modules.py中写入AVAILABLE_USER_SELECT字典中，在menu.py在源代码基础上elif形式实现功能选择,在rely.py模块中写一个模块的help文档输出函数<br>
开发新模块时，如需要颜色显示，请使用已有的颜色类使用方法，颜色类在modules.py中,用法如下<br>


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
主程序位置BDirectory.py 实现主程序命令交互式菜单.<br>

2019/5/20任务分配：
--
请各位开发人员尽全力完善程序容错性，使用try except<br>
