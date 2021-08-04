# Реализовать фабричный метод паттерн проектирования на примере браузера.
from abc import ABC, abstractmethod


class Application(ABC):

    @abstractmethod
    def run(self):
        pass


class GoogleChrome(Application):
    def run(self):
        return "Open Google Chrome."


class FireFox(Application):
    def run(self):
        return "Open FireFox."


class Tor(Application):
    def run(self):
        return "Open Tor."


class GoOnline(ABC):
    @abstractmethod
    def use_browser(self, parameter):
        pass


class BrowseInternet(GoOnline):
    def use_browser(self, browser_name):
        if browser_name == 'GoogleChrome':
            return GoogleChrome()
        elif browser_name == "Firefox":
            return FireFox()
        elif browser_name == "Tor":
            return Tor()


if __name__ == "__main__":
    browser = BrowseInternet()
    print(browser.use_browser('GoogleChrome').run())
    print(browser.use_browser('Firefox').run())
    print(browser.use_browser('Tor').run())
