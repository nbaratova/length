s = "a a a a b b b c c c d "
s = s.split()
my_map = {}

for i in s:
    if i in my_map:
        my_map[i] += 1
    else:
        my_map[i] = 1

my_list = list()
for x in range(5):
    try:
        first_max = max(my_map, key=my_map.get)
        my_list.append(f"{first_max} = {my_map[first_max]}")
        del my_map[first_max]
    except:
        pass

print("\n".join(my_list))
