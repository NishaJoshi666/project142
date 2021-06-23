import pandas as pd
import numpy as np

df = pd.read_csv('articles.csv')
sharedDf = df.sort_values(['total_events'],ascending=True)
output = sharedDf[['title','url','lang','contentId','authorPersonId','total_events']].head(20).values.tolist()
