my_list = [[] for _ in range(10)]

def hash_function(value):
    sum = 0
    for char in value:
        sum += ord(char)
    return sum % len(my_list)

print(hash_function("Bob"))
    
def add(value):
    index = hash_function(value)
    my_list[index].append(value)


add("Bob")
add("Alice")
add("Charlie")
add("David")
add("Stuart")
add("Kevin")
add("bob")
add("alice")
add("charlie")
print(my_list)


def find(value):
    index = hash_function(value)
    return value in my_list[index]

print(find("Bob"))
print(find("Alice"))
print(find("Charlie"))
