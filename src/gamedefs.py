### THIS IS THE GAME DEFINITIONS MODULE
#
# This file contains the definitions and defines the structure of each
# specific game to be analyzed

### Powerball Data
# Downloaded File Format
# Draw Date,    Winning Numbers,    Multiplier
# 09/26/2020,   11 21 27 36 62 24,  3
#
# Game  Starting Date   5 Balls   Power Ball  Jackpot Odds        Multiplier
#   1   04/22/1992      45        45          1:54,979,154        None
#   2   11/05/1997      49        42          1:80,089,127        None
#   3   03/07/2001      49        42          1:80,089,127        1x-5x
#   4   10/09/2002      53        42          1:120,526,769       2x-5x
#   5   08/28/2005      55        42          1:146,107,961       2x-5x
#   6   01/07/2009      59        39          1:195,249,054       2x-5x; 10x
#   7   01/15/2012      59        35          1:175,223,510       None
#   8   01/19/2014      59        35          1:175,223,510       2x-5x
#   9   10/07/2015      69        26          1:292,201,338       2x-5x; 10x


### Mega Millions Data
# Downloaded File Format
# Draw Date,    Winning Numbers,    Mega Ball,  Multiplier
# 09/25/2020,   20 36 37 48 67,     16,         02
#
# Game  Starting Date   5 Balls   Mega Ball   Jackpot Odds        Multiplier
#   1   09/06/1996      50        25          1:52,969,000        1x-5x
#   2   01/13/1999      50        36          1:76,275,360        1x-5x
#   3   05/15/2002      52        52          1:135,145,920       1x-5x
#   4   06/22/2005      56        46          1:175,711,536       1x-5x
#   5   10/19/2013      75        15          1:258,890,850       1x-5x
#   6   10/28/2017      70        25          1:302,575,350       1x-5x


### Texas Lotto Data File
### Started as a 6/54 in July 2000, then changed to Powerball, and in April 2006,
### changed back from its Powerball-type game to the original 6/54 format.
# - Nov 14, 1992 to May 3, 2003:
# - Game Name, Month, Day, Year, Num1, Num2, Num3, Num4, Num5, Num6
# - Lotto Texas,11,14,1992,13,16,22,29,32,36
# - May 7, 2003 to Apr 22, 2006:
# - Game Name, Month, Day, Year, Num1, Num2, Num3, Num4, Num5, Bonus Ball
# - Lotto Texas,5,7,2003,1,28,11,41,17,40
# - Apr 26, 2006 to present:
# - Game Name, Month, Day, Year, Num1, Num2, Num3, Num4, Num5, Num6
# - Lotto Texas,4,26,2006,32,6,23,14,8,52
# Game  Starting Date   5 Balls   Mega Ball   Jackpot Odds
#   1   11/14/1992      54        None        1:25,827,165
#   2   05/07/2003      54        54          1:25,827,165
#   3   04/26/2006      54        None        1:25,827,165


### Texas Two Step Data File
# Game Name, Month, Day, Year, Num1, Num2, Num3, Num4, Bonus Ball
# Texas Two Step,5,18,2001,9,10,22,13,1
# Game  Starting Date   5 Balls   Mega Ball   Jackpot Odds
#   1   05/13/2001      35        35          1:1,832,600


### Texas Cash Five Data File
# Game Name, Month, Day, Year, Num1, Num2, Num3, Num4, Num5
# Cash Five,10,13,1995,26,1,22,23,35
# Game  Starting Date   5 Balls   Mega Ball   Jackpot Odds
#   1   10/13/1995      35        None        1:324,632


### Test Data File (combination of Powerball & MegaMillions)
# Draw Date,    Winning Numbers,    Mega Ball,  Multiplier
# 04/22/1992,   20 36 37 48 67,     16,         02
# Game  Starting Date   5 Balls   Mega Ball   Jackpot Odds        Multiplier
#   1   04/22/1992      75        54          1:302,575,350       1x-10x



from datetime import date

