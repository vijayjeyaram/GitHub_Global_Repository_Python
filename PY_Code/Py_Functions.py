# Pass List
def pass_list(lst):
    lst[1] = "Testing"
    for l in lst:
        print("List Values are:", l)

myList = [10, "Test", 3.14]
pass_list(myList)

#Scenario-1 (By Position)
def add(name, age):
    print(name)
    print(age)

add("Test", 5)
print("---------------------------")
#Scenario-2 (By Keywords)
def add(name, age):
    print(name)
    print(age-5)

add(age=15, name="Test")
print("---------------------------")
#Scenario-2 (By default)
def add(name, age=30):
    print(name)
    print(age-5)

add("Test")
#If you pass the value the default value will be override
add("Test", 10)
print("---------------------------")
#Scenario - 3 (By Variable Length)
#No of Parameter is not fixed

def multiple_argument_add(*x):
    for i in x:
        j = i
        j = i + j
        print(j)

multiple_argument_add(5, 10, 15, 20, 25)
print("---------------------------")
def sum_multiple_argument(*y):
    m = 0
    for k in y:
        m = k + m
    print(m)

sum_multiple_argument(5, 10, 15, 20, 25)
print("---------------------------")
#Scenario - 4 (By Position,keyword,Variable Length)
def student_details(student_id, **student_data):
    print(student_id)
    for i, j in student_data.items():
        print(i, j)

student_details(201901, name="Testing", age="15", total_mark="497")

