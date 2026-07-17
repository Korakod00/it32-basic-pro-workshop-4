gang_members = []


def add_members(name, age, gang):
    person = {
        'name': name,
        'age': age,
        'gang': gang
    }
    gang_members.append(person)

while True:
    big_c = input('1 เพิ่มสมาชิก | 2 สมาชิกทั้งหมด | 3 ออก: ')
    
    if big_c == "1":
        name = str(input('ชื่อ: '))
        age = int(input('อายุ: '))
        gang = str(input('แกงค์: '))
    
        add_members(name, age, gang)

    elif big_c == "2":
        print(gang_members)

    else:
        print('quit')
        break
