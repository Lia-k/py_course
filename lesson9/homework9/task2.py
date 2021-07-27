# Реализовать функцию которая возвращает дату недельной давности от текущего
# момента времени.
import datetime


def week_counter():
    """
        Returns a week ago date from current time
    """
    current_date = datetime.datetime.today()
    week_interval = datetime.timedelta(days=7)
    past_date = current_date - week_interval
    return past_date.strftime("%Y-%m-%d")
