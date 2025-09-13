# 一、下XHR断点
    将“https://match.yuanrenxue.cn/api/match/1”添加至XHR断点

# 二、跟栈

![bc2b88595241ccc5e5a3f3c47b6da2fb](D:\qq\Tencent Files\1916942714\nt_qq\nt_data\Pic\2025-09\Ori\bc2b88595241ccc5e5a3f3c47b6da2fb.png)

发现这里出现了加密字符串，这里即为入口函数
我们需要oo0O0()和window.f来破解这个加密，

**oo0O0()**返回的是"",所以主要目标是**window.f**

# 三、逆向分析
1、在往上跟一级，进入1这个文件，可以发现入口函数文件是由1这个文件里面执行eval函数生成的
![img_1](E:\Pycharm_Project\The-Journey-of-Web-Scraping-from-Scratch\猿人学\题目1：抓取所有（5页）机票的价格\img_1.png)

2、于是仔细研究1这个文件，发现里面有oo0O0()这个函数，
而且在这个函数的最底部,有这样一行代码：
```JS
eval(atob(window['b'])[J('0x0', ']dQW')](J('0x1', 'GTu!'), '\x27' + mw + '\x27'));
```
很可疑！！！
将其用控制台打印一下可得到：J('0x0', ']dQW') ===> replase

atob(window['b']):
![image-20250913161049128](C:\Users\19169\AppData\Roaming\Typora\typora-user-images\image-20250913161049128.png)
注意在这个文本最后有：window.f = hex_md5(mwqqppz)

![image-20250913161120516](C:\Users\19169\AppData\Roaming\Typora\typora-user-images\image-20250913161120516.png)

**window.f**已找到，将这一大串封装为字符串的代码转化为js文件，得到window_atob文件。
然后结合gateway.js文件运行一下，不报错，且输出正确的加密格式

![image-20250913161223808](C:\Users\19169\AppData\Roaming\Typora\typora-user-images\image-20250913161223808.png)

OK，本题done！