# RUN LOTTO GAMES MAIN CLASS ###
#
# lottorun.py - This class
#   It also reports detailed results and saves the normalized data to a file.
#


import lottogames
from datetime import datetime


class LottoRun (object):

    DATA_DIR_PREFIX = '../output/'
    HEADER = 'Draw Date,Game #,Winning Numbers,Ball,Multiplier'

    PRINT_DATA_ARRAYS = False
    PRINT_FREQ_NUMBERS = False
    PRINT_LARGE_NUMBERS = False
    PRINT_THRESHOLD_NUMBERS = False


    def __init__(self, name, data_array, freq_numbers, large_numbers, threshold_numbers):
        self.game_name = name
        self.game_results = ""
        self.saved_file_name = ""
        self.current_game_version = 0
        self.l = None

        self.PRINT_DATA_ARRAYS = data_array
        self.PRINT_FREQ_NUMBERS = freq_numbers
        self.PRINT_LARGE_NUMBERS = large_numbers
        self.PRINT_THRESHOLD_NUMBERS = threshold_numbers


    # Run a specific lotto game
    def RunGame(self, game_name, infile, outfile, game_version):

        # Save game_name and current_game_version
        self.game_name = game_name
        self.current_game_version = game_version
        # Fire up Setup object
        self.l = lottogames.SetupLottoGames(game_name)
        # Load Game Data
        data_list = self.l.LoadGameData(infile)
        # Check for load data errors
        if not isinstance(data_list, list):
            return (data_list)

        # Process Game Data
        results = self.l.ProcessDrawingData(data_list)
        if (type(results) == str) and (results.startswith('Error')):
            return ('Error in Processing Input Data')
        else:
            # Locally store game results
            self.game_results = results
            # Check to see if we only report last game results
            if (self.current_game_version == 0):
                self.current_game_version = self.l.GetLastGameNumber()
            # Save normalized data to file
            if (outfile == True):
                status = self.SaveNormalDataFile(results)
                if (status != None):
                    return (status)

            print('\n*** Game Overview')
            print(f"Game Name is {game_name}")
            # Print Data Size in bytes
            print(f"Size of data in bytes is     ==> {self.l.GetGameDataSize()}")
            # Print Total Number of Games Played
            print(f"Total Number of games played ==> {self.l.GetTotalGamesPlayed()}")
            # Print Number of Draws Processed for each game
            print(self.printList('Number of games processed', self.l.GetGamesProcessed()))

            if (self.PRINT_DATA_ARRAYS == True):
                # Print out the List of data
                five_data_arrays = self.printList('Five Ball', self.l.GetFiveList())
                ball_data_arrays = self.printList('Power Ball', self.l.GetPowerList())
                multi_data_arrays = self.printList('Multiplier', self.l.GetMultiplierList())
                print('\n*** Final Lists of data')
                print(five_data_arrays)
                print(ball_data_arrays)
                print(multi_data_arrays)

            if (self.PRINT_FREQ_NUMBERS == True):
                # Print first five high frequency numbers for each game
                five_freq_numbers = self.printTopFive("Five", self.l.GetFiveList(), True)
                ball_freq_numbers = self.printTopFive("Ball", self.l.GetPowerList(), True)
                print('\n*** First Five Highest Frequency Numbers for Each Game')
                print(five_freq_numbers)
                print(ball_freq_numbers)

                # Print first five low frequency numbers for each game
                five_low_five = self.printTopFive("Five", self.l.GetFiveList(), False)
                ball_low_five = self.printTopFive("Ball", self.l.GetPowerList(), False)
                print('\n*** First Five Lowest Frequency Numbers for Each Game')
                print(five_low_five)
                print(ball_low_five)

            if (self.PRINT_THRESHOLD_NUMBERS == True):
                # Print high frequency numbers over a threshold for each game
                five_threshold_numbers = self.printNumberFrequency("Five", self.l.GetFiveList(), self.l.GetMaxPlayThreshold())
                ball_threshold_numbers = self.printNumberFrequency("Ball", self.l.GetPowerList(), self.l.GetMaxPowerThreshold())
                print('\n*** High Frequency Numbers over a Threshold for Each Game')
                print(five_threshold_numbers)
                print(ball_threshold_numbers)

            if (self.PRINT_LARGE_NUMBERS == True):
                # Print Law of Large Numbers for each game
                five_large_numbers = self.printLawLargeNums("Five", self.l.GetFiveList(), self.l.GetGamesProcessed())
                ball_large_numbers = self.printLawLargeNums("Ball", self.l.GetPowerList(), self.l.GetGamesProcessed())
                print('\n*** Law of Large Numbers for Each Game')
                print(five_large_numbers)
                print(ball_large_numbers)

            if __name__ == '__main__':
                return (None)


    #
    def getFileName (self):
        return self.saved_file_name


    #
    def SaveNormalDataFile (self, result):

        now = datetime.now()  # current date and time
        self.saved_file_name = now.strftime(self.DATA_DIR_PREFIX + self.game_name + "_%m%d%y_%H%M.csv")

        file = None
        try:
            file = open(self.saved_file_name, 'w')
            file.write(self.HEADER + '\n')
            for draw in result:
                draw_number = draw.split(',')
                if (self.current_game_version == int(draw_number[1])) or (self.current_game_version == 0):
                    file.write(draw + '\n')

        except Exception as e:
            print(f'Error in Saving File Data. Error is: {e}')

        file.close()
        return None


    # Return save game results
    def getGameResults(self):

        sorted_results = [self.HEADER]
        for draw in self.game_results:
            draw_number = draw.split(',')
            if (self.current_game_version == int(draw_number[1])):
                sorted_results.append(draw)

        return sorted_results



    # Get the Number of games processed
    def getGamesProcessed(self):
        return self.l.GetGamesProcessed()

    # Get the Five Lists for all games
    def getFiveList(self):
        return self.l.GetFiveList()

    # Get the Ball List for all games
    def getBallList(self):
        return self.l.GetPowerList()

    # Get and put Large Numbers in array as [number, fraction]
    def getLawLargeNums(self, the_dict, games_dict):
        results = []
        for game_num, the_list in the_dict.items():
            if (the_list == None):
                continue
            elif (self.current_game_version == game_num) or (self.current_game_version == 0):
                draw_count = games_dict.get(game_num)
                mylist = the_list.copy()
                for (index, value) in enumerate(mylist):
                    if (index == 0): continue
                    mylist[index] = (value/draw_count)
                sorted_mylist = sorted(((v, i) for i, v in enumerate(mylist)), reverse=False)

                for index, (v, i) in enumerate(sorted_mylist):
                    if (i == 0): continue
                    results.append([i, v])

        return results


    #
    def printList (self, text, the_dict):
        results = ""
        for game_num, count in the_dict.items():
            if (self.current_game_version == game_num) or (self.current_game_version == 0):
               results += (f'{text} by Game {game_num} Counts => {count}\n')

        return results


    #
    def printNumberFrequency(self, text, the_dict, the_max):
        results = ""
        for game_num, the_list in the_dict.items():
            if (the_list == None):
                continue
            elif (self.current_game_version == game_num) or (self.current_game_version == 0):
                for game_max_num, the_threshold in the_max.items():
                    if (game_num == game_max_num):
                        break
                for i in range(1, len(the_list)):
                    if the_list[i] > the_threshold:
                        results += (f'{self.game_name} {game_num}, {text} Number {i} => Frequency {the_list[i]}\n')

        return results


    #
    def printTopFive(self, text, the_dict, top_five):
        results = ""
        # Make copy of list, remove total count at (0) and sort into tuple to save indicies
        for game_num, the_list in the_dict.items():
            if (the_list == None):
                continue
            elif (self.current_game_version == game_num) or (self.current_game_version == 0):
                mylist = the_list.copy()
                sorted_mylist = sorted(((v, i) for i, v in enumerate(mylist)), reverse=top_five)
                loop_count = 5
                for i, (value, index) in enumerate(sorted_mylist):
                    if (index == 0):
                        loop_count += 1
                        continue
                    if (i >= loop_count): break
                    results += (f'{self.game_name} {game_num}, {text} Number {index} -> Frequency {value}\n')

        return results


    #
    def printLawLargeNums(self, text, the_dict, games_dict):
        results = ""
        for game_num, the_list in the_dict.items():
            if (the_list == None):
                continue
            elif (self.current_game_version == game_num) or (self.current_game_version == 0):
                draw_count = games_dict.get(game_num)
                mylist = the_list.copy()
                for (index, value) in enumerate(mylist):
                    if (index == 0): continue
                    mylist[index] = (value/draw_count)
                sorted_mylist = sorted(((v, i) for i, v in enumerate(mylist)), reverse=False)

                # Get the middle based on the number of balls
                num_of_balls = len(the_dict[game_num]) - 1
                half_balls = num_of_balls//2
                for index, (v, i) in enumerate(sorted_mylist):
                    if (i == 0): continue
                    if (index == half_balls):
                        results += (f'MID-POINT OF THE {text} BALLS\n')
                    results += (f'{self.game_name} Game {game_num}, {text} Number {i:02}, {v:2.4f}\n')

            results += '\n'
        return results
