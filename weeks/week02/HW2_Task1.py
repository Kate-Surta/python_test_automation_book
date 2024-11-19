my_list = [0,-12,8,-44,461]
for i in range(len(my_list)):
    for j in range(len(my_list) - i - 1):
        if my_list[j] > my_list[j+1]:
           my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
           print(my_list)

#bubble_sort_desc
my_list = [0,-12,8,-44,461]
for i in range(len(my_list)):
    for j in range(len(my_list) - i - 1):
        if my_list[j] < my_list[j+1]:
           my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
           print(my_list)


# bubble_sort_withEarlyStop
my_list = [0, -12, 8, -44, 461, 0, 666, 999]
for i in range(len(my_list)):
    is_swapped = False
    for j in range(len(my_list) - i - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            is_swapped = True
            print(my_list)
    if not is_swapped:
        break