### Global Variables
# GameTypes are 'Powerball', 'MegaMillions', 'TexasLotto', 'TexasTwoStep', 'CashFive', 'Test'
# games is a complex Python data structure to show a Python Dictionary type
games = [
        {'Powerball': [
                    {'game_name': 'Powerball', 'total_game_plays': 0,   # Index Zero
                     'game_file_name': '../data/ny_powerball_data.csv',
                     'game_power_location': 'inline', 'game_date_delimiter': '/', 'game_date_start_index': 0,
                     'game_data_link': 'https://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD'
                    },
                    {'game_plays': 0, 'game_object': None,      # Game One, Index One
                        'start_date': date(1992, 4, 22), 'end_date': date(1997, 11, 4),
                        'max_play_number': 45+1, 'max_power_number': 45+1, 'max_multi_number': None,
                        'max_play_threshold': 25, 'max_power_threshold': 10,
                        'num_input_data_fields': 3, 'num_play_numbers': 5,
                        'multiplex_field_index': 2, 'lotto_ball_field_index': 5, 'num_input_data_index': 1
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Two, Index Two
                        'start_date': date(1997, 11, 5), 'end_date': date(2001, 3, 6),
                        'max_play_number': 49+1, 'max_power_number': 42+1, 'max_multi_number': None,
                        'max_play_threshold': 25, 'max_power_threshold': 10,
                        'num_input_data_fields': 3, 'num_play_numbers': 5,
                        'multiplex_field_index': 2, 'lotto_ball_field_index': 5, 'num_input_data_index': 1
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Three, Index Three
                        'start_date': date(2001, 3, 7), 'end_date': date(2002, 10, 8),
                        'max_play_number': 49+1, 'max_power_number': 42+1, 'max_multi_number': 5+1,
                        'max_play_threshold': 25, 'max_power_threshold': 10,
                        'num_input_data_fields': 3, 'num_play_numbers': 5,
                        'mltiplex_field_index': 2, 'lotto_ball_field_index': 5, 'num_input_data_index': 1
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Four, Index Four
                        'start_date': date(2002, 10, 9), 'end_date': date(2005, 8, 27),
                        'max_play_number': 53+1, 'max_power_number': 42+1, 'max_multi_number': 5+1,
                        'max_play_threshold': 25, 'max_power_threshold': 10,
                        'num_input_data_fields': 3, 'num_play_numbers': 5,
                        'multiplex_field_index': 2, 'lotto_ball_field_index': 5, 'num_input_data_index': 1
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Five, Index Five
                        'start_date': date(2005, 8, 28), 'end_date': date(2009, 1, 6),
                        'max_play_number': 55+1, 'max_power_number': 42+1, 'max_multi_number': 5+1,
                        'max_play_threshold': 25, 'max_power_threshold': 10,
                        'num_input_data_fields': 3, 'num_play_numbers': 5,
                        'multiplex_field_index': 2, 'lotto_ball_field_index': 5, 'num_input_data_index': 1
                     },
                     {'game_plays': 0, 'game_object': None,     # Game Six, Index Six
                        'start_date': date(2009, 1, 7), 'end_date': date(2012, 1, 14),
                        'max_play_number': 59+1, 'max_power_number': 39+1, 'max_multi_number': 10+1,
                        'max_play_threshold': 25, 'max_power_threshold': 10,
                        'num_input_data_fields': 3, 'num_play_numbers': 5,
                        'multiplex_field_index': 2, 'lotto_ball_field_index': 5, 'num_input_data_index': 1
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Seven, Index Seven
                        'start_date': date(2012, 1, 15), 'end_date': date(2014, 1, 18),
                        'max_play_number': 59+1, 'max_power_number': 35+1, 'max_multi_number': None,
                        'max_play_threshold': 25, 'max_power_threshold': 10,
                        'num_input_data_fields': 3, 'num_play_numbers': 5,
                        'multiplex_field_index': 2, 'lotto_ball_field_index': 5, 'num_input_data_index': 1
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Eight, Index Eight
                        'start_date': date(2014, 1, 19), 'end_date': date(2015, 10, 6),
                        'max_play_number': 59+1, 'max_power_number': 35+1, 'max_multi_number': 5+1,
                        'max_play_threshold': 20, 'max_power_threshold': 10,
                        'num_input_data_fields': 3, 'num_play_numbers': 5,
                        'multiplex_field_index': 2, 'lotto_ball_field_index': 5, 'num_input_data_index': 1
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Nine, Index Nine
                        'start_date': date(2015, 10, 7), 'end_date': date.today(),
                        'max_play_number': 69+1, 'max_power_number': 26+1, 'max_multi_number': 10+1,
                        'max_play_threshold': 55, 'max_power_threshold': 30,
                        'num_input_data_fields': 3, 'num_play_numbers': 5,
                        'multiplex_field_index': 2, 'lotto_ball_field_index': 5, 'num_input_data_index': 1
                     }
               ]
        },
        {'MegaMillions':    [
                    {'game_name': 'Mega Millions', 'total_game_plays': 0,   # Index Zero
                     'game_file_name': '../data/ny_megamillions_data.csv',
                     'game_power_location': 'separate', 'game_date_delimiter': '/', 'game_date_start_index': 0,
                     'game_data_link': 'https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD',
                    },
                    {'game_plays': 0, 'game_object': None,      # Game One, Index One
                        'start_date': date(1996, 9, 6), 'end_date': date(1999, 1, 12),
                        'max_play_number': 50+1, 'max_power_number': 25+1, 'max_multi_number': 5+1,
                        'max_play_threshold': 35, 'max_power_threshold': 10,
                        'num_input_data_fields': 4, 'num_play_numbers': 5,
                        'multiplex_field_index': 3, 'lotto_ball_field_index': 2, 'num_input_data_index': 1
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Two, Index Two
                        'start_date': date(1999, 1, 13), 'end_date': date(2002, 5, 14),
                        'max_play_number': 50+1, 'max_power_number': 36+1, 'max_multi_number': 5+1,
                        'max_play_threshold': 35, 'max_power_threshold': 10,
                        'num_input_data_fields': 4, 'num_play_numbers': 5,
                        'multiplex_field_index': 3, 'lotto_ball_field_index': 2, 'num_input_data_index': 1
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Three, Index Three
                        'start_date': date(2002, 5, 15), 'end_date': date(2005, 6, 21),
                        'max_play_number': 52+1, 'max_power_number': 52+1, 'max_multi_number': 5+1,
                        'max_play_threshold': 35, 'max_power_threshold': 10,
                        'num_input_data_fields': 4, 'num_play_numbers': 5,
                        'multiplex_field_index': 3, 'lotto_ball_field_index': 2, 'num_input_data_index': 1
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Four, Index Four
                        'start_date': date(2005, 6, 22), 'end_date': date(2013, 10, 18),
                        'max_play_number': 56+1, 'max_power_number': 46+1, 'max_multi_number': 5+1,
                        'max_play_threshold': 85, 'max_power_threshold': 22,
                        'num_input_data_fields': 4, 'num_play_numbers': 5,
                        'multiplex_field_index': 3, 'lotto_ball_field_index': 2, 'num_input_data_index': 1
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Five, Index Five
                        'start_date': date(2013, 10, 19), 'end_date': date(2017, 10, 27),
                        'max_play_number': 75+1, 'max_power_number': 15+1, 'max_multi_number': 5+1,
                        'max_play_threshold': 35, 'max_power_threshold': 35,
                        'num_input_data_fields': 4, 'num_play_numbers': 5,
                        'multiplex_field_index': 3, 'lotto_ball_field_index': 2, 'num_input_data_index': 1
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Six, Index Six
                        'start_date': date(2017, 10, 28), 'end_date': date.today(),
                        'max_play_number': 70+1, 'max_power_number': 25+1, 'max_multi_number': 5+1,
                        'max_play_threshold': 35, 'max_power_threshold': 18,
                        'num_input_data_fields': 4, 'num_play_numbers': 5,
                        'multiplex_field_index': 3, 'lotto_ball_field_index': 2, 'num_input_data_index': 1
                     }
               ]
        },
        {'TexasLotto': [
                    {'game_name': 'Texas Lotto', 'total_game_plays': 0,   # Index Zero
                     'game_file_name': '../data/tx_lottotexas_data.csv',
                     'game_power_location': 'continuous', 'game_date_delimiter': ',', 'game_date_start_index': 1,
                     'game_data_link': 'https://www.texaslottery.com/export/sites/lottery/Games/Lotto_Texas/Winning_Numbers/lottotexas.csv'
                     },
                    {'game_plays': 0, 'game_object': None,      # Game One, Index One
                        'start_date': date(1992, 11, 14), 'end_date': date(2003, 5, 3),
                        'max_play_number': 54+1, 'max_power_number': None, 'max_multi_number': None,
                        'max_play_threshold': 140, 'max_power_threshold': None,
                        'num_input_data_fields': 10, 'num_play_numbers': 6,
                        'multiplex_field_index': None, 'lotto_ball_field_index': None, 'num_input_data_index': 4
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Two, Index Two
                        'start_date': date(2003, 5, 7), 'end_date': date(2006, 4, 22),
                        'max_play_number': 54+1, 'max_power_number': 54+1, 'max_multi_number': None,
                        'max_play_threshold': 40, 'max_power_threshold': 10,
                        'num_input_data_fields': 10, 'num_play_numbers': 5,
                        'multiplex_field_index': None, 'lotto_ball_field_index': 9, 'num_input_data_index': 4
                     },
                    {'game_plays': 0, 'game_object': None,      # Game Three, Index Three
                        'start_date': date(2006, 4, 26), 'end_date': date.today(),
                        'max_play_number': 54+1, 'max_power_number': None, 'max_multi_number': None,
                        'max_play_threshold': 200, 'max_power_threshold': None,
                        'num_input_data_fields': 10, 'num_play_numbers': 6,
                        'multiplex_field_index': None, 'lotto_ball_field_index': None, 'num_input_data_index': 4
                     }
              ]
        },
        {'TexasTwoStep': [
                    {'game_name': 'Texas Two Step', 'total_game_plays': 0,  # Index Zero
                         'game_file_name': '../data/tx_texastwostep_data.csv',
                         'game_power_location': 'continuous', 'game_date_delimiter': ',', 'game_date_start_index': 1,
                         'game_data_link': 'https://www.texaslottery.com/export/sites/lottery/Games/Texas_Two_Step/Winning_Numbers/texastwostep.csv'
                    },
                    {'game_plays': 0, 'game_object': None,  # Game One, Index One
                         'start_date': date(2001, 5, 13), 'end_date': date.today(),
                         'max_play_number': 35+1, 'max_power_number': 35+1, 'max_multi_number': None,
                         'max_play_threshold': 260, 'max_power_threshold': 70,
                         'num_input_data_fields': 9, 'num_play_numbers': 4,
                         'multiplex_field_index': None, 'lotto_ball_field_index': 8, 'num_input_data_index': 4
                    },
            ]
        },
        {'CashFive': [
                    {'game_name': 'Cash Five', 'total_game_plays': 0,  # Index Zero
                     'game_file_name': '../data/tx_cashfive_data.csv',
                     'game_power_location': 'continuous', 'game_date_delimiter': ',', 'game_date_start_index': 1,
                     'game_data_link': 'https://www.texaslottery.com/export/sites/lottery/Games/Cash_Five/Winning_Numbers/cashfive.csv'
                     },
                    {'game_plays': 0, 'game_object': None,  # Game One, Index One
                     'start_date': date(1995, 10, 13), 'end_date': date.today(),
                     'max_play_number': 39 + 1, 'max_power_number': None, 'max_multi_number': None,
                     'max_play_threshold': 260, 'max_power_threshold': 70,
                     'num_input_data_fields': 9, 'num_play_numbers': 5,
                     'multiplex_field_index': None, 'lotto_ball_field_index': None, 'num_input_data_index': 4
                     },
            ]
        },

        {'Test': [
                {'game_name': 'Mega Millions', 'total_game_plays': 0,  # Index Zero
                 'game_file_name': '../data/ny_test_data.csv',
                 'game_power_location': 'separate', 'game_date_delimiter': '/', 'game_date_start_index': 0,
                 'game_data_link': 'file:////Users/gknitz/PycharmProjects/lottery/data/ny_bothtest_data.csv'
                 },
                {'game_plays': 0, 'game_object': None,  # Game One, Index One
                 'start_date': date(1992, 1, 1), 'end_date': date.today(),
                 'max_play_number': 75+1, 'max_power_number': 54+1, 'max_multi_number': 10+1,
                 'max_play_threshold': 35, 'max_power_threshold': 18,
                 'num_input_data_fields': 4, 'num_play_numbers': 5,
                 'multiplex_field_index': 3, 'lotto_ball_field_index': 2, 'num_input_data_index': 1
                 },
            ]
        }

    ]
