### RUN LOTTO GAMES MAIN SCRIPT ###
"""
There are 5 modules that process and save normalized lottery data
lottoscript --> lottorun --> lottogames --> gameplay

1) lottoscript.py - This script receives input from a command line and decide which lotto game Types to run.
   Game Types are 'Powerball', 'MegaMillions', 'TexasLotto', 'TexasTwoStep', 'All'
2) lottorun.py - This class will manage the running of a specific game and collect data
   It also reports detailed results and saves the normalized data to a file.
3) lotogames.py - This class will process one game type.  For example, it may just do Pawerball then it
   may be called again to do Megamillions.
4) gameplay.py - This class will process one drawing (one date) and return the results back to lottogames.
5) gamedefs.py - This file contains the definitions and defines the structure of each specific game to be analyzed
   It was written as a python dictionary instead as a JSON file to demonstrate the use of a python data type.
"""

import sys
import lottorun as lr

# Game Type is 'Powerball', 'MegaMillions', 'TexasLotto', 'TexasTwoStep', 'CashFive', 'All' or 'Test'
# infile is 'False' for link data, Anything else it loads the file name from gamedefs
# Set game_version to '0' to run last versions of a game (incase you no not know it)
def main(game = 'All', infile = False, outfile = True, game_version = 0):
    argc = len(sys.argv)
    if (argc >= 2): game = sys.argv[1]
    if (argc >= 3): infile = sys.argv[2]
    if (argc >= 4): outfile = sys.argv[3]
    if (argc >= 5): game_version = sys.argv[4]

    status = None
    game_options = {'Powerball', 'MegaMillions', 'TexasLotto', 'TexasTwoStep', 'CashFive', 'All', 'Test'}
    if (game in game_options):
        if (game == 'All'):
            game_options.remove('All')
            for this_game in game_options:
                if (game == 'Test'):
                    nowfile = True
                else:
                    nowfile = infile
                lrun = lr.LottoRun(this_game, True, True, True, True)
                status = lrun.RunGame(this_game, nowfile, outfile, game_version)
        else:
            if (game == 'Test'):
                infile = True
            lrun = lr.LottoRun(game, True, True, True, True)
            status = lrun.RunGame(game, infile, outfile, game_version)
    else:
        status = 'Unknown Game Type'

    # Check for possible errors
    if (status == None):
        print(f'\n*** Successful Completion ***\n')
    else:
        print(f'\n*** {status} for "{game}" ***\n')



if __name__ == '__main__':
    main()
