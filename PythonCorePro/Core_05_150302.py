#-*-coding:utf-8-*-
# Python 核心编程 第五章

print '-' * 15
print '''
复数：
	i + j
	num.real	实部
	num.imag	虚部
	num.conjugate()	返回公厄复数
'''

print '''
标准类型函数：
	cmp() str() type() 
数字类型函数:
	int() float() long() complex() bool()
功能函数:
	abs()		:绝对值
	coerce()	:将两个数转化为同一类型，并以元组形式返回
	divmod()	:把除法和取余运算结合起来，返回一个包含商和余数的元组
	pow()		:幂运算 如果有第三个参数 先幂运算，然后结果与第三个参数取余
	round()		:对浮点数进行四舍五入 若有第二个参数，则表明精确到第几位小数
仅用于整数的函数：
	进制转换函数 oct() 8进制 hex() 16进制
	ASCII 转换函数 ord() 接受一个字符 返回一个整数 chr() 接受一个单字节整数值 返回一个字符	
	unichr() 接受一个Unicode码值 返回对应的Unicode字符
'''

print '-' * 15
print '''
十进制浮点数：
	decimal 模块
'''

print '-' * 15
print '''
相关模块:
	decimal 	十进制浮点运算类
	array		高效数值数组
	math/cmath	常规数学运算math 复数运算cmath
	operator	数字运算符的函数实现
	random		多种伪随机数生成器

核心模块random:
	randrange()	接受和range()一样的参数，随即返回其中一项
	uniform(）	几乎和randint()一样，不过它返回的是两者之间的一个浮点数且不包括上限
	random()	类似与uniform() 只不过下限恒等于0.0 上限恒等于1.0
	choice(0	随即返回一个给定序列的一个元素
'''	

