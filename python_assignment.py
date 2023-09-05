class Employee:
    def __init__(self, Empid, Name, Age, Salary):
        self.Empid = Empid
        self.Name = Name
        self.Age = Age
        self.Salary = Salary

emps = [Employee("121E90","Raman",41,56000),Employee("161F91","Himadari",38,67500),\
        Employee("161F99","Jaya",51,82100),Employee("171E20","Tejas",30,55000),\
            Employee("171G30","Ajay",45,44000)]

def search_age(emps, sign, age):
    res = []
    for i in emps:
        if sign == ">" and i.Age>age:
            res.append(i)
        elif sign == "<" and i.Age<age:
            res.append(i)
        elif sign == "<=" and i.Age<=age:
            res.append(i)
        elif sign == ">=" and i.Age>=age:
            res.append(i)
    return res

def search_salary(emps, sign, sal):
    res = []
    for i in emps:
        if sign == ">"and i.Salary > sal:
            res.append(i)
        elif sign == "<" and i.Salary < sal:
            res.append(i)
        elif sign == "<=" and i.Salary<=sal:
            res.append(i)
        elif sign == ">=" and i.Salary >= sal:
            res.append(i)
    return res

def search_Empid(emps,empid):
    res = []
    for i in emps:
        if i.Empid == empid:
            res.append(i)
    return res

while True:
    print("Select:")
    print("1.search by age")
    print("2.search by salary")
    print("3.search by empid")
    print("4.Exit")
    ch = int(input("Enter you choice(1-4):"))
    if ch == 1:
        s = input("Enter opertor(<,>,<=,>=):")
        age = int(input("Enter Age:"))
        res = search_age(emps,s,age)
    elif ch ==2:
        s = input("Enter opertor(<,>,<=,>=):")
        sal = int(input("Enter salary:"))
        res = search_salary(emps,s,sal)
    elif ch == 3:
        empid = input("Enter Empid:")
        res = search_Empid(emps,empid)
    elif ch == 4:
        break
    for i in res:
        print(f"Employe ID:{i.Empid},Name:{i.Name},Age:{i.Age},Salary:{i.Salary}")