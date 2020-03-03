from datetime import datetime
data = [
    dict(name='Qinger', gender='女', birthday='19960412'),
    dict(name='Kitty', gender='女', birthday='20000412'),
    dict(name='Yufei', gender='女', birthday='20050412'),
    dict(name='Yufei', gender='女', birthday='20110412')
]


class Student:
    def __init__(self, name, gender, birthday):
        self.name = name
        self.gender = gender
        self.birthday = birthday


class System:
    def __init__(self, name):
        self.name = name
        self.data = []

    def show_menu(self):
        print(f"""
                 *********************************
                       欢迎使用【{self.name}】
                       1，显示全部学生信息
                       2，查找学生信息
                       3，添加学生信息
                       4，修改学生信息
                       5，删除学生信息
                       0，退出系统
                 **********************************
                    """)

    def load_data(self):
        for item in data:
            student = Student(item['name'], item['gender'], item['birthday'])
            self.data.append(student)

    def show_all_student(self):
        for index, item in enumerate(self.data):
            self.show_one_student(index)

    def show_one_student(self,index):
        current_time = datetime.now().year
        print(f'序号：{index}', end='\t')
        print(f'姓名：{self.data[index].name}', end='\t')
        print(f'生日：{self.data[index].birthday}', end='\t')
        print(f'年龄：{current_time - int(self.data[index].birthday[:4])}', end='\t')
        print(f'性别：{self.data[index].gender}')

    def choose_gender(self):
        while True:
            print('1:男生  2：女生')
            number = input('输入1或2选择学生性别')
            if number == '1':
                gender='男'
                return gender
            elif number == '2':
                gender='女'
                return gender

    def name_input(self):
        while True:
            name = input('新建学生姓名：').strip()
            if name:
                return name

    # 读取输入信息：姓名，性别，生日
    def add_one_student(self):
        name = self.name_input()
        gender = self.choose_gender()
        birthday = input('新建学生日：')
        aa = Student(name, gender, birthday)
        return aa

    def op(self):
        while True:
            op = input('输入操作符:')
            if op == '1':
                self.show_all_student()
            if op == '2':
                self.show_one_student(self.search())
            if op == '3':
                self.data.append(self.add_one_student())
                print('新建学生信息成功')
            if op == '4':
                self.data[self.search()] = self.add_one_student()
                print('修改学生信息成功')
            if op == '5':
                self.data.remove(self.data[self.search()])

    # 输入姓名查找，返回序号
    def search(self):
        while True:
            name = input('请输入学生姓名：')
            for index, item in enumerate(self.data):
                if item.name == name:
                    return index
            print('查无此人')


if __name__ == '__main__':
    ss = System('LvDi学生系统')
    ss.show_menu()
    ss.load_data()
    ss.op()

