def get_objective_details(scoreboard_json, objective):
    objectives = scoreboard_json["data"]["Objectives"]

    objective_info = [o for o in objectives if o["Name"] == objective]

    if not objective_info:
        return None
    return objective_info[0]

def get_objective_leaderboard(scoreboard_json, objective):
    players_list = get_players_list(scoreboard_json)
    players_list = [player['Name'] for player in players_list]

    player_scores = scoreboard_json["data"]["PlayerScores"]
    player_scores = [s for s in player_scores if s["Objective"] == objective and s["Name"] in players_list]

    player_scores.sort(key=lambda score: score["Score"], reverse=True)

    if not player_scores: 
        return None
    return player_scores


def get_players_list(scoreboard_json):
    players_list = []
    tmp_list = []
    player_scores = scoreboard_json["data"]["PlayerScores"]
    for score in player_scores:
        if score['Name'] in tmp_list:
            continue
        players_list.append({ 'Name': score['Name'] })
        tmp_list.append(score['Name'])
    
    players_list = filter(lambda player: not '#' in player['Name'], players_list) # remove fake players

    return list(players_list)

def get_player_scores(scoreboard_json, player):
    scores_list = []
    
    player_scores = scoreboard_json["data"]["PlayerScores"]
    scores_list = filter(lambda score: score["Name"] == player, player_scores)

    return list(scores_list)