import os

# 定义学生列表,保存所有学生信息
stu_list = []
tab = '\t\t'


def show_menu():
    """
    打印菜单
    :return:
    """
    print(tab + '*' * 81)
    print(tab + '*\t\t\t\t*学生信息管理系统*\t\t\t\t*')
    print(tab + '*' * 81)
    print(tab + '*\t\t1.添加学生信息\t\t\t2.删除学生信息\t\t\t*')
    print(tab + '*' * 81)
    print(tab + '*\t\t3.修改学生信息\t\t\t4.查询单个学生信息\t\t*')
    print(tab + '*' * 81)
    print(tab + '*\t\t5.查询所有的学生信息\t\t6.退出系统\t\t\t*')
    print(tab + '*' * 81)


def insert_info():
    """
    添加学生信息
    :return:
    """
    # 通过input函数获取学生的信息(姓名,学号,性别,年龄,专业)
    name = input(tab + '请输入学生姓名:')
    sno = input(tab + '请输入学生学号:')

    # 判断学号是否重复
    for stu in stu_list:
        if stu['sno'] == sno:
            print('\n' + tab + '该学号已存在,请勿重复添加!!!')
            return

    gender = input(tab + '请输入学生性别:')
    age = input(tab + '请输入学生年龄:')
    major = input(tab + '请输入学生专业:')

    # 将学生信息转换为字典进行保存
    stu_dict = {'name': name, 'sno': sno, 'gender': gender, 'age': age, 'major': major}

    # 将这个学生字典添加到列表中
    stu_list.append(stu_dict)
    print('\n' + tab + '学生信息添加成功!')


def remove_info():
    """
    删除学生信息
    :return:
    """
    # 使用input()获取要删除的学生学号
    sno = input(tab + '请输入要删除的学生的学号:')
    # 判断学生信息是否存在
    for stu in stu_list:
        if stu['sno'] == sno:
            # 学生信息存在,对学生进行删除操作
            stu_list.remove(stu)
            print('\n' + tab + '删除成功!')
            break
    # 学生信息不存在,直接结束
    else:
        print('\n' + tab + '该学生信息不存在,无法删除!!!')


def modify_info():
    """
    修改学生信息
    :return:
    """
    # 使用input()获取要修改的学生学号
    sno = input(tab + '请输入要修改的学生的学号:')
    # 判断学生信息是否存在
    for stu in stu_list:
        if stu['sno'] == sno:
            # 学生信息存在,对学生进行修改操作
            stu['name'] = input('\n' + tab + '请输入修改后的姓名:')
            stu['sno'] = input(tab + '请输入修改后的学号:')
            stu['gender'] = input(tab + '请输入修改后的性别:')
            stu['age'] = input(tab + '请输入修改后的年龄:')
            stu['major'] = input(tab + '请输入修改后的专业:')
            break
    # 学生信息不存在,直接结束
    else:
        print('\n' + tab + '该学生信息不存在!!!')


def search_info():
    """
    查询单个学生信息
    :return:
    """
    # 使用input()获取要查询的学生学号
    sno = input(tab + '请输入要查询的学生的学号:')
    # 判断学生信息是否存在
    for stu in stu_list:
        if stu['sno'] == sno:
            # 学生信息存在,对学生进行查询操作
            print('\n' + tab + f'姓名:{stu["name"]},学号:{stu["sno"]},性别:{stu["gender"]},年龄:{stu["age"]},专业:{stu["major"]}')
            break
    # 学生信息不存在,直接结束
    else:
        print('\n' + tab + '该学生信息不存在!!!')


def show_all_info():
    """
    查询所有的学生信息
    :return:
    """
    if len(stu_list) > 0:
        for stu in stu_list:
            print(tab + f'姓名:{stu["name"]},学号:{stu["sno"]},性别:{stu["gender"]},年龄:{stu["age"]},专业:{stu["major"]}')
    else:
        print('\n' + tab + '暂无学生信息!')


def save():
    """
    保存功能
    :return:
    """
    f = open('student.txt', 'w', encoding='utf-8')
    f.write(str(stu_list))
    f.close()


def load_file():
    """
    读取文件
    :return:
    """
    global stu_list
    if os.path.exists('student.txt'):
        f = open('student.txt', 'r', encoding='utf-8')
        buf = f.read()
        if buf:
            stu_list = eval(buf)
        f.close()


def main():
    load_file()  # 只执行一次
    while True:
        show_menu()
        option = input(tab + '请选择相应的操作:')
        print()
        if option == '1':
            # 添加学生信息
            insert_info()
            save()
        elif option == '2':
            # 删除学生信息
            remove_info()
            save()
        elif option == '3':
            # 修改学生信息
            modify_info()
            save()
        elif option == '4':
            # 查询单个学生信息
            search_info()
        elif option == '5':
            # 查询所有的学生信息
            show_all_info()
        elif option == '6':
            print(tab + '您已退出本系统!')
            # save()
            break
        else:
            print('\n' + tab + '输入有误,请重新输入!!!')
            # continue
        input('\n' + tab + '......请按回车键继续......')
        os.system('cls')
        print('\b')


main()
