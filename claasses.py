# use classes to reuse data and build upon them later.
# methods - function associated with a classes
# attributes - data
import datetime


class Employee:

    raise_amount = 1.04
    noe = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + '.' + last + '@protonmail.com'

        Employee.noe +=1

        # instance variables are unique for each instance

    # class variables are same for all instances in a class
    @property
    def fullname(self):
        return("{} {}".format(self.first,self.last))

    @property
    def email(self):
        return "{}.{}@protonmail.com".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

    @classmethod
    def setram(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_wd(day):
        if day.weekday()==5 or day.weekday() ==6:
            return False
        else:
            return True

    def __repr__(self):
            return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleted name!")
        self.first = None
        self.last = None

# class -> blue print for creating instances


emp1 = Employee("dan","smith",21312)
print(emp1)

emp1.first = "Dylan"

print(emp1.email)
emp1.fullname = 'Corey Schafer'
print(emp1.fullname)
del emp1.fullname

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang


dev1 = Developer("John","doe",345325,'Python')
dev2 = Developer("Steve","Wozniak",1000,"SQL")

print(dev1.email)
print(dev2.prog_lang)


class Manager(Employee):
    raise_amount = 1.12

    def __init__(self,first,last,pay,branch,employees=None):
        Employee.__init__(self,first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp  in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->', emp.fullname())


mgr1 = Manager("Sue","Smith",9000,"technical",[dev1])
print(mgr1.pay)
mgr1.print_emp()
mgr1.add_emp(dev2)
mgr1.print_emp()

mgr1.remove_emp(dev1)

mgr1.print_emp()


print(int.__add__(1,2))
print(str.__add__('a','b'))
