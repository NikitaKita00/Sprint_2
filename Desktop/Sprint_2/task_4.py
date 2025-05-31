class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email=None):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours=None, rest_days=None):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment


emp1 = EmployeeSalary("Иван", hours=40, rest_days=2, email="ivan@mail.com")
print(f"Зарплата Ивана: {emp1.salary()}")

emp2 = EmployeeSalary.get_hours("Мария", rest_days=1)
print(f"Часы Марии: {emp2.hours}")
print(f"Зарплата Марии: {emp2.salary()}")

emp3 = EmployeeSalary.get_email("Алексей", hours=35, rest_days=2)
print(f"Почта Алексея: {emp3.email}")

EmployeeSalary.set_hourly_payment(450)
print(f"Новая зарплата Ивана: {emp1.salary()}")
