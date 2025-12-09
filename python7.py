#question 1
items=[3,5,7,9,11,13]
items.pop(4)
items.insert(1,11)
items.append(11)
print(items)

#question 2
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
result=first_set.intersection(second_set)
print(result)
print(first_set.difference(second_set))

#question 3
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
print(first_set.issubset(second_set))
print(second_set.difference(first_set))

#question 4
month = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54,
'Aug': 44, 'Sept': 54}
print(list(set(month.values())))

#question 5
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
result=set(sample_list)
tuples=tuple(result)
print('Tuple=',tuples)
print('Maximum number=', max(tuples))
print('Minimum number=',min(tuples))

#question 6 
i=int(input("Enter value of i: "))
j=int(input('Enter the value of j: '))
k=int(input('Enter '))
if i < 10:
    if j < 5:
        print('Result A')
    else:
        if k%2==0:
            print("Result B")
        else:
            print('Result C') 
else:
    if k>10:
        if i==k:
            print('Result D')
        else: 
            print('Result E')
    else: 
        print('Result F')

#question 7
club_A={'Alice','Bob','Charlie'}
club_B={'David','Eve','Bob'}
common_members=club_A.intersection(club_B)
if common_members:
    print("There is an overlap")
else:
    print("No overlap between clubs")

#question 8
i=int(input("Enter a number for i:"))
j=int(input("Enter a number for j:"))
k=int(input("Enter a number for k:"))
if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
    if j>k:
        j=i
    else:
        i=k
print(i,j,k)
#output 
# a=5 5 7
# b=9 -5 9
# c=8 12 12
# d=13 13 13 
# e=5 5 17
# f=17 15 17

#question 9
student={"name":input("Enter student's name:"),"course":input("Enter requested course:"),"grade":int(input("Enter student's grade:"))}
valid_courses=input("Enter valid courses(coma-separated):")
valid_courses = {c.strip() for c in valid_courses.split(",")}
print("Enter minimum required grade for each course:")
min_grades={}
for course in valid_courses:
    min_grade=int(input(f"Minimum grade for{course}:"))
    min_grades[course]=min_grade
if student["course"] not in valid_courses:
    print("Invalid course.")
elif student["grade"] < min_grades[student["course"]]:
    print(f"Grade too low for {student['course']}.")
else:
    print(f"{student['name']} approved for {student['course']}.")

#question 10 
required_tasks={"Email","Report","Meeting"}
completed_tasks={"Email","Report"}
if required_tasks.issubset(completed_tasks):
    print("All task done!")
else:
    print("some tasks pending.")
    
#question 11
student={
    "Shreeya Timilsina": "shreeya@gmail.com",
    "Prapti Bhetwal": "prapti@gmail.com",
    "Drishti Dangol": "drishti@yahoo.com",
}
name=input("Enter the student's full name:")
if name in student:
    print("Email:",student[name])
else:
    print("Contacts not found")

#question 12
shopping_list={ "Milk","Bread","Eggs"}
bought_containing={"Bread","Eggs"}
remaining=shopping_list.difference(bought_containing)
if remaining:
    print(f"Still need to buy:{remaining}")
else:
    print("Shopping complete!")

#question 13
class_list=["ram","sita", "laxman"]
new_student='ram'
if new_student in class_list:
    print("ram is already in class")
else:
    class_list.append('ram')
    print(class_list,"Added ram")
    
#question 14
votes = ["Blue", "Red", "Blue", "Green", "Blue"]
count=votes.count('Blue')
print(count)
if count>=3:
    print("Blue wins!")
else:
    print("Blue did not win")

#question 15
grade={'Ram':92,'sita':88}
student='Laxman'
if student in grade:
    print(f"{student}'s grade is {grade[student]}")
else:
    print(f"Grade not available for {student}")

#question 16
student={'name':input("Enter the name:"),
         'course':input("Enter the course:"),
         'grade':int(input("Enter the grade:"))
         }
valid_courses={'Creative Writing', 'Robotics','Digital Art'}
name=student['name']
course=student['course']
grade=student['grade']
if grade>=9 and grade<=12:
    print(f"{name} is approved for {course}")
elif course=='Robotics' and grade==9:
    print(f"{name} is not eligible for {course} (grade too low)")
else:
    print(f"{name} selected an invalid course")
    
    
#question 17
applicant = {
 "name": "Priya",
 "skills": ["Java", "SQL"],
 "experience": 1
}
required_skills = {"Python", "Java"}
name=applicant['name']
skills=applicant['skills']
experience=applicant['experience']
has_required_skills = any(skill in required_skills for skill in skills)
if has_required_skills and experience>=2:
    print(f"{name} qualifies")
else:
    print(f"{name} does not qualify")
    
    
#question 18
banned_list={"scissors", "knife","lighter"}
weight=int(input("Enter the weight of baggage (in kg):"))
item_carried=input("Enter the name of the item:")
if weight<=7 and item_carried not in banned_list:
    print("Bag accepted")
else:
    print("Bag not allowed")


#question 19
group1_input = input("Enter names for Group 1 (comma-separated): ")
group1 = {name.strip() for name in group1_input.split(",")}
group2_input = input("Enter names for Group 2 (comma-separated): ")
group2 = {name.strip() for name in group2_input.split(",")}
if group1.intersection(group2):
    print("Warning: Groups share at least one student!")
else:
    print("Groups are OK – no overlap.")
    

#question 20
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Shyam', 'salary': 500}
}
for key, value in sample_dict.items():
    if value.get('name')=='Shyam':
        value['salary']=8500
print(sample_dict)


#question 21
riya={"bread", "butter", "jam", "tea"}
anjali={"butter", "jam","coffee", "eggs"}
extra_items=riya-anjali
if extra_items:
    print(f"Riya has extra items:{extra_items}")
else:
    print("Riya has no extra items")
    

#question 22
alice_items={'apple','pen','scissor'}
bob_items={'mango','drinks','copy','pen'}
if alice_items.intersection(bob_items):
    print("They have some common items")
else:
    print("They picked copletely different items")
