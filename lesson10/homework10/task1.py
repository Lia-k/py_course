# Создайте класс с описанием любой компании. К примеру тошиба или глобал
# лоджик. Company.

from datetime import date, datetime
from typing import Tuple, Union, List


class Company:
    def __init__(
            self,
            company_name: str,
            founded: date,
            headquarters: str,
            founders: Tuple[str, ...],
            ceo: str,
            industry: str,
            staff: List[str]
    ):
        """
            Initializes attributes that describe company
        """
        self.__company_name = company_name
        self.__founded = founded
        self.__headquarters = headquarters
        self.__founders = founders
        self.__ceo = ceo
        self.__industry = industry
        self.__staff = staff

    @property
    def company_name(self) -> str:
        """
            Gets the company name value
        """
        return self.__company_name

    @property
    def founded(self) -> date:
        """
            Gets the company foundation date value
        """
        return self.__founded

    @property
    def headquarters(self) -> str:
        """
            Gets the company headquarters value
        """
        return self.__headquarters

    @property
    def founders(self) -> Tuple[str, ...]:
        """
            Gets the company founders names
        """
        return self.__founders

    @property
    def ceo(self) -> str:
        """
            Gets the company ceo name
        """
        return self.__ceo

    @property
    def industry(self):
        """
            Gets the company industry
        """
        return self.__industry

    @property
    def staff(self):
        """
            Gets the company industry
        """
        return self.__staff

    def hire_new_staff(self, hired_employee: str) -> Union[int, str]:
        if hired_employee in self.staff:
            return "No such employee"
        else:
            self.staff.append(hired_employee)
            return len(self.staff)

    def fire_staff(self, fired_employee: str) -> Union[int, str]:
        if fired_employee in self.staff:
            self.staff.remove(fired_employee)
            return len(self.staff)
        else:
            return "No such employee"


if __name__ == "__main__":
    telegram = Company('Telegram Messenger LLT',
                       datetime(2019, 4, 2),
                       "London, United Kingdom",
                       ('Pavel Durov', "Nikolai Durov"),
                       "Pavel Durov",
                       "Software",
                       ["Test1", "Test2", "Test3"])
