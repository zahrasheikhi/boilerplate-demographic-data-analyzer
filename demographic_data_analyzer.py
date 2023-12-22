import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    df=pd.read_csv('adult.data.csv')
    #print(df.head(3))
    races=df['race'].unique()
    s_race={}
    for i in races:
        s_race[i]=len(df.loc[df['race']==i])

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count =pd.Series(s_race)

    # What is the average age of men?
    average_age_men =np.average(df[df['sex']=='Male']['age'])

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors =(len(df.loc[df['education']=='Bachelors'])*100)/len(df)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[df['education'].isin(["Bachelors","Masters","Doctorate"])]
    lower_education = df.loc[~df['education'].isin(["Bachelors","Masters","Doctorate"])]
    # percentage with salary >50K
    higher_education_rich =len(higher_education.loc[higher_education['salary']=='>50K'])*100/len(higher_education)
    lower_education_rich = len(lower_education.loc[lower_education['salary']=='>50K'])*100/len(lower_education)
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = np.min(df['hours-per-week'])
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers =df.loc[df['hours-per-week']==min_work_hours]
    rich_percentage =len(num_min_workers.loc[num_min_workers['salary']=='>50K'])*100/len(num_min_workers)

    # What country has the highest percentage of people that earn >50K?
    list_highest_earning_country=(df.loc[df['salary']=='>50K']['native-country']).value_counts()
    highest_earning_country =list_highest_earning_country.keys()[0]
    #Countries_name_count=highest_earning_country.value_counts()
    highest_earning_country_percentage= (list_highest_earning_country.values[0]*100)/sum(list_highest_earning_country.values)
    #############Calculating percentage
    #print(sum(Countries_name_count.values))
    #percentage_highest_country = (Countries_name_count.values[0]*100)/sum(Countries_name_count.values)
    #print(percentage_highest_country)
    
    # Identify the most popular occupation for those who earn >50K in India.
    Indian_Highest_Earning=df.loc[(df['native-country']=='India') & (df['salary']=='>50K')]['occupation']
#    print(Indian_Highest_Earning)
    top_IN_occupation = (Indian_Highest_Earning.value_counts()).keys()[0]
 #   print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    
  #  print(top_IN_occupation)
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data(print_data=True)
