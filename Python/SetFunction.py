fruits = set(["avocado", "tomato", "banana"])
vegi = set(["beets", "carrots", "tomato"])

# intersections
print (fruits | vegi)

# Union, share all items, remove duplicated values
print (fruits & vegi)

# Show things that fruits has but vegi doesnt have
print (fruits - vegi)
