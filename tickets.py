from rich import print
from rich.panel import Panel
from rich import inspect

class Gamer:

    def __init__(self, name, nick):
        self.name = name
        self.nick = nick
        self.favourites = list()

    def add_favourite(self, game):
        self.favourites.append(game)
        self.favourites.sort(key=str.lower)

    def ticket(self):
        content = f"Name: [black on blue]{self.name}[/black on blue]"
        content += f"\nFavourite Games:"

        for num, game in enumerate(self.favourites):
            content += f"\n:video_game: {game}"

        panel = Panel(content, title=f"Player <{self.nick}>", width=40)
        print(panel)

p1 = Gamer("Luiz Tramontini", "luizw")
p1.add_favourite("The Legend of Zelda: Breath of the Wild")
p1.add_favourite("Hollow Knight")
p1.add_favourite("Celeste")
p1.ticket()

p2 = Gamer("Little John", "johnny123")
p2.add_favourite("Game of Thrones")
p2.add_favourite("The Witcher 3: Wild Hunt")
p2.add_favourite("Red Dead Redemption 2")
p2.ticket()