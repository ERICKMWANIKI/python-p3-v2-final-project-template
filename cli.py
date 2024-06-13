from models.lib.config import conn, cursor
from models.lib.players import Player  # Assuming the Player class is defined in player.py
from models.lib.team import Team  # Assuming the Team class is defined in team.py
from models.lib.games import Game  # Assuming the Game class is defined in game.py
from models.lib.statistics import Statistics  # Assuming the Statistics class is defined in statistics.py

def create_tables():
    """Create the necessary tables in the database."""
    Player.create_table()
    Team.create_table()
    Game.create_table()
    Statistics.create_table()
    print("All tables created successfully.")

def exit_program():
    """Exit the program."""
    print("Exiting the program.")
    conn.close()
    exit()

def add_a_player():
    """Add a new player."""
    first_name = input("Enter player's first name: ")
    last_name = input("Enter player's last name: ")
    jersey_number = input("Enter player's jersey number: ")
    contact_details = input("Enter player's contact details: ")
    team_id = input("Enter player's team ID: ")

    player = Player(first_name, last_name, jersey_number, contact_details, team_id)
    player.save()

def list_of_players():
    """List all players."""
    players = Player.get_all_players()
    for player in players:
        print(player)

def get_player_by_player_id():
    """Get player by ID."""
    player_id = input("Enter player ID: ")
    player = Player.get_player_by_id(int(player_id))
    print(player)

def get_a_player_by_player_first_name():
    """Get player by first name."""
    first_name = input("Enter player first name: ")
    players = Player.get_player_by_first_name(first_name)
    for player in players:
        print(player)

def list_of_players_of_a_team():
    """List players of a team."""
    team_id = input("Enter team ID: ")
    players = Player.get_players_of_a_team(int(team_id))
    for player in players:
        print(player)

def update_player_details():
    """Update player details."""
    player_id = input("Enter player ID: ")
    Player.update_player(int(player_id))

def delete_a_player():
    """Delete a player."""
    player_id = input("Enter player ID: ")
    Player.delete_player(int(player_id))

def add_a_team():
    """Add a new team."""
    team_name = input("Enter team name: ")
    team = Team(team_name)
    team.save()

def list_of_teams():
    """List all teams."""
    teams = Team.get_all_teams()
    for team in teams:
        print(team)

def list_team_by_id():
    """Get team by ID."""
    team_id = input("Enter team ID: ")
    team = Team.get_team_by_id(int(team_id))
    print(team)

def list_team_by_name():
    """Get team by name."""
    team_name = input("Enter team name: ")
    team = Team.get_team_by_name(team_name)
    print(team)

def update_a_team():
    """Update team details."""
    team_id = input("Enter team ID: ")
    Team.update_team(int(team_id))

def delete_a_team():
    """Delete a team."""
    team_id = input("Enter team ID: ")
    Team.delete_team(int(team_id))

def create_a_new_game():
    """Create a new game."""
    home_team_id = input("Enter home team ID: ")
    away_team_id = input("Enter away team ID: ")
    date = input("Enter game date (YYYY-MM-DD): ")
    time = input("Enter game time (HH:MM): ")
    location = input("Enter game location: ")

    game = Game(home_team_id, away_team_id, date, time, location)
    game.save()

def list_of_games():
    """List all games."""
    games = Game.get_all_games()
    for game in games:
        print(game)

def list_game_by_id():
    """Get game by ID."""
    game_id = input("Enter game ID: ")
    game = Game.get_game_by_id(int(game_id))
    print(game)

def list_games_by_date():
    """Get games by date."""
    date = input("Enter game date (YYYY-MM-DD): ")
    games = Game.get_games_by_date(date)
    for game in games:
        print(game)

def list_games_by_team_id():
    """Get games by team ID."""
    team_id = input("Enter team ID: ")
    games = Game.get_games_by_team(int(team_id))
    for game in games:
        print(game)

