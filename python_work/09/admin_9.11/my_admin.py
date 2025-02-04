from users import User
from privileges import AdminPrivileges

# 创建一个Admin实例
admin = User('admin', '123456')
admin.privileges = AdminPrivileges()
admin.privileges.show_privileges()

