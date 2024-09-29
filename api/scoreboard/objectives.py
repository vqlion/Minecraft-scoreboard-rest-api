from flask import jsonify
from services.auth.auth_guard import auth_guard
from services.nbt.nbt_service import get_nbt_json
from services.nbt.scoreboard_service import get_objective_details, get_objective_leaderboard
from dotenv import load_dotenv
import os

load_dotenv()
SCOREBOARD_PATH = os.getenv('SCOREBOARD_PATH')

def init(app):

    @app.route('/scoreboard/objectives', methods=['GET'])
    @auth_guard()
    def objectives():
        nbt_json = get_nbt_json(SCOREBOARD_PATH)
        objectives = nbt_json["data"]["Objectives"]
        
        return jsonify({"data": objectives, "status": 200}), 200
    
    @app.route('/scoreboard/objectives/<objective>', methods=['GET'])
    @auth_guard()
    def objective_info(objective):
        nbt_json = get_nbt_json(SCOREBOARD_PATH)
        objective_info = get_objective_details(nbt_json, objective)

        if not objective_info:
            return jsonify({"message": "Objective does not exist", "status": 400}), 400
        return jsonify({"data": objective_info, "status": 200}), 200

    @app.route('/scoreboard/objectives/rank/<objective>', methods=['GET'])
    @auth_guard()
    def objective_rank(objective):
        nbt_json = get_nbt_json(SCOREBOARD_PATH)
        ranking = get_objective_leaderboard(nbt_json, objective)

        if not ranking:
            return jsonify({"message": "Objective does not exist or no player is ranked", "status": 400}), 400
        return jsonify({"data": ranking, "status": 200}), 200
