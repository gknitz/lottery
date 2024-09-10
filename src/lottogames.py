### Lottery Games Base Class ###

import urllib.request
import gameplay
from gamedefs import *


class SetupLottoGames (object):

    # Setup Constructor
    def __init__(self, game):

        # Setup Game Name and Game Index
        self.game_name = game
        # Setup Game Index
        i = 0
        for game in games:
            if (game.get(self.game_name, None) != None):
                self.game_index = i
                break
            i += 1



    def LoadGameData (self, file = False):

        data_link = games[self.game_index][self.game_name][0]['game_data_link']
        file_name = games[self.game_index][self.game_name][0]['game_file_name']
        if (data_link == None):
            pw_csv = None
        else:
            if (file == True):
                # Load data from file
                try:
                    with open(file_name, mode='r') as file:
                        self.pw_data = file.read()
                        file.close()
                        # re.split('\r\n|\n', pw_data):
                except Exception as e:
                    return (f'Error in loading File Data. Error is: {e}')
            else:
                try:
                    self.pw_data = urllib.request.urlopen(data_link).read().decode("utf-8")
                    self.SaveDataFile(file_name, self.pw_data)
                except Exception as e:
                    return (f'Error in loading URL Data. Error is: {e}')

            # Remove EOL characters and first line of CSV file if title line
            pw_csv = self.pw_data.splitlines()
            if 'Date' in pw_csv[0]:
                pw_csv.pop(0)

        return (pw_csv)



    def ProcessDrawingData(self, data_list):

        # Get game date differences and Power ball differences
        self.power_location = games[self.game_index][self.game_name][0]['game_power_location']
        self.date_delimiter = games[self.game_index][self.game_name][0]['game_date_delimiter']
        self.date_start_idx = games[self.game_index][self.game_name][0]['game_date_start_index']

        game_results = []
        for draw in data_list:
            if draw:
                # Gate Draw Date and Format Date as a Python Date for comparison
                in_date = draw.split(',', 1)[self.date_start_idx]
                game_date = self.GetDrawDate(in_date)
                # Get game number
                self.game_number = self.GetGameNumberByDate(game_date)

                # Does game object exist
                game_obj = games[self.game_index][self.game_name][self.game_number]['game_object']
                if (game_obj == None):
                    # Create game object for this game
                    game_obj = gameplay.SetupGame(self.game_name, self.game_index, self.game_number)
                    # Set creation of game object to true
                    games[self.game_index][self.game_name][self.game_number]['game_object'] = game_obj

                # Count Numbers Used
                results = game_obj.CountNumbersUsed(draw, self.power_location)
                # save game results for future
                game_data = game_date.strftime('%m/%d/%Y') + ',' + results
                game_results.append(game_data)
                # Increment the number of games processed
                games[self.game_index][self.game_name][0]['total_game_plays'] += 1

        return (game_results)



    def GetGameNumberByDate(self, game_date):
        # Go through game and compare date range to find the game number
        for i, game in self.GameNumberGenerator():
            # Get game number for this draw
            start_date = game.get('start_date')
            end_date = game.get('end_date')
            if (start_date <= game_date <= end_date):
                # print(i, start_date, game_date, end_date)
                break

        # returns Game Number
        return (i)


    # Gate Draw Date and Format Date as a Python Date
    def GetDrawDate(self, in_date):
        draw_date = in_date.split(self.date_delimiter)
        return(date(int(draw_date[2]), int(draw_date[0]), int(draw_date[1])))


    # Save downloaded file
    def SaveDataFile(self, file_name, file_data):

        try:
            file = open(file_name, 'w')
            file.write(file_data)
        except Exception as e:
            return (f'Error in Saving File Data. Error is: {e}')

        file.close()


    ### Generators
    # Use Generator to loop through games and get game, game number
    def GameNumberGenerator(self):
        for i, game in enumerate(games[self.game_index][self.game_name], start=0):
            # skip zero game number
            if (i == 0): continue
            # Get game number
            yield i, game


    # Use Generator to loop through games and get game, game object
    def GameObjectGenerator(self):
        for i, game in enumerate(games[self.game_index][self.game_name], start=0):
            # skip zero game number
            if (i == 0): continue
            game_obj = games[self.game_index][self.game_name][i]['game_object']
            if (game_obj != None):
                # Get game object
                yield i, game_obj



    ### Class Helpers

    # Get Game Name
    def GetGameName(self):
        return (self.game_name)


    # Get Game Data Size in bytes
    def GetGameDataSize (self):
        return(len(self.pw_data))


    # Get The number of games played by all games
    def GetTotalGamesPlayed (self):
        return(games[self.game_index][self.game_name][0]['total_game_plays'])


    # Go through game to find game objects that have been used and
    # the number of games played from each object
    def GetGamesProcessed(self):
        results = {}
        for i, game_obj in self.GameObjectGenerator():
            results[i] = game_obj.GetGameProcessed()
        # return number of games processed per game
        return(results)


    #
    def GetFiveList(self):
        results = {}
        for i, game_obj in self.GameObjectGenerator():
            results[i] = game_obj.GetFiveList()
        # return list
        return(results)


    #
    def GetPowerList(self):
        results = {}
        for i, game_obj in self.GameObjectGenerator():
            results[i] = game_obj.GetPowerList()
        # return list
        return (results)


    #
    def GetMultiplierList(self):
        results = {}
        for i, game_obj in self.GameObjectGenerator():
            results[i] = game_obj.GetMultiplierList()
        # return list
        return (results)


    # Return active games Maximum Play Thresholds
    def GetMaxPlayThreshold(self):
        results = {}
        for i, game in self.GameNumberGenerator():
            results[i] = game.get('max_play_threshold')
        # return active games Maximum Play Thresholds
        return (results)


    # Return active games Maximum Power Thresholds
    def GetMaxPowerThreshold(self):
        results = {}
        for i, game in self.GameNumberGenerator():
            results[i] = game.get('max_power_threshold')
        # return active games Maximum Power Thresholds
        return (results)


  # Return number of last game played
    def GetLastGameNumber(self):
        for i, game in self.GameNumberGenerator():
            end_date = game.get('end_date')
            if (end_date == date.today()):
                break
        # returns Latest Game Number
        return (i)
