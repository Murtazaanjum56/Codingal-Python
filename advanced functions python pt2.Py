n1 = {2, 3, 4}
a1 = ("a", "b", "c")
result = zip(n1, a1)
print(list(result))

l1 = [10, 20, 30, 40]
l2 = [100, 200, 300, 400]

for x, y in zip(l1, l2[::-1]):
    print(x, y)


item = ["Mango:", "Toy:" "Shoes:"]
price = [20, 5, 100]

new_dict = {item: price for item,
            price in zip(item, price)}

print("\n{}".format(new_dict))