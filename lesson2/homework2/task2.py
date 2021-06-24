# У вас есть 3 группы людей bingo_blacklist, poker_blacklist,
# mahjong_blacklist.Имена людей в формате "John Dow" первое и второе имя.
# Найти тех кто состоит во всех черных списках.

bingo_blacklist = {
    "Prince William",
    "Russell Crowe",
    "Catherine Zeta-Jones",
    "Kate Moss"
}
poker_blacklist = {
    "Daniel Negreanu",
    "Phil Ivey",
    "Phil Hellmuth",
    "Patrik Antonius",
    "Russell Crowe",
    "Catherine Zeta-Jones",
    "Kate Moss"
}
mahjong_blacklist = {
    "Mai Hatsune",
    "Prince William",
    "Russell Crowe",
    "Catherine Zeta-Jones",
    "Phil Ivey",
    "Phil Hellmuth",
    "Zhou Yong"
}

all_blacklist = bingo_blacklist.intersection(
    poker_blacklist, mahjong_blacklist
)
# print(all_blacklist)

# Good. Take a look how I have reformat the code. It is easy to read.
# try to install black formatter it will help you format code automatically
