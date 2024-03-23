import json


class Data:
    def __init__(self):
        self.players_data = []

    def load_players_data(self):
        with open('PlayersData.json', 'r') as file:
            self.players_data = json.load(file)

    def save_players_data(self):
        with open('PlayersData.json', 'r+') as file:
            try:
                existing_data = json.load(file)
            except json.decoder.JSONDecodeError:
                existing_data = []

            existing_data.extend(self.players_data)
            file.seek(0)
            json.dump(existing_data, file, indent=4)
            file.truncate()

    def leaderboard(self):
        sorted_players = sorted(self.players_data, key=lambda x: x['points'], reverse=True)
        num_players = min(len(sorted_players), 15)
        for i, player in enumerate(sorted_players[:num_players], 1):
            print(f"{i}. {player['player']}: {player['points']} points")

    def add_player(self, player_name, points, current_question=0, current_help=10):
        player_exists = False
        for player in self.players_data:
            if player['player'] == player_name:
                player['points'] = points
                player['currentQuestion'] = current_question
                player['currentHelp'] = current_help
                player_exists = True
                break
        if not player_exists:
            player = {
                'player': player_name,
                'points': points,
                'currentQuestion': current_question,
                'currentHelp': current_help
            }
            self.players_data.append(player)
        self.save_players_data()

    def update_player(self, player_name, points, current_question=None, current_help=None):
        for player in self.players_data:
            if player['player'] == player_name:
                if points > player['points']:
                    player['points'] = points
                    if current_question is not None:
                        player['currentQuestion'] = current_question
                    if current_help is not None:
                        player['currentHelp'] = current_help
                    break

    def get_player_data(self, player_name):
        for player in self.players_data:
            if player['player'] == player_name:
                return player
        return None

    def reset_player_data(self, player_name):
        for player in self.players_data:
            if player['player'] == player_name:
                player['points'] = 0
                player['currentQuestion'] = 0
                player['currentHelp'] = 10
                break

    def load_game_state(self, filename):
        with open(filename, 'r') as file:
            game_state = json.load(file)
        return game_state

    def save_game_state(self, game_state, filename):
        with open(filename, 'w') as file:
            json.dump(game_state, file)
