class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        ll = [f'Name: {self.name}', f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
        for skill in self.skills:
            ll.append(f"==={skill} - {self.skills[skill]}")

        return '\n'.join(str(x) for x in ll)