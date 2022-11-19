def hello():
    print('hello world')

def pack(a,b,c):
    return[a,b,c]

def what_to_eat(my_list):
    if len(my_list) == 0:
        print('My list is empty!')
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f'First I have to eat {my_list[0]}')
            else:
                for x in range(len(my_list)):
                    print(f'Next I\'ll get {my_list[1]}')



hello()
print(pack("a","b","c"))
print(pack(1,2,3))
what_to_eat([])
what_to_eat(["Apple","Chocolate", "Noodles", "Bacon", "Eggs"])
