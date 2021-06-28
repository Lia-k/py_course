# У вас есть 2 компании с людьми. Одна из компаний пусть будет это global_logic
# была поглощена компанией toshiba. Отобразите это в коде. Учитывайте что люди
# с одинаковыми именами могут быть в обеих компаниях

global_logic = [
    "John Doe",
    "Marta Doe",
    "Aamir khan",
    "Abhinav Shukla",
    "Abhishek Bachchan",
    "Ajay Devgan"
]
toshiba = [
    "Shinji Ikari",
    "Misato Katsuragi",
    "Rei Ayanami",
    "Asuka Langley Soryu",
    "Ritsuko Akagi",
    "Kozo Fuyutsuki",
    "Ryoji Kaji",
    "Makoto Hyuga",
    "John Doe"
]
toshiba.extend(global_logic)
# print(toshiba)
# Good but I think that some ot employees in this case still stay as employees of global logic so I suppose you should fire them from global logic company
# global_logic.clear()