mydict1 = {"smith": 25, "John": 25, "henry": 25}
ages = list(mydict1.values())
names = list(mydict1.keys())
if len(set(ages)) == 1:
    print(names[0] + ',' + names[1] + ',' + names[2] + ' have same ages')
    print()
else:
    min_age = min(ages)
    person = [person for person in mydict1 if mydict1[person] == min_age][0]
    print(person + ' is younger')

