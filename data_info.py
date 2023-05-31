import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('speeddating.csv')

print(df.head())
print(df.shape)
# df =df.dropna()
dfSample = df.sample(n=1000)
print(df.shape)
sns.pairplot(dfSample, hue='match',vars=['d_age','samerace', 'interests_correlate'])
"""possible affect of d_age on match"""
plt.show()

sns.pairplot(dfSample, hue="match", vars=["d_age", "match"] , corner=True )
sns.countplot(x='match', data=dfSample)
plt.title('Match vs d_age')
'''possibly important feature = d_age'''
plt.show()

sns.pairplot(dfSample, hue="match", vars=["interests_correlate", "match"] , corner=True )

plt.title('Match vs interests_correlate')
'''possibly not so important feature = interests_correlate'''
plt.show()

"""samoocena vs oczekiwania partnera"""
sns.pairplot(dfSample, hue="match", vars=["attractive", "sincere", "intelligence", "pref_o_attractive", "pref_o_sincere", "pref_o_intelligence"] , corner=True )
plt.title('oczekiwania partnera vs samoocena 1')
plt.show()

"""samoocena vs oczekiwania partnera 2"""
sns.pairplot(dfSample, hue="match", vars=["funny", "ambition", "pref_o_funny", "pref_o_ambitious"] , corner=True )
plt.title('oczekiwania partnera vs samoocena 2')
plt.show()

"""oczekiwania vs oczekiwania partnera"""
sns.pairplot(dfSample, hue="match", vars=["attractive_important", "sincere_important", "intellicence_important",  "pref_o_attractive", "pref_o_sincere", "pref_o_intelligence"] , corner=True )
plt.title('oczekiwania vs oczekiwania partnera 1')
plt.show()

"""oczekiwania vs oczekiwania partnera"""
sns.pairplot(dfSample, hue="match", vars=["funny_important", "ambtition_important", "pref_o_funny", "pref_o_ambitious"] , corner=True )
plt.title('oczekiwania vs oczekiwania partnera 1')
plt.show()

"""oczekiwania co do wyników randkowania po 20 szybkich randkach"""
sns.pairplot(dfSample, hue="match", vars=["expected_happy_with_sd_people", "expected_num_interested_in_me", "expected_num_matches"] , corner=True )
plt.title("oczekiwanie dotyczące randkowania")
plt.show()

"""Czy jakiś kandydat ma większe szanse na sukces?"""
sns.pairplot(dfSample, hue="match", vars=["age", "race", ] , corner=True )
# sns.pairplot(df, hue='match',vars=['d_age','samerace', 'importance_same_race','like'], corner=True )


"""
 * gender: Gender of self  
 * age: Age of self  
 * age_o: Age of partner  
 * d_age: Difference in age  
 * race: Race of self  
 * race_o: Race of partner  
 * samerace: Whether the two persons have the same race or not.  
 * importance_same_race: How important is it that partner is of same race?  
 * importance_same_religion: How important is it that partner has same religion?  
 * field: Field of study  
 * pref_o_attractive: How important does partner rate attractiveness  
 * pref_o_sinsere: How important does partner rate sincerity  
 * pref_o_intelligence: How important does partner rate intelligence  
 * pref_o_funny: How important does partner rate being funny  
 * pref_o_ambitious: How important does partner rate ambition  
 * pref_o_shared_interests: How important does partner rate having shared interests  
 * attractive_o: Rating by partner (about me) at night of event on attractiveness  
 * sincere_o: Rating by partner (about me) at night of event on sincerity  
 * intelligence_o: Rating by partner (about me) at night of event on intelligence  
 * funny_o: Rating by partner (about me) at night of event on being funny  
 * ambitous_o: Rating by partner (about me) at night of event on being ambitious  
 * shared_interests_o: Rating by partner (about me) at night of event on shared interest  
 * attractive_important: What do you look for in a partner - attractiveness  
 * sincere_important: What do you look for in a partner - sincerity  
 * intellicence_important: What do you look for in a partner - intelligence  
 * funny_important: What do you look for in a partner - being funny  
 * ambtition_important: What do you look for in a partner - ambition  
 * shared_interests_important: What do you look for in a partner - shared interests  
 * attractive: Rate yourself - attractiveness  
 * sincere: Rate yourself - sincerity   
 * intelligence: Rate yourself - intelligence   
 * funny: Rate yourself - being funny   
 * ambition: Rate yourself - ambition  
 * attractive_partner: Rate your partner - attractiveness  
 * sincere_partner: Rate your partner - sincerity   
 * intelligence_partner: Rate your partner - intelligence   
 * funny_partner: Rate your partner - being funny   
 * ambition_partner: Rate your partner - ambition   
 * shared_interests_partner: Rate your partner - shared interests  
 * sports: Your own interests [1-10]  
 * tvsports  
 * exercise  
 * dining  
 * museums  
 * art  
 * hiking  
 * gaming  
 * clubbing  
 * reading  
 * tv  
 * theater  
 * movies  
 * concerts  
 * music  
 * shopping  
 * yoga  
 * interests_correlate: Correlation between participant's and partner's ratings of interests.  
 * expected_happy_with_sd_people: How happy do you expect to be with the people you meet during the speed-dating event?  
 * expected_num_interested_in_me: Out of the 20 people you will meet, how many do you expect will be interested in dating you?  
 * expected_num_matches: How many matches do you expect to get?  
 * like: Did you like your partner?  
 * guess_prob_liked: How likely do you think it is that your partner likes you?   
 * met: Have you met your partner before?  
 * decision: Decision at night of event.
 * decision_o: Decision of partner at night of event.  
 * match: Match (yes/no)

 
Brak ~połowy cech
 """

"""
do odrzucenia
has_null




""" 
 
"""

 wave,
 gender,
 age,
 age_o,
 d_age,
 d_d_age,
 race,
 race_o,
 samerace,
 importance_same_race,
 importance_same_religion,
 d_importance_same_race,
 d_importance_same_religion,
 field,
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
 attractive_o,
 sinsere_o,
 intelligence_o,
 funny_o,
 ambitous_o,
 shared_interests_o,
 d_attractive_o,
 d_sinsere_o,
 d_intelligence_o,
 d_funny_o,
 d_ambitous_o,
 d_shared_interests_o
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
 interests_correlate,
 d_interests_correlate,
 expected_happy_with_sd_people,
 expected_num_interested_in_me,
 expected_num_matches,
 d_expected_happy_with_sd_people,
 d_expected_num_interested_in_me,
 d_expected_num_matches,
 like
 ,guess_prob_liked,
 d_like,
 d_guess_prob_liked,
 met,
 decision,
 decision_o,
 match

"""