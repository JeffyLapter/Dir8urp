Dir8urp
==
开发语言python，它的名字叫Dir8urp，非常de炫酷<br>
功能为扫描后台目录与敏感文件<br>
#依赖库：Simhash requests
命令：<br>
pip install Simhash<br>
pip install requests<br>
<br>

函数接口设计规范：
--
不可随便写变量名，要根据实际意义来写变量和函数名，注意在函数前面加注释，明确函数具有什么功能，要接受什么参数，返回什么数据<br>
冗余代码统一用三个引号包含<br>

2019/5/15任务分配：
--
NothingH 负责url输入检测函数开发，要求：用户输入任意url都转换成http://example.com/ 的形式，函数接收参数一个，函数返回数据为str形式，位置在module.py模块中<br>
测试用例：www.baidu.com - > http://www.baidu.com/<br>
测试用例：http：//www.baidu.com - > http://www.baidu.com/<br>

Anaz负责收集二级敏感目录，txt格式，换行书写，文件位置位于DICTS.txt <br>

示例<br>

>dicttest <br>
>admin <br>
>admin2 <br>
>wp-login <br>
>jboss <br>
>phpcms<br>
<br>

项目完成开发后作为默认后台字典使用<br>
