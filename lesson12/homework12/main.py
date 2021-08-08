from lesson12.homework12.metahuman import MetaHuman

if __name__ == "__main__":
    super_man = MetaHuman("Clark Kent",
                          38,
                          55,
                          102,
                          1.8,
                          "no chronic illness",
                          True,
                          "alien",
                          100,
                          True,
                          False,
                          "x-ray vision, cold breath, invulnerability",
                          "kryptonians",
                          100,
                          "Superman",
                          "wearing glasses")

    print(super_man.super_hero_name)
    print(super_man.disguise)
    print(super_man.hide_identity())
    print(super_man.live())
    print(super_man.work("reporter"))
    print(super_man.run(55))
    print(super_man.die())
    print(super_man.increase_strength(60))
    print(super_man.use_ability("help people"))


