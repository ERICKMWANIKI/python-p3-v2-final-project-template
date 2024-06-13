from models.lib.config import conn, cursor

class Game:
    def __init__(self, home_team_id, away_team_id, date, time, location, statistics=None, game_id=None):
        self.id = game_id
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.date = date
        self.time = time
        self.location = location
        self.statistics = statistics or ""

    def __repr__(self):
        return f'<Game {self.home_team_id} vs {self.away_team_id} on {self.date} at {self.time} in {self.location}>'

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS games (
            game_id INTEGER PRIMARY KEY,
            home_team_id INTEGER NOT NULL,
            away_team_id INTEGER NOT NULL,
            date DATE NOT NULL,
            time TIME NOT NULL,
            location TEXT NOT NULL,
            statistics TEXT NOT NULL,
            FOREIGN KEY(home_team_id) REFERENCES teams(team_id),
            FOREIGN KEY(away_team_id) REFERENCES teams(team_id)
        );
        """
        cursor.execute(sql)
        conn.commit()
        print("Table 'games' created successfully.")

    def save(self):
        sql = """
        INSERT INTO games (home_team_id, away_team_id, date, time, location, statistics)
        VALUES (?, ?, ?, ?, ?, ?);
        """
        cursor.execute(
            sql,
            (
                self.home_team_id,
                self.away_team_id,
                self.date,
                self.time,
                self.location,
                self.statistics,
            )
        )
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Game {self.home_team_id} vs {self.away_team_id} added with ID {self.id}")

    @classmethod
    def get_all_games(cls):
        sql = "SELECT * FROM games"
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def get_game_by_id(cls, game_id):
        sql = "SELECT * FROM games WHERE game_id = ?"
        cursor.execute(sql, (game_id,))
        return cursor.fetchone()

    @classmethod
    def get_games_by_date(cls, date):
        sql = "SELECT * FROM games WHERE date = ?"
        cursor.execute(sql, (date,))
        return cursor.fetchall()

    @classmethod
    def get_games_by_team(cls, team_id):
        sql = "SELECT * FROM games WHERE home_team_id = ? OR away_team_id = ?"
        cursor.execute(sql, (team_id, team_id))
        return cursor.fetchall()

    @classmethod
    def update_game(cls, game_id, home_team_id=None, away_team_id=None, date=None, time=None, location=None, statistics=None):
        game = cls.get_game_by_id(game_id)
        if not game:
            print(f"Game with ID {game_id} not found")
            return

        update_fields = []
        params = []

        if home_team_id is not None:
            update_fields.append("home_team_id = ?")
            params.append(home_team_id)
        if away_team_id is not None:
            update_fields.append("away_team_id = ?")
            params.append(away_team_id)
        if date is not None:
            update_fields.append("date = ?")
            params.append(date)
        if time is not None:
            update_fields.append("time = ?")
            params.append(time)
        if location is not None:
            update_fields.append("location = ?")
            params.append(location)
        if statistics is not None:
            update_fields.append("statistics = ?")
            params.append(statistics)

        if update_fields:
            update_query = f"UPDATE games SET {', '.join(update_fields)} WHERE game_id = ?"
            params.append(game_id)
            cursor.execute(update_query, tuple(params))
            conn.commit()
            print(f"Game with ID {game_id} updated successfully")
        else:
            print("No fields to update")

    @classmethod
    def delete_game(cls, game_id):
        sql = "DELETE FROM games WHERE game_id = ?"
        cursor.execute(sql, (game_id,))
        conn.commit()
        print(f"Game with ID {game_id} deleted successfully")