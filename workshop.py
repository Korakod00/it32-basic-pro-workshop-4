gang_members = []
# person = {
#     'name': '',
#     'age': '',
#     'gang': ''
# }

def add_members(name, age, gang):
    print(name, 'ชื่อ')
    print(age, 'อายุ')
    print(gang, 'แกงค์')

while True:
    big_c = input('1 ชื่อ | 2 อายุ | 3 แกงค์: ')
    name = str(input('ชื่อ: '))
    age = int(input('อายุ: '))
    gang = str(input('แกงค์: '))
    
    add_members(name, age, gang)