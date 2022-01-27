
def SelectMode():
    try :
        while True:
            select = str(SelectGUI())
            if select == "1" :
                LockPassword()
            elif select == "2" :
                KeyPassword()
            elif select == "0":
                break
            else:
                print("【无效选项】")
                input("【按回车键继续】")
    except:
        print("【非法操作】")
        input("【按回车键继续】")
    # 退出信息
def Exit():
    print('========================')
    print('感谢使用凯撒加密系统  ')
    print('欢迎下次使用凯撒加密系统  ')
    print('========================')    
        



# 选择GUI
def SelectGUI():
    print('========================')
    print('欢迎使用凯撒加密系统  ')
    print('请选择模式')
    print('【1.加密】【2.解密】【0.退出】')
    print('欢迎使用凯撒加密系统  ')
    print('========================')
    Select = input("【请输入你选择功能的序号】")
    return Select   

# 版本信息
def Loading(verson) :
    print('========================')
    print('欢迎使用凯撒加密系统  ')
    print('【作者】莫欣儿')
    print('【版本】v' + verson)
    print('欢迎使用凯撒加密系统  ')
    print('========================')

# 加密
def LockPassword() :
    password = input('【请输入您需要加密的内容】')
    print('========================')
    print('欢迎使用凯撒加密系统  ')
    print('【加密密码】',end = "")
    for p in password:
        if "a" <= p <= "z" :
            print(chr(ord("a") + (ord(p) - ord("a") + 3)%26),end = "")
        elif "A" <= p <= "Z" :
            print(chr(ord("A") + (ord(p) - ord("A") + 3)%26),end = "")
        else:
            print(p,end = "")
    print('\n========================')
    input("【按回车键继续】")
# 解密
def KeyPassword() :
    password = input('【请输入您要解密的内容】')
    print('========================')
    print('【欢迎使用凯撒加密系统】')
    print('【解密结果】',end = "")
    for p in password:
        if "a" <= p <= "z" :
            print(chr(ord("a") + (ord(p) - ord("a") - 3)%26),end = "")
        elif "A" <= p <= "Z" :
            print(chr(ord("A") + (ord(p) - ord("A") - 3)%26),end = "")
        else:
            print(p,end = "")
    print('\n========================')
    input("【按回车键继续】")
# 主程序


Loading("1.0")
SelectMode()
Exit()
