class Valentine:
    def __init__(self, neighbour):
        self.neighbour = [int(el) for el in neighbour]

        self.index = 0
        self.jump = 0
        self.end_flag = False
        self.house_count = 0

    def cupid(self):

        while True:
            jump_command = input().split(" ")
            self.jump = int(jump_command[1]) + self.index if not jump_command[0] == "Love!" else bool
            if not type(self.jump) == int:
                break
            if self.jump >= len(self.neighbour):
                self.index = 0
            else:
                self.index = self.jump
            if self.neighbour[self.index] == 0:
                print(f"Place {self.index} already had Valentine's day.")
            else:
                self.neighbour[self.index] -= 2
                if self.neighbour[self.index] == 0:
                    print(f"Place {self.index} has Valentine's day.")

        print(f"Cupid's last position was {self.index}.")
        if sum(self.neighbour) == 0:
            print(f"Mission was successful.")
        else:
            self.house_count = len([el for el in self.neighbour if not el == 0])
            print(f"Cupid has failed {self.house_count} places.")


neighborhood = Valentine(input().split("@"))
neighborhood.cupid()
