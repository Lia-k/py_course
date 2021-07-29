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
            salary: float
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

    @property
    def full_name(self) -> str:
        """
            Gets the employee's full name
        """
        return self.__full_name

    @full_name.setter
    def full_name(self, new_name: str):
        """
            Sets new employee's name
        """
        self.__full_name = new_name

    @property
    def address(self) -> str:
        """
            Gets the employee's address
        """
        return self.__address

    @address.setter
    def address(self, new_address: str):
        """
            Sets new employee's address
        """
        self.__address = new_address

    @property
    def phone_number(self) -> int:
        """
            Gets the employee's phone number
        """
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, new_phone_number: int):
        """
            Sets new employee's phone number
        """
        self.__phone_number = new_phone_number

    @property
    def ssn(self) -> int:
        """
            Gets the employee's social security number
        """
        return self.__ssn

    @ssn.setter
    def ssn(self, new_ssn: int):
        """
            Sets new employee's social security number
        """
        self.__ssn = new_ssn

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

    @department.setter
    def department(self, new_department: str):
        """
            Sets new employee's department
        """
        self.__department = new_department

    @property
    def position(self) -> str:
        """
            Gets the employee's position
        """
        return self.__position

    @position.setter
    def position(self, new_position: str):
        """
            Sets new employee's position
        """
        self.__position = new_position

    @property
    def start_date(self) -> date:
        """
            Gets the employee's start date
        """
        return self.__start_date

    @start_date.setter
    def start_date(self, new_start_date: date):
        """
            Sets new employee's start date
        """
        self.__start_date = new_start_date

    @property
    def salary(self) -> float:
        """
            Gets the employee's salary
        """
        return self.__salary

    @salary.setter
    def salary(self, new_salary: float):
        """
            Sets new employee's salary
        """
        self.__salary = new_salary


if __name__ == "__main__":
    my_employee = Employee("John Doe",
                           "Warren st., 15/4",
                           12345323,
                           46785874,
                           datetime(1982, 6, 23),
                           "Test department",
                           "Test position",
                           datetime(2020, 3, 9),
                           2340.55)