def update_a_game():
    """Update game details."""
    game_id = input("Enter game ID: ")
    Game.update_game(int(game_id))

def delete_a_game():
    """Delete a game."""
    game_id = input("Enter game ID: ")
    Game.delete_game(int(game_id))

def create_statistic():
    """Create a new statistic."""
    player_id = input("Enter player ID: ")
    game_id = input("Enter game ID: ")
    points_scored = input("Enter points scored: ")
    rebounds = input("Enter rebounds: ")
    assists = input("Enter assists: ")
    blocks = input("Enter blocks: ")

    stat = Statistics(player_id, game_id, int(points_scored), int(rebounds), int(assists), int(blocks))
    stat.save()

def list_all_statistics():
    """List all statistics."""
    stats = Statistics.get_all_statistics()
    for stat in stats:
        print(stat)

def list_stat_by_id():
    """Get statistic by ID."""
    stat_id = input("Enter stat ID: ")
    stat = Statistics.get_statistic_by_id(int(stat_id))
    print(stat)

def list_player_stats():
    """Get statistics of a player."""
    player_id = input("Enter player ID: ")
    stats = Statistics.get_player_statistics(int(player_id))
    for stat in stats:
        print(stat)

def list_game_stats():
    """Get statistics of a game."""
    game_id = input("Enter game ID: ")
    stats = Statistics.get_game_statistics(int(game_id))
    for stat in stats:
        print(stat)

def list_highest_stat_of_a_field():
    """Get the highest statistic by a specific field."""
    field = input("Enter the field (points_scored, rebounds, assists, blocks): ")
    stats = Statistics.get_stat_with_highest(field)
    for stat in stats:
        print(stat)

def list_lowest_stat_of_a_field():
    """Get the lowest statistic by a specific field."""
    field = input("Enter the field (points_scored, rebounds, assists, blocks): ")
    stats = Statistics.get_stat_with_lowest(field)
    for stat in stats:
        print(stat)

def update_stat():
    """Update a statistic."""
    stat_id = input("Enter stat ID: ")
    Statistics.update_statistic(int(stat_id))

def delete_stat():
    """Delete a statistic."""
    stat_id = input("Enter stat ID: ")
    Statistics.delete_statistic(int(stat_id))

def menu():
    print("Please select an option:")
    print("0. Exit Program!!!")
    print("*************************Players Menu************************")
    print("1. Add a Player")
    print("2. List all Players")
    print("3. Get Player by ID")
    print("4: Get player by First Name")
    print("5: List of Players in a Team")
    print("6: Update Player details")
    print("7. Delete a Player")
    print("**************************Teams Menu*************************")
    print("8. Add a Team")
    print("9. List all teams")
    print("10: Get a Team by ID")
    print("11: Get a team by Name")
    print("12: Update Team details")
    print("13: Delete a Team")
    print("*************************Games Menu**************************")
    print("14: Add a Game ")
    print("15. List all Games")
    print("16: Get game by ID")
    print("17: Get game by date")
    print("18: Get game by team")
    print("19: Update Game details")
    print("20: Delete a game")
    print("***********************Statistics Menu***********************")
    print("21: Add a Statistic")
    print("22: List all statistics")
    print("23: Get a stat by ID")
    print("24: Get the stats of a Player")
    print("25: Get the stats of a Game")
    print("26: Get the highest stats by a field")
    print("27: Get the least stats by a field")
    print("28: Update a Stat Details")
    print("29: Delete a Stat")

def main():
    create_tables()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_a_player()
        elif choice == "2":
            list_of_players()
        elif choice == "3":
            get_player_by_player_id()
        elif choice == "4":
            get_a_player_by_player_first_name()
        elif choice == "5":
            list_of_players_of_a_team()
        elif choice == "6":
            update_player_details()
        elif choice == "7":
            delete_a_player()
        elif choice == "8":
            add_a_team()
        elif choice == "9":
            list_of_teams()
        # elif choice == "10":
        #     list_team_by

if __name__ == "__main__":
    main()