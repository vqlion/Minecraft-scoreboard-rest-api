from api.scoreboard.objectives import init as init_objectives
from api.scoreboard.players import init as init_players

def init(app):
    init_objectives(app)
    init_players(app)