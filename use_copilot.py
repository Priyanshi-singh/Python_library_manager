#flet code to display list of items geenerated from a function

def display_list(list):
    for item in list:
        print(item)

def generate_list():
    list = []
    for i in range(10):
        list.append(i)
    return list

def main():
    list = generate_list()
    display_list(list)
#display a list using lambda function
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
#display a list using lambda function
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
