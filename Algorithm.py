# This function will take a list as a parameter and sort it alphabetically
def alphabet_sort(x = list):
    order = []
    list_length = len(x)
    for item in x:
        order_index = list_length - 1
        for i in list_length:
            if item > x[i]:
                order_index = order_index - 1
        order.append(order_index)
    x = [x[i] for i in order]
    return x

#alphabet_sort(["apple", "bannana", "green bean", "danish", "pumpkin", "onion"])
x = ["apple", "bannana", "green bean", "danish", "pumpkin", "onion"]
x.sort()
print(x)