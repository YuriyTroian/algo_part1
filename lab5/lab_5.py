class RaceHorse:
    def __init__(self, speed, age, name, prize_racing, hp = 100):
        self.speed = speed
        self.age = age
        self.name = name
        self.prize_racing = prize_racing
        self.hp = hp
        self.placeInRace = 0

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Speed: {self.speed}"

class Anabolic:
    def __init__(self, name_anabolic, speed_plus_anabolic, cost_anabolic, hp_minus_anabolic):
        self.name_anabolic = name_anabolic
        self.speed_plus_anabolic = speed_plus_anabolic
        self.cost_anabolic = cost_anabolic
        self.hp_minus_anabolic = hp_minus_anabolic

    def __str__(self):
        return f"Name anabolic:{self.name_anabolic}, Speed plus anabolic:{self.speed_plus_anabolic},"\
               f"Cost anabolic:{self.cost_anabolic}, HP:{self.hp_minus_anabolic}"

class Race:
    def __init__(self):
        self.participants = []
        self.anabolic_for_racer = []

    def add_racer(self, member):
        if isinstance(member, RaceHorse):
            if 3 <= member.age <= 7:
                self.participants.append(member)
                print(f"Added racer -> {member}")
            else:
                print(f"Неможливо додати учасника: {member} через вікові обмеження ")
        else:
            raise TypeError("Учасника не знайдено")

    def remove_racer(self, member):
        if isinstance(member, RaceHorse):
            self.participants.remove(member)
            print(f"Removed racer: {member}")
        else:
            raise TypeError("Учасника не знайдено")

    def find_anabolic(self, anabolic, member):
        if member.hp - anabolic.hp_minus_anabolic > 0 and anabolic.cost_anabolic <= member.prize_racing * 0.5:
            speed_with_anabolic = member.speed + anabolic.speed_plus_anabolic
            self.anabolic_for_racer.append((anabolic, speed_with_anabolic))
            print(f"Анаболік {anabolic.name_anabolic} підходить для {member.name}")
        else:
            print(f"Анаболік {anabolic.name_anabolic} не підходить для {member.name}")



    def select_anabolic(self):
        sorted_anabolics_speed = sorted(self.anabolic_for_racer,
                                  key=lambda x: x[1], reverse=True)
        print(f"Посортовані анаболіки за швидкістю:")
        for anabolic, speed_with in sorted_anabolics_speed:
            print(f"\t{anabolic}, Speed with anabolic: {speed_with}")
        if sorted_anabolics_speed:
            best_anabolic, best_speed = sorted_anabolics_speed[0]
            print(f"Анаболік {best_anabolic.name_anabolic} забезпечить найбільшу швидкість для {member.name}")
            member.speed = best_speed
            member.hp = member.hp - best_anabolic.hp_minus_anabolic
            print(f"{member.name} speed with anabolic -> {member.speed}, HP with-> {member.hp}")

        else:
            print("СПИСОК ПОРОЖНІЙ")



    def find_winner(self):
        sorted_participants = sorted(
            self.participants,
            key=lambda participant: participant.speed + abs(
                (sum(p.age for p in self.participants) / len(self.participants)) - participant.age
            ),
            reverse=True
        )
        for index, participant in enumerate(sorted_participants[:3]):
            participant.placeInRace = index + 1

        print("Sorted places:")
        for participant in sorted_participants:
            print(f"\t{participant}, Place in Race: {participant.placeInRace}")
        print(f"Member {sorted_participants[0]} - winner")

    def sort_speed(self):
        sorted_participants_speed = sorted(
            self.participants, key=lambda participant: participant.speed
        )
        print("Sorted participants_speed:")
        for participant in sorted_participants_speed:
            print(f"\t{participant}")


racers = [  RaceHorse(60, 5,"Joy", 30),
            RaceHorse(20, 7, "Kish", 40),
            RaceHorse(30, 4, "Kur", 60),
            RaceHorse(40, 2, "Git", 70),
            RaceHorse(50, 17, "Adzara",  80)
            ]
anabolics = [ Anabolic("One", 10, 15, 75),
              Anabolic("Two", 20, 20, 90),
              Anabolic("Three", 30, 30, 93),
              Anabolic("Four", 40, 35, 95),
              Anabolic("Five", 50, 40, 99)
              ]


if __name__ == "__main__":
    race = Race()



for member in racers:
    race.add_racer(member)

for member in race.participants:
    race.anabolic_for_racer.clear()
    for anabolic in anabolics:
        race.find_anabolic(anabolic, member)

    race.select_anabolic()

race.find_winner()
race.sort_speed()






    # member.speed += anabolic.speed_plus_anabolic
    # sorted_anabolics = sorted(race.anabolic_for_racer, key=lambda x: (member.speed + anabolic.speed_plus_anabolic))
    # race.select_anabolic(member)
    #
    # member.hp -= anabolic.hp_minus_anabolic
    # print(f"member_speed with anabolic -> {member.speed}, HP with-> {member.hp}")










