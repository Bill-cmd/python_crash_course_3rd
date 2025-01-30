'''
def get_formatted_name(first_name, last_name):
    """返回标准格式的姓名"""
    fullname=f"{first_name} {last_name}"
    return fullname.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
'''
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name == '':
        full_name = f"{first_name} {last_name}"
    else:
        full_name = f"{first_name} {middle_name} {last_name}"
    return full_name

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)
