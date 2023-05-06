group1 = ("Hanan", "Mohammed", 25, 26, True)
print(group1[0])

group2 = ["Hanoon", "Hamood", 18, 19, False]
group2[2] = "Hamodi"
print(group2[2])
group2.append("Love")
print(group2)
group2.pop()
print(group2)

group3 = {'name': 'Jack', 'age': 26, 'weight': 80, 'has_glasses': False}
group3['name'] = 'Mohammed'
print(group3['name'])
group3['age'] = 50
print(group3['age'])
group3['last_name'] = 'Alashqar'
print(group3['last_name'])
w = group3.pop('has_glasses')
print(w)

print(type(2.62))
print(type(group3))

print(len("Hello World!"))
print(len(group3))