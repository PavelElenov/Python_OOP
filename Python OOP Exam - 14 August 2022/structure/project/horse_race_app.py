from project.horse_specification.appaloosa import Appaloosa

from project.horse_specification.thoroughbred import Thoroughbred

from project.jockey import Jockey

from project.horse_race import HorseRace


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def find_horse(self, horse_type_):
        for horse in reversed(self.horses):
            if type(horse).__name__ == horse_type_ and not horse.is_taken:
                return horse
        raise Exception(f"Horse breed {horse_type_} could not be found!")

    def find_jockey(self, jockey_name_):
        for jockey in self.jockeys:
            if jockey.name == jockey_name_:
                return jockey
        raise Exception(f"Jockey {jockey_name_} could not be found!")

    def find_race(self, race_type_):
        for race in self.horse_races:
            if race.race_type == race_type_:
                return race
        raise Exception(f"Race {race_type_} could not be found!")

    def add_horse(self, horse_type, horse_name, horse_speed):
        if horse_name in [horse.name for horse in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in ['Appaloosa', 'Thoroughbred']:
            if horse_type == 'Appaloosa':
                horse = Appaloosa(horse_name, horse_speed)
            else:
                horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        if jockey_name in [jockey.name for jockey in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        if race_type in [race.race_type for race in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        jockey = self.find_jockey(jockey_name)
        horse = self.find_horse(horse_type)

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        race = self.find_race(race_type)
        jockey = self.find_jockey(jockey_name)

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        race = self.find_race(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        best_jockey = sorted(race.jockeys, key=lambda jockey: -jockey.horse.speed)[0]
        return f"The winner of the {race_type} race, with a speed of {best_jockey.horse.speed}km/h is " \
               f"{best_jockey.name}! Winner's horse: {best_jockey.horse.name}."
