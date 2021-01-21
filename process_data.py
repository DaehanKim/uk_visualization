import pandas as pd 
import json

DATA_TYPE = 'euclidean'
THRESHOLD = 0.9
assert DATA_TYPE in ['euclidean','kl_divergence'], "DATA_TYPE must be either 'euclidean' or 'kl_divergence'!"

df = pd.read_csv(f'raw_data/{DATA_TYPE}.csv', sep=',', header=0, encoding='utf-8')

if DATA_TYPE == 'euclidean':
    df['Distance'] /= df['Distance'].max()
    df['Distance'] = 1-df['Distance']
    df = df.rename(columns={'Distance':'Similarity'})
    sorted_df = df.sort_values(by='Similarity', ascending=False)
else : 
    pass 

unique_labels = sorted_df['Src label'].unique()
edges_to_display = sorted_df[sorted_df['Similarity'] > THRESHOLD][['Src label' ,'Dest label']]

# print(edges_to_display.head().values)

nodes = [{"id": label, "group": 1} for label in unique_labels]
links = [{"source": s, "target": t, "value": 1} for s,t in edges_to_display.values]

# print(links[:10])
print(f"number of nodes : {len(nodes)} | number of links : {len(links)}")

resulting_json = {"nodes" : nodes, "links" : links}
# print(df['Distance'].max())
# print(df.head())
with open(f"processed_{DATA_TYPE}.json",'w') as f:
    json.dump(resulting_json, f)