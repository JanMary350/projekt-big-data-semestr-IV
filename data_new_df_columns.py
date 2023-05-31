import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
import numpy as np

def in_same_range(partner_range, value):
    try:
        "check if the value is in the range chosen by a partner"
        numbers = re.findall(r'\d+', partner_range)  
        numbers = list(map(int, numbers))
        value = int(value)
        print(numbers)
        print(value)
        in_range = bool(numbers[0]<=value and value<=numbers[1])
    except ValueError:
        return None
    return in_range



# def replace_ranges(df):


df = pd.read_csv('speeddating.csv')
new_df = pd.DataFrame()
for row in df.itertuples():

    difference_age = row[6]
    # print(difference_age)

    difference_race = row[10]

    importance_same_race = row[11]

    #preferences

    difference_attractive_imporatance = abs(row[16]-row[40])
    # print(difference_attractive_imporatance, row[16], row[40])

    difference_sincere_imporatance = abs(row[17]-row[41])
    # print(difference_sincere_imporatance, row[17], row[41])

    difference_intelligence_imporatance = abs(row[18]-row[42])
    # print(difference_intelligence_imporatance, row[18], row[42])

    difference_funny_imporatance = abs(row[19]-row[43])
    # print(difference_funny_imporatance, row[19], row[43])

    difference_ambition_imporatance = abs(row[20]-row[44])
    # print(difference_ambition_imporatance, row[20], row[44])

    difference_shared_interests_imporatance = abs(row[21]-row[45])
    # print(difference_shared_interests_imporatance, row[21], row[45])

    #ratings

    attractive_difference = abs(row[28] - row[52])
    # print(row[28], row[52], attractive_difference)

    sinsere_difference = abs(row[29] - row[53])
    # print(row[29], row[53], sinsere_difference)

    intelligence_difference = abs(row[30] - row[54])
    # print(row[30], row[54], intelligence_difference)

    funny_difference = abs(row[31] - row[55])
    # print(row[31], row[55], funny_difference)

    ambitous_difference = abs(row[32] - row[56])
    # print(row[32], row[56], ambitous_difference)

    interests_correlation = row[108]
    target = row[123]











# print(df.head())
# print(df.shape)
# # df =df.dropna()
# print(df.shape)
"""
NEW COLUMNS:
11, 13 - preference of same race in partners range
12, 14 - preference of same religion in partners range


"""
'''
INTERESTS:
 sports,
 tvsports,
 exercise,
 dining,
 museums,
 art,
 hiking,
 gaming,
 clubbing,
 reading,
 tv,
 theater,
 movies,
 concerts,
 music,
 shopping,
 yoga,
 d_sports,
 d_tvsports,
 d_exercise,
 d_dining,
 d_museums,
 d_art,
 d_hiking,
 d_gaming,
 d_clubbing,
 d_reading,
 d_tv,
 d_theater,
 d_movies,
 d_concerts,
 d_music,
 d_shopping,
 d_yoga,


PREFERENCES:
pref_o_attractive,
 pref_o_sincere,
 pref_o_intelligence,
 pref_o_funny,
 pref_o_ambitious,
 pref_o_shared_interests,
 d_pref_o_attractive,
 d_pref_o_sincere,
 d_pref_o_intelligence,
 d_pref_o_funny,
 d_pref_o_ambitious,
 d_pref_o_shared_interests,
 ,attractive_important,
 sincere_important,
 intellicence_important,
 funny_important,
 ambtition_important,
 shared_interests_important,
 d_attractive_important,
 d_sincere_important,
 d_intellicence_important,
 d_funny_important,
 d_ambtition_important,
 d_shared_interests_important,
 attractive
 sincere
 ,intelligence,
 funny,
 ambition,
 d_attractive,
 d_sincere,
 d_intelligence,
 d_funny,
 d_ambition,
 attractive_partner,
 sincere_partner,
 intelligence_partner,
 funny_partner,
 ambition_partner,
 shared_interests_partner,
 d_attractive_partner,
 d_sincere_partner,
 d_intelligence_partner
 ,d_funny_partner,
 d_ambition_partner,
 d_shared_interests_partner,
'''