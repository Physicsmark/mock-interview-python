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