# 定义函数进行四则运算
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2

# 主程序
while True:
    # 输入两个数字和操作符
    num1 = float(input('请输入第一个数字：'))
    operator = input('请输入运算符（+、-、*、/）：')
    num2 = float(input('请输入第二个数字：'))

    # 调用函数进行计算，并输出结果
    result = calculate(num1, num2, operator)
    print('计算结果为：', result)

    # 询问是否继续计算
    flag = input('是否继续计算（Y/N）：')
    if flag.upper() == 'N':
        print('结束计算。')
        break
以上代码实现了基本的加减乘除四则运算，可以循环进行计算，并在需要时终止程序。
