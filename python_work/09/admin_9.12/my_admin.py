from privileges import Admin

admin1 = Admin("admin1", "2121")
admin1.privileges.show_privileges()
admin1.privileges.privileges.append("can delete users")
admin1.privileges.show_privileges()
