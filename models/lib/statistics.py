from models.lib.config import conn, cursor

class Statistics:
    def __init__(self, player_id, game_id, points_scored=0, rebounds=0, assists=0, blocks=0, stat_id=None):
        self.id = stat_id
        self.player_id = player_id
        self.game_id = game_id
        self.points_scored = points_scored
        self.rebounds = rebounds
        self.assists = assists
        self.blocks = blocks

    def __repr__(self):
        return f"<Statistics PlayerID: {self.player_id}, GameID: {self.game_id}, Points: {self.points_scored}, Rebounds: {self.rebounds}, Assists: {self.assists}, Blocks: {self.blocks}>"

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS statistics (
            stat_id INTEGER PRIMARY KEY,
            player_id INTEGER NOT NULL,
            game_id INTEGER NOT NULL,
            points_scored INTEGER DEFAULT 0,
            rebounds INTEGER DEFAULT 0,
            assists INTEGER DEFAULT 0,
            blocks INTEGER DEFAULT 0,
            UNIQUE(player_id, game_id),
            FOREIGN KEY(player_id) REFERENCES players(player_id),
            FOREIGN KEY(game_id) REFERENCES games(game_id)
        );
        """
        cursor.execute(sql)
        conn.commit()
        print("Table 'statistics' created successfully.")

    def save(self):
        sql = """
        INSERT INTO statistics (player_id, game_id, points_scored, rebounds, assists, blocks)
        VALUES (?, ?, ?, ?, ?, ?);
        """
        cursor.execute(
            sql,
            (
                self.player_id,
                self.game_id,
                self.points_scored,
                self.rebounds,
                self.assists,
                self.blocks
            )
        )
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Statistics for Player {self.player_id} in Game {self.game_id} added with ID {self.id}")

    @classmethod
    def get_all_statistics(cls):
        sql = "SELECT * FROM statistics"
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def get_statistic_by_id(cls, stat_id):
        sql = "SELECT * FROM statistics WHERE stat_id = ?"
        cursor.execute(sql, (stat_id,))
        return cursor.fetchone()

    @classmethod
    def get_player_statistics(cls, player_id):
        sql = "SELECT * FROM statistics WHERE player_id = ?"
        cursor.execute(sql, (player_id,))
        return cursor.fetchall()

    @classmethod
    def get_game_statistics(cls, game_id):
        sql = "SELECT * FROM statistics WHERE game_id = ?"
        cursor.execute(sql, (game_id,))
        return cursor.fetchall()

    @classmethod
    def update_statistic(cls, stat_id, points_scored=None, rebounds=None, assists=None, blocks=None):
        stat = cls.get_statistic_by_id(stat_id)
        if not stat:
            print(f"Statistic with ID {stat_id} not found")
            return

        update_fields = []
        params = []

        if points_scored is not None:
            update_fields.append("points_scored = ?")
            params.append(points_scored)
        if rebounds is not None:
            update_fields.append("rebounds = ?")
            params.append(rebounds)
        if assists is not None:
            update_fields.append("assists = ?")
            params.append(assists)
        if blocks is not None:
            update_fields.append("blocks = ?")
            params.append(blocks)

        if update_fields:
            update_query = f"UPDATE statistics SET {', '.join(update_fields)} WHERE stat_id = ?"
            params.append(stat_id)
            cursor.execute(update_query, tuple(params))
            conn.commit()
            print(f"Statistic with ID {stat_id} updated successfully")
        else:
            print("No fields to update")

    @classmethod
    def delete_statistic(cls, stat_id):
        sql = "DELETE FROM statistics WHERE stat_id = ?"
        cursor.execute(sql, (stat_id,))
        conn.commit()
        print(f"Statistic with ID {stat_id} deleted successfully")
        