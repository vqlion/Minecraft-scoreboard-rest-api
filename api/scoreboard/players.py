from flask import jsonify
from services.nbt.nbt_service import get_nbt_json
from services.nbt.scoreboard_service import get_players_list, get_player_scores
from dotenv import load_dotenv
import os

load_dotenv()
SCOREBOARD_PATH = os.getenv('SCOREBOARD_PATH')

def init(app):

    @app.route('/scoreboard/players', methods=['GET'])
    def get_players():
        nbt_json = get_nbt_json(SCOREBOARD_PATH)
        players_list = get_players_list(nbt_json)

        return jsonify({"data": players_list, "status": 200}), 200

    @app.route('/scoreboard/players/scores/<player>', methods=['GET'])
    def get_scores(player):
        nbt_json = get_nbt_json(SCOREBOARD_PATH)
        player_scores = get_player_scores(nbt_json, player)

        return jsonify({"data": player_scores, "status": 200}), 200