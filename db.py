import json

class MysqlDatabases:
    def __init__(self):
        self.users = json.loads(open('users.json', 'r', encoding='utf-8').read())
        self.students = json.loads(open('students.json', 'r', encoding='utf-8').read())
    def checkLogin(self, username, password):
        for user in self.users:
            if user['username'] == username:
                if user['password'] == password:
                    return True, '登录成功'
                else:
                    return False, '密码错误'
        return False, '用户不存在'
    def all(self):
        return self.students

    def insert(self, student):
        self.students.append(student)

    def delete(self, name):
        for student in self.students:
            if student['name'] == name:
                self.students.remove(student)
                return True, '删除成功'
        return False, f'{name} 用户不存在'
    def search(self, name):
        for student in self.students:
            if student['username'] == name:
                self.students.remove(student)
                return True, student
        return False, f'{name} 用户不存在'
    def updata(self, stu):
        for student in self.students:
            if student['username'] == stu['username']:
                student.update(stu)
                return True, f'{stu['username']} 修改成功'
        return False, f'{stu['username']} 用户不存在'
db = MysqlDatabases()
if __name__ == '__main__':
    # print(db.checkLogin('admin', '123456'))
    print(db.all())