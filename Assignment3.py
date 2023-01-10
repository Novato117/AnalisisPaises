import pandas as pd
from urllib.request import urlretrieve

urlretrieve('https://gist.githubusercontent.com/aakashns/28b2e504b3350afd9bdb157893f9725c/raw/994b65665757f4f8887db1c85986a897abb23d84/countries.csv', 
            'countries.csv')

countries_df=pd.read_csv('countries.csv')
print(countries_df)
num_countries=countries_df.location.shape
print('There are {} countries in the data set'.format(num_countries))

continents=pd.unique(countries_df.continent)
print(continents)
total_population=countries_df.population.sum()
print("\n\n\n\n total population : ", total_population)
life_expectancy=countries_df.life_expectancy.mean()
print(life_expectancy)

most_populous_df=countries_df.sort_values('population',ascending=True).head(10)

print('\n\n\n',most_populous_df)

countries_df['gdp']=countries_df['population']*countries_df['gdp_per_capita']
print('\n\n\n',countries_df)

country_counts_df=countries_df.groupby('continent').count()

print('\n\n\n\n contador de continente\n\n\n',country_counts_df)

country_counts_df=country_counts_df.location
print('\n\n\n\n paises por continente\n',country_counts_df)

continent_populations_df=countries_df.groupby('continent').sum()
print('\n\n\n\n',continent_populations_df)

print(continent_populations_df['population'])


urlretrieve('https://gist.githubusercontent.com/aakashns/b2a968a6cfd9fbbb0ff3d6bd0f26262b/raw/b115ed1dfa17f10fc88bf966236cd4d9032f1df8/covid-countries-data.csv', 
            'covid-countries-data.csv')

covid_data_df=pd.read_csv('covid-countries-data.csv')
print('\n\n\n\n',covid_data_df)


total_tests_missing=covid_data_df['total_tests'].isna().sum()


print('the data for total test  is missing for {} countries'.format(int(total_tests_missing)))

combined_df=countries_df.merge(covid_data_df,on='location')
print('\n\n\n',combined_df)

combined_df['tests_per_million']=combined_df['total_tests']*1e6/combined_df['population']
combined_df['cases_per_million']=combined_df['total_cases']*1e6/combined_df['population']
combined_df['deaths_per_million']=combined_df['total_deaths']*1e6/combined_df['population']
highest_tests_df=combined_df.sort_values('tests_per_million',ascending=False).head(10)
print('\n\n\n\n\n 10 countries that have highest number of positive cases per million \n\n\n')
print(highest_tests_df)
highest_cases_df=combined_df.sort_values('cases_per_million',ascending=False).head(10)
highest_deaths_df=combined_df.sort_values('deaths_per_million',ascending=False).head(10)
print(highest_cases_df)
print(highest_deaths_df)