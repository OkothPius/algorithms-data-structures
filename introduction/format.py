price = 24
item = "banana"

print("The %s costs %d cents"%(item, price))
print("The %+4s costs %5.2f cents"%(item, price))

item_dict = {"item":"banana", "cost":14}
print("The %(item)s costs %(cost)7.1f cents"%item_dict)