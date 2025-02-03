
import pandas as pd
import numpy as np

# Path to your TSV file
file_path = 'occurrence_trimmed2.tsv'

df_full = pd.read_csv(file_path, sep='\t', header=None, low_memory=False)

df_notnull = df_full[df_full[8].notnull() & df_full[28].notnull() & df_full[18].notnull() & df_full[31].notnull() & df_full[32].notnull() & df_full[33].notnull()]

df = df_notnull.copy()

df.rename(columns={31: 'year', 32: 'month', 33: 'day', 18: 'vernacularName', 8: 'individualCount', 28: 'stateProvince'},inplace=True)

df['date'] = pd.to_datetime(df.loc[:, ['year', 'month', 'day']])

# Set the date column as the index
df.set_index('date', inplace=True)

df_sub = df[['vernacularName', 'individualCount', 'stateProvince','year', 'month', 'day']]

df_group_month = df.groupby('month')['individualCount'].sum()

import plotly.graph_objects as go
import plotly.express as px

fig1 = px.bar(df_group_month, x=df_group_month.index, y='individualCount')
fig1.write_html('month.html')

data_Teal = df_sub.query("vernacularName == 'Grey Teal'")

data_Teal = data_Teal.sort_index()

fig = px.bar(data_Teal, x='year', y='individualCount', color='stateProvince')
fig.write_html('Teal.html')

fig_go = go.Figure([
    go.Bar(
        x=data_Teal.year.unique(), 
        y=data_Teal.groupby('year')['individualCount'].sum()
        )
    ])
fig_go.write_html('Teal.html')

###

import matplotlib.pyplot as plt

grouped_data = df_sub.groupby('vernacularName')['individualCount'].sum()

# Plot the grouped data as a bar chart
grouped_data.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Sum of Individual Counts by Vernacular Name')
plt.xlabel('Vernacular Name')
plt.ylabel('Sum of Individual Counts')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

import plotly.express as px

fig = px.bar(monthly_resampled, x=monthly_resampled.index, y=8)

fig.show()

