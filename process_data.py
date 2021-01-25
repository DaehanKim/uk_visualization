import pandas as pd 
import json
import sys 

DATA_TYPE = sys.argv[1]
THRESHOLD_PER_SE = {'euclidean' : 0.86, 'kl_divergence' : 0.91, 'b_distance':0.97}
print(f"DATA_TYPE is {DATA_TYPE}")
print(f'THRESHOLD is {THRESHOLD_PER_SE[DATA_TYPE]}')

THRESHOLD = 0.9
assert DATA_TYPE in ['euclidean','kl_divergence' ,'b_distance'], "DATA_TYPE must be either 'euclidean', 'kl_divergence' or 'b_distance'!"

df = pd.read_csv(f'raw_data/{DATA_TYPE}.csv', sep=',', header=0, encoding='utf-8')

df['Distance (normalized)'] = 1-df['Distance (normalized)']
df = df.rename(columns={'Distance (normalized)':'Similarity'})
sorted_df = df.sort_values(by='Similarity', ascending=False)

unique_labels = sorted_df['Src label'].unique()
edges_to_display = sorted_df[sorted_df['Similarity'] > THRESHOLD_PER_SE[DATA_TYPE]][['Src label' ,'Dest label']]


nodes = [{"id": label, "group": 1} for label in unique_labels]
links = [{"source": s, "target": t, "value": 1} for s,t in edges_to_display.values]

# print(links[:10])
print(f"number of nodes : {len(nodes)} | number of links : {len(links)}")

resulting_json = {"nodes" : nodes, "links" : links}
# print(df['Distance'].max())
# print(df.head())
with open(f"processed_{DATA_TYPE}.json",'w') as f:
    json.dump(resulting_json, f)