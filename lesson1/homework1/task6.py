# 6. Создать список с именами людей, в нем должны повторяться некоторые имена. Превратите список с повторяющимися именами в список
# уникальных имен используя множества.
names = [
    "Tom",
    "Viktor",
    "Andrew",
    "Jennifer",
    "Troy",
    "Jessica",
    "Andrew",
    "Viktor",
    "Jessica",
]
unique_names = list(set(names))

if __name__ == "__main__":
    print(
        unique_names
    )  # printing of unique value is not needed according to task requirements
# Good but no new line in the end od file
