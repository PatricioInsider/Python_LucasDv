#llaves y claves

subjects = {"Math":[],
          "Englinh": [],
          "History": [],
          "Science": [],
          "IT": []}


for key in subjects:
  print("===", key, "")
  for i in range (1, 4):
    subjects[key].append(int(input("Nota trimestre {} ".format(i))))
for key,val in subjects.items():
    print(key,":", sum(val)/len(val))

subjects_copy = subjects.copy()
print(subjects_copy)