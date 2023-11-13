class IteratorTeam:
    def __init__(self):
        self.team = Team()
        self.juniors_iter = iter(self.team.juniors)
        self.seniors_iter = iter(self.team.seniors)

    def __next__(self):
        try:
            return next(self.juniors_iter)
        except StopIteration:
            # Якщо juniors закінчуються, переходимо до seniors
            return next(self.seniors_iter)

class Team:
    def __init__(self):
        self.juniors = ["JPlayer 1", "JPlayer 2", "JPlayer 3", "JPlayer 4"]
        self.seniors = ["Player 1", "Player 2", "Player 3"]

    def __iter__(self):
        return IteratorTeam()

for x in Team():
    print(x)