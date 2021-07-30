# Создайте класс с описанием любой компании. К примеру тошиба или глобал
# лоджик. Company.

from datetime import date, datetime
from typing import Tuple


class Company:
    def __init__(
            self,
            company_name: str,
            founded: date,
            headquarters: str,
            founders: Tuple[str, ...],
            ceo: str,
            industry: str
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

    @property
    def company_name(self) -> str:
        """
            Gets the company name value
        """
        return self.__company_name

    @company_name.setter
    def company_name(self, new_company_name: str):
        """
            Sets new company name
        """
        self.__company_name = new_company_name

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

    @headquarters.setter
    def headquarters(self, new_headquarters: str):
        """
            Sets new headquarters
        """
        self.__headquarters = new_headquarters

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

    @ceo.setter
    def ceo(self, new_ceo: str):
        """
            Sets new ceo
        """
        self.__ceo = new_ceo

    @property
    def industry(self):
        """
            Gets the company industry
        """
        return self.__industry

    @industry.setter
    def industry(self, new_industry: str):
        """
            Sets new industry
        """
        self.__industry = new_industry


if __name__ == "__main__":
    telegram = Company('Telegram Messenger LLT',
                       datetime(2019, 4, 2),
                       "London, United Kingdom",
                       ('Pavel Durov', "Nikolai Durov"),
                       "Pavel Durov",
                       "Software")

# Good it is really nice and easy to read such class. But no logic inside class - 1point
# and anyone from global scope could change name of company, industry, and other things
# -2 points
