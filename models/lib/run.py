from players import Player
from games import Game
from team import Team
from statistics import Statistics


Player.create_table()

Game.create_table()

Statistics.create_table()

Team.create_table()
    


# Adding players
player1 = Player(first_name="John", last_name="Doe", jersey_number=10, contact_details="john.doe@example.com", team_id=1)
player1.save()
    
player2 = Player(first_name="Jane", last_name="Smith", jersey_number=11, contact_details="jane.smith@example.com", team_id=1)
player2.save()

# Adding a game
game1 = Game(home_team_id=1, away_team_id=2, date="2023-06-10", time="15:00", location="Stadium A")
game1.save()

 # Adding a statistic
stat1 = Statistics(player_id=1, game_id=1, points_scored=20, rebounds=10, assists=5, blocks=2)
stat1.save()

# Adding a team
team1 = Team(team_name="Team A")
team1.save()

# Updating a game
Game.update_game(1, home_team_id=2, location="Stadium B")

# Updating a statistic
Statistics.update_statistic(1, points_scored=25, assists=7)

# Updating a team's name
Team.update_team(1, new_team_name="Updated Team A")

# Deleting a statistic
Statistics.delete_statistic(1)

# Deleting a game
Game.delete_game(1)

# Deleting a team
Team.delete_team(1)