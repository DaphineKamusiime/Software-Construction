
#implement manager class with  bonus calculation

class Manager(Employee):
    def calculate_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")
