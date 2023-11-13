# def singleton(orig_cls):
#     orig_cls = orig_cls.__new__
#     instance = None
#
#     def __new__(cls, *args, **kwargs):
#         nonlocal instance
#         if instance is None:
#             instance = orig_cls(cls, *args, **kwargs)
#         return instance
#     orig_cls.__new__ = __new__
#     return orig_cls
# @singleton
# class Logger:
#     def log(msg):
#         print(msg)
#
# Logger - singleton()

class IteratorTeam:
    def __init__(self):
        self.team = Team()
        self.i = 0

    def __next__(self):
        if self.i < len(self.team.juniors):
            x = self.i
            self.i += 1
            return self.team.juniors[x]
        else:
            raise StopIteration

class Team:
    def __init__(self):
        self.juniors = ["JPlayer 1", "JPlayer 2", "JPlayer 3", "JPlayer4"]
        self.seniors = ["Player 1", "Player 2", "Player 3"]

    def __iter__(self):
        return IteratorTeam

for x in Team():
    print(x)