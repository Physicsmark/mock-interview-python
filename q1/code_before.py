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