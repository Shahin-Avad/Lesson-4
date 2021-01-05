my_list = [1, 2, 2, 3, 4, 1, 2]
new_list = [el for el in my_list if my_list.count(el)==1]
print(new_list)