from flask import jsonify
from services.nbt.nbt_service import get_nbt_json
from services.nbt.scoreboard_service import get_objective_details, get_objective_leaderboard
from dotenv import load_dotenv
import os

load_dotenv()
SCOREBOARD_PATH = os.getenv('SCOREBOARD_PATH')

def init(app):

    @app.route('/scoreboard/objectives', methods=['GET'])
    def objectives():
        nbt_json = get_nbt_json(SCOREBOARD_PATH)
        objectives = nbt_json["data"]["Objectives"]

        objectives = [o for o in objectives if o["CriteriaName"] != "dummy"]
        
        return jsonify(objectives), 200
    
    @app.route('/scoreboard/objectives/<objective>', methods=['GET'])
    def objective_info(objective):
        nbt_json = get_nbt_json(SCOREBOARD_PATH)
        objective_info = get_objective_details(nbt_json, objective)

        if not objective_info:
            return jsonify("Objective does not exist"), 400
        return jsonify(objective_info), 200

    @app.route('/scoreboard/objectives/rank/<objective>', methods=['GET'])
    def objective_rank(objective):
        nbt_json = get_nbt_json(SCOREBOARD_PATH)
        ranking = get_objective_leaderboard(nbt_json, objective)

        if not ranking:
            return jsonify("Objective does not exist or no player is ranked"), 400
        return jsonify(ranking), 200
