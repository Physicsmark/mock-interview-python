# Question

You're asked to review a developer's implementation after he/she finished the story after adding the Employee object and show the employee ages with desc/asc orders. Please provide the comments after your review.

__Notes: You don't need to review main function, the comments would focus on Employer and Employee class.__

## Before Implementation

Codes:

```python
class Employer:
    """
    Construct an employer object with employee in it
    """
    def __init__(self, name: str, employee: list):
        self.name = name
        self.employee = employee

    def get_employee_count(self) -> int:
        return len(self.employee)


def main():
    company1 = Employer("1bM", ["alan", "alice", "bob"])
    print("company1: %s, employee number: %d" % (company1.name, company1.get_employee_count()))

if __name__ == "__main__":
    main()
```

Outputs:

```
company1: 1bM, employee number: 3
```


## After Implementation

Codes:

```python
class Employee:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Employer:
    """
    Construct an Employer object with employees in it
    """
    def __init__(self, name: str, employee: list):
        self.name = name
        self.employee = employee if employee else []

    def get_employee_count(self) -> int:
        return len(self.employee)

    def getEmployeeByAgeDesc(self) -> list:
        results = [] + self.employee
        n = len(self.employee)
        for i in range(0, n):
            for j in range(i + 1, n):
                if results[i].age < results[j].age:
                    results[i], results[j] = results[j], results[i]
        return results

    def getEmployeeByAgeAsc(self) -> list:
        results = [] + self.employee
        n = len(self.employee)
        for i in range(0, n):
            for j in range(i + 1, n):
                if results[i].age > results[j].age:
                    results[i], results[j] = results[j], results[i]
        return results

def main():
    employees = [["Alan", 30], ["Alice", 24], ["Bob", 35]]
    company1 = Employer("1bM", [Employee(e[0], e[1]) for e in employees])

    print("company1: %s, employee number: %d" % (company1.name, company1.get_employee_count()))
    print("--")
    print("Employee list:")
    for e in company1.getEmployeeByAgeAsc():
        print("name: %s, age: %d" % (e.name, e.age))

if __name__ == "__main__":
    main()
```

Outputs:

```
company1: 1bM, employee number: 3
--
Employee list:
name: Alice, age: 24
name: Alan, age: 30
name: Bob, age: 35
```