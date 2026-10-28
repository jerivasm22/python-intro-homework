
list1 = ["Python", "JavaScript", "SQL", "Java", "C++"]
list2 = ["C", "SQL", "PHP", "Ruby", "Python"]

set1 = set(list1)
set2 = set(list2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))