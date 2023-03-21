import numpy as np
rouge_all_sorted = []
rouge_all = []
with open('rouge_result.txt','r') as f:
    for line in f:
        rouge_all_sorted.append(line)
        rouge_all.append(line)
for i in range(len(rouge_all_sorted)):
    rouge_all_sorted[i] = float(rouge_all_sorted[i][0:7])
    rouge_all[i] = float(rouge_all[i][0:7])
# sort_index = list(range(0,281))
# for i in range(1, len(rouge_all_sorted)):
#     for j in range(0, len(rouge_all_sorted)-i):
#         if rouge_all_sorted[j] > rouge_all_sorted[j+1]:
#             rouge_all_sorted[j], rouge_all_sorted[j + 1] = rouge_all_sorted[j + 1], rouge_all_sorted[j]
#             sort_index[j], sort_index[j + 1] = sort_index[j + 1], sort_index[j]
# print(rouge_all_sorted)
# print(sort_index)
import json
tmp = []
for line in open('data/QMSum/qmsum_test_with_oracle.jsonl','r'):
    tmp.append(json.loads(line))
# print(tmp[0]['specific_query_list'][6]['query'])

num_specific = []
num_general = []
index_specific = []
index_general = []

#计算每个会议有多少gen和spec的query
for i in range(len(tmp)):
    num_specific.append(len(tmp[i]['specific_query_list']))
    num_general.append(len(tmp[i]['general_query_list']))

#将gen和spec的query的index记录下来
curr_index = -1
for i in range(len(num_general)):
    for j in range(num_general[i]):
        curr_index += 1
        index_general.append(curr_index)
    for j in range(num_specific[i]):
        curr_index += 1
        index_specific.append(curr_index)
# print(index_specific)
# print(index_general)
# print(tmp[8]["specific_query_list"][3])
# print(num_general)
# print(num_specific)

#将rouge score和query对应起来和计算两种query的std
index_spec_rouge = {}
index_gen_rouge = {}
rouge_spec = []
rouge_gen = []
for i in index_general:
    index_gen_rouge[i] = rouge_all[i]
    rouge_gen.append(rouge_all[i])
for i in index_specific:
    index_spec_rouge[i] = rouge_all[i]
    rouge_spec.append(rouge_all[i])
# print(index_gen_rouge)
# print(index_spec_rouge)
# print("\n\n\n")
# print(np.std(rouge_gen,ddof = 1))
# print(np.std(rouge_spec,ddof = 1))

#根据rouge排序好的两种query
spec_rouge_sorted = sorted(index_spec_rouge.items(), key=lambda x: x[1], reverse=True)
gen_rouge_sorted = sorted(index_gen_rouge.items(), key=lambda x: x[1], reverse=True)
# print(spec_rouge_sorted)
# print(gen_rouge_sorted)

#前三99，158，214，中三111，166，209，后三245，8，243     这些是指总的里面第几条query
# print(tmp[]['general_query_list'][])
# print(tmp[]['general_query_list'][])
# print(tmp[]['general_query_list'][])
# print(tmp[13]['specific_query_list'][1]['query'])
# print(tmp[20]['specific_query_list'][2]['query'])
# print(tmp[26]['specific_query_list'][10]['query'])

# print(tmp[14]['specific_query_list'][4]['query'])
# print(tmp[20]['specific_query_list'][10]['query'])
# print(tmp[26]['specific_query_list'][5]['query'])

# print(tmp[29]['specific_query_list'][4]['query'])
# print(tmp[0]['specific_query_list'][7]['query'])
# print(tmp[14]['specific_query_list'][2]['query'])

#前三44()，254()，261()，后三203(27)，240(31)，68(10)
# print(tmp[]['specific_query_list'][])
# print(tmp[]['specific_query_list'][])
# print(tmp[]['specific_query_list'][])
# print(tmp[26]['general_query_list'][0]['query'])
# print(tmp[30]['general_query_list'][0]['query'])
# print(tmp[9]['general_query_list'][0]['query'])







#---------------------没用的-------------------------

#两种query的均分
# sum_rouge_spec = 0
# sum_rouge_gen = 0 
# for i in range(len(spec_rouge_sorted)):
#     sum_rouge_spec += spec_rouge_sorted[i][1]
# for i in range(len(gen_rouge_sorted)):
#     sum_rouge_gen += gen_rouge_sorted[i][1]
# print(sum_rouge_spec/len(spec_rouge_sorted))
# print(sum_rouge_gen/len(gen_rouge_sorted))