# Создайте класс с описанием работника. Любого работника. Employee.
from datetime import date, datetime


class Employee:
    def __init__(
            self,
            full_name: str,
            address: str,
            phone_number: int,
            ssn: int,
            birth_date: date,
            department: str,
            position: str,
            start_date: date,
            salary: float,
            fired: bool
    ):
        """
            Initializes attributes that describe employee
        """
        self.__full_name = full_name
        self.__address = address
        self.__phone_number = phone_number
        self.__ssn = ssn
        self.__birth_date = birth_date
        self.__department = department
        self.__position = position
        self.__start_date = start_date
        self.__salary = salary
        self.__fired = fired

    @property
    def full_name(self) -> str:
        """
            Gets the employee's full name
        """
        return self.__full_name

    @property
    def address(self) -> str:
        """
            Gets the employee's address
        """
        return self.__address

    @property
    def phone_number(self) -> int:
        """
            Gets the employee's phone number
        """
        return self.__phone_number

    @property
    def ssn(self) -> int:
        """
            Gets the employee's social security number
        """
        return self.__ssn

    @property
    def birth_date(self) -> date:
        """
            Gets the employee's birth date
        """
        return self.__birth_date

    @property
    def age(self) -> int:
        """
            Gets the employee's age
        """
        days_in_year = 365.2425
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) <
                                                   (self.birth_date.month,
                                                    self.birth_date.day))
        return age

    @property
    def department(self) -> str:
        """
            Gets the employee's department
        """
        return self.__department

    @property
    def position(self) -> str:
        """
            Gets the employee's position
        """
        return self.__position

    @property
    def start_date(self) -> date:
        """
            Gets the employee's start date
        """
        return self.__start_date

    @property
    def salary(self) -> float:
        """
            Gets the employee's salary
        """
        return self.__salary

    @property
    def fired(self) -> bool:
        """
            Gets the employee's salary
        """
        return self.__fired

    def salary_with_raise(self, salary_raise):
        if salary_raise > 0:
            return self.salary + salary_raise
        else:
            "It is a fine, not salary raise"

    def fire_employee(self):
        if self.fired:
            return "The employee does not work with us anymore."
        else:
            return "The employee is not fired yet, but we can change it."


if __name__ == "__main__":
    my_employee = Employee("John Doe",
                           "Warren st., 15/4",
                           12345323,
                           46785874,
                           datetime(1982, 6, 23),
                           "Test department",
                           "Test position",
                           datetime(2020, 3, 9),
                           2340.55,
                           False)

    print(my_employee.fire_employee())