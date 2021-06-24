# У вас есть две группы людей. В одной группе состоят всеядные люди в другой
# лишь вегетарианцы. Всеядный является вегетарианцем но вегетарианец не
# является всеядным. Вывести список гостей которые могут есть овощи и зелень.

omnivore = ["Prince William", "Russell Crowe", "Catherine Zeta-Jones",
            "Kate Moss"]
vegan = ["Daniel Negreanu", "Phil Ivey", "Phil Hellmuth", "Patrik Antonius"]
veg_and_salad = list(set(omnivore).union(set(vegan)))
print(veg_and_salad)
