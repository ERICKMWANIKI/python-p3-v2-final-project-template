from models.lib.config import conn, cursor

class Team:
    def __init__(self, team_name, team_id=None):
        self.id = team_id
        self.team_name = team_name

    def __repr__(self):
        return f"<Team ID: {self.id}, Name: {self.team_name}>"

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS teams (
            team_id INTEGER PRIMARY KEY,
            team_name TEXT NOT NULL UNIQUE
        );
        """
        cursor.execute(sql)
        conn.commit()
        print("Table 'teams' created successfully.")

    def save(self):
        sql = """
        INSERT INTO teams (team_name)
        VALUES (?);
        """
        cursor.execute(sql, (self.team_name,))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Team '{self.team_name}' added with ID {self.id}")

    @classmethod
    def get_all_teams(cls):
        sql = "SELECT * FROM teams"
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def get_team_by_id(cls, team_id):
        sql = "SELECT * FROM teams WHERE team_id = ?"
        cursor.execute(sql, (team_id,))
        return cursor.fetchone()

    @classmethod
    def get_team_by_name(cls, team_name):
        sql = "SELECT * FROM teams WHERE team_name = ?"
        cursor.execute(sql, (team_name,))
        return cursor.fetchone()

    @classmethod
    def update_team(cls, team_id, new_team_name=None):
        team = cls.get_team_by_id(team_id)
        if not team:
            print(f"Team with ID {team_id} not found")
            return

        if new_team_name is not None:
            sql = "UPDATE teams SET team_name = ? WHERE team_id = ?"
            cursor.execute(sql, (new_team_name, team_id))
            conn.commit()
            print(f"Team ID {team_id} updated to name '{new_team_name}'")
        else:
            print("No new team name provided for update")

    @classmethod
    def delete_team(cls, team_id):
        team = cls.get_team_by_id(team_id)
        if not team:
            print(f"Team with ID {team_id} not found")
            return

        sql = "DELETE FROM teams WHERE team_id = ?"
        cursor.execute(sql, (team_id,))
        conn.commit()
        print(f"Team with ID {team_id} deleted successfully")