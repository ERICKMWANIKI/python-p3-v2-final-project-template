from models.lib.config import conn, cursor

class Player:
    def __init__(
        self, first_name, last_name, jersey_number, contact_details, team_id, id=None
    ):
        self.id =id
        self.first_name = first_name
        self.last_name = last_name
        self.jersey_number = jersey_number
        self.contact_details = contact_details
        self.team_id = team_id

    def __repr__(self):
        return f'<player {self.first_name} {self.last_name} {self.jersey_number} {self.contact_details} {self.team_id}>'

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            jersey_number INTEGER,
            contact_details STRING,
            team_id INTEGER
            )
        """

        cursor.execute(sql)
        conn.commit()
    
    def save (self):
        sql = """
            INSERT INTO players (
            first_name,
            last_name,
            jersey_number,
            contact_details,
            team_id
            )
            VALUES(?, ?, ?, ?, ?);
        """

        cursor.execute(
            sql,
            (
                self.first_name,
                self.last_name,
                self.jersey_number,
                self.contact_details,
                self.team_id,
            )
        )
        conn.commit()

        self.id = cursor.lastrowid
        print(f"Player {self.first_name} {self.last_name} added with ID {self.id}")

    @classmethod
    def get_all_players(cls):
        sql = "SELECT * FROM players"
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def get_player_by_id(cls, player_id):
        sql = "SELECT * FROM players WHERE player_id = ?"
        cursor.execute(sql, (player_id,))
        return cursor.fetchone()

    @classmethod
    def get_player_by_first_name(cls, first_name):
        sql = "SELECT * FROM players WHERE first_name = ?"
        cursor.execute(sql, (first_name,))
        return cursor.fetchall()

    @classmethod
    def get_players_of_a_team(cls, team_id):
        sql = "SELECT * FROM players WHERE team_id = ?"
        cursor.execute(sql, (team_id,))
        return cursor.fetchall()

    @classmethod
    def update_player(cls, player_id, first_name=None, last_name=None, jersey_number=None, contact_details=None, team_id=None):
        player = cls.get_player_by_id(player_id)
        if player:
            update_fields = []
            params = []

            if first_name:
                update_fields.append("first_name = ?")
                params.append(first_name)
            if last_name:
                update_fields.append("last_name = ?")
                params.append(last_name)
            if jersey_number:
                update_fields.append("jersey_number = ?")
                params.append(jersey_number)
            if contact_details:
                update_fields.append("contact_details = ?")
                params.append(contact_details)
            if team_id:
                update_fields.append("team_id = ?")
                params.append(team_id)

            if update_fields:
                update_query = f"UPDATE players SET {', '.join(update_fields)} WHERE player_id = ?"
                params.append(player_id)

                cursor.execute(update_query, tuple(params))
                conn.commit()
                print(f"Player with ID {player_id} updated successfully")
            else:
                print("No fields to update")
        else:
            print(f"Player with ID {player_id} not found")

    @classmethod
    def delete_player(cls, player_id):
        player = cls.get_player_by_id(player_id)
        if player:
            cursor.execute("DELETE FROM players WHERE player_id = ?", (player_id,))
            conn.commit()
            print(f"Player with ID {player_id} deleted successfully")
        else:
            print(f"Player with ID {player_id} not found")    
        
