import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

pd.options.mode.chained_assignment = None

path = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/10-06-2021.csv"

df = pd.read_csv(path)

df.head() #5 is default value

df.info()

df.drop(["FIPS","Admin2","Province_State","Last_Update","Lat","Long_","Recovered","Active","Combined_Key","Case_Fatality_Ratio","Incident_Rate"],axis=1,inplace=True)

df.head()

df.rename(columns={'Country_Region':'Country'},inplace=True)

df.head()

world = df.groupby('Country').sum()

world.head()

world.reset_index(inplace=True)

world.shape

world.sort_values(by=['Confirmed'],ascending=False,inplace=True)

world.head()

top20=world[0:20]

x1=top20['Confirmed']
z1=top20['Deaths']
y1=top20['Country']

plt.figure(figsize=(8,7))
sns.barplot(x=x1,y=y1,palette='rocket')
plt.title('Top 20 Countries based on number of confirmed cases')
plt.show()

plt.figure(figsize=(8,7))
sns.barplot(x=z1,y=y1,palette='rocket')
plt.title('Top 20 Countries based on number of deaths')
plt.show()

top5 = top20[0:5]

Recovered=[34392326,33200258,20554936,6528673,6799230]

top5['Recovered']=Recovered

x1=top5['Confirmed']
x2=top5['Recovered']
y1=top5['Country']

plt.figure(figsize=(6,3))
sns.barplot(x=x1,y=y1,palette="crest")
sns.barplot(x=x2,y=y1,palette='rocket')

j=0
for i in x1:
    plt.text(i-7e6,0+j,i,fontdict={'color':'white'})
    #plt.text(x-coordinate,y-coordinate,message)
    j+=1

fig = px.choropleth(world, locations="Country",
                    color="Confirmed",
                    locationmode='country names',
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='ice_r',
                   range_color=[1e3,5e6])

fig.show()
