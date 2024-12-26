# VeeObjectives API

Rest API for minecraft scoreboard based on world save 

## Usage 

This API is meant to be installed alongside a Minecraft server. It allows access to the players scoreboard (objectives tracking in Minecraft).

### Installation

Copy the `.env.example` file into a `.env` and fill the details. The `SCOREBOARD_PATH` is the path of the scoreboard file in your world's save. This is the file used by the API to get the players' rankings.

Install the dependencies and launch the API:

```bash
pip install -r requirements.txt
python app.py
```

I recommend using the app with nginx or apache for a proper configuration.

## API reference

All routes are `GET` routes.

### /scoreboard/players

Get a list of the players that have played on the server (and have an entry on the scoreboard).

Returns: `List<Player>`

```
Name: String //name of the player
```

### /scoreboard/players/scores/\<player\>

Get the list of tracked scores for a given player. If the player doesn't exist, returns an empty list 

Returns: `List<PlayerScore>` (refer to [NBT format](https://minecraft.wiki/w/Scoreboard#NBT_format))

```
Locked: Int
Name: String //name of the player
Objective: String //name of the objective (matches "Name" attribute of Objective)
Score: Int
```

### /scoreboard/objectives

Get the list of tracked objectives.

Returns: `List<Objective>` (refer to [NBT format](https://minecraft.wiki/w/Scoreboard#NBT_format))

```
CriteriaName: String
DisplayName: String
Name: String
RenderType: Int
display_auto_update: Int
```

### /scoreboard/objectives/\<objective\>

Get information about a specific tracked objective. If it doesn't exist returns "Objective doesn't exist"

Returns: `Objective` (refer to [NBT format](https://minecraft.wiki/w/Scoreboard#NBT_format))

```
CriteriaName: String
DisplayName: String
Name: String
RenderType: Int
display_auto_update: Int
```

### /scoreboard/objectives/rank/\<objective\>

Get the leaderboard for an objective. Players are ranked by their scores, descending.

Returns: `List<PlayerScore>` (refer to [NBT format](https://minecraft.wiki/w/Scoreboard#NBT_format))

```
Locked: Int
Name: String //name of the player
Objective: String //name of the objective (matches "Name" attribute of Objective)
Score: Int
```
