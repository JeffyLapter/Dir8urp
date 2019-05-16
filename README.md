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

2019/5/16任务分配：
--
NothingH 负责url输入检测函数开发，要求：用户输入任意url都转换成http://example.com 的形式，函数接收参数一个，函数返回数据为str形式，位置在module.py模块中<br>
测试用例：www.baidu.com - > http://www.baidu.com<br>
测试用例：http：//www.baidu.com - > http://www.baidu.com<br>
测试用例：www.baidu.com/admin -> http://www.baidu.com/admin<br>
<br>
HC1024 负责404检测函数重定向模块开发，实现module.py中 行57 identify404() 函数错误返回302的重定向，即当服务器返回重定向302跳转请求时，返回跳转的url，回显到用户窗口中。<br>实现方法：新写一个函数接收302跳转信息并提取requests返回的跳转链接，返回标准链接str，进而可通过requests调用。<br>修改identify404函数，添加条件，调用新写的302函数,函数返回标准str<br>
最终效果：<br>返回302跳转时<br>
>[!] 302 redirect from http://example.com/login to http://example.com/admin2
<br>
Anaz任务我没时间写了要上自习了回来再写
<br>
