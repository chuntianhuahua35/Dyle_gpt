import json
from nltk.tokenize import word_tokenize

mode = "train"

def process_line_train(idx):
    #???????
    # if mode != "train":
    #     return []
    print('idx----------------------------')
    print(idx)
    if idx == 1349:
        return []

    # Update the path
    with open('/home/zixuandeng_alan/Dyle_chatgpt/QMSum/ALL/greedy/index_{}/{}.dec'.format(mode, idx), 'r') as f:
        line = f.read()
        line = line.lstrip('[')
        line = line.rstrip(']\n')
        # print(line)
        line_list = [int(x) for x in line.split(',')]
        # print(line_list)
        return line_list

# Download the QMSum datasets and set the path
path = '/home/zixuandeng_alan/Dyle_chatgpt/QMSum/ALL/jsonl/{}.jsonl'.format(mode)
data = []
with open(path) as f:
    for line in f:
        data.append(json.loads(line))

idx = 0
for i in range(len(data)):
    text = []
    ref = []
    print(i)
    for j in range(len(data[i]['meeting_transcripts'])):
        text.append(' '.join(word_tokenize(data[i]['meeting_transcripts'][j]['content'].lower())))
    
    #因为这里有个greedy所以先跑qmsum_oracle
    for j in range(len(data[i]['general_query_list'])):
        data[i]['general_query_list'][j]['greedy_oracle_idx'] = process_line_train(idx)
        idx += 1
    for j in range(len(data[i]['specific_query_list'])):
        data[i]['specific_query_list'][j]['greedy_oracle_idx'] = process_line_train(idx)
        idx += 1
    print('{}: Finished {} pairs'.format(mode, idx))

# Update the path
with open('/home/zixuandeng_alan/Dyle_chatgpt/QMSum/ALL/greedy/{}_oracle.jsonl'.format(mode), 'w') as outfile:
    for entry in data:
        json.dump(entry, outfile)
        outfile.write('\n')
