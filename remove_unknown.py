def clean_data(text):
    text = text.replace('{ vocalsound } ', '')
    text = text.replace('{ disfmarker } ', '')
    text = text.replace('a_m_i_', 'ami')
    text = text.replace('l_c_d_', 'lcd')
    text = text.replace('p_m_s', 'pms')
    text = text.replace('t_v_', 'tv')
    text = text.replace('{ pause } ', '')
    text = text.replace('{ nonvocalsound } ', '')
    text = text.replace('{ gap } ', '')
    return text
def tokenize(sent):
    tokens = ' '.join(word_tokenize(sent.lower()))
    return tokens

import json
from nltk import word_tokenize

tmp = []
for line in open('data/QMSum/qmsum_val_with_oracle.jsonl','r'):
    tmp.append(json.loads(line))

session = tmp[0]['meeting_transcripts'][2]
# dialogue = [clean_data(turn['speaker'].lower() + ': ' + tokenize(turn['content']))
#                             for turn in session['meeting_transcripts']]
text = tmp[0]['meeting_transcripts'][0]
speaker = session['speaker'].lower()
content = tokenize(session['content'])
clean = clean_data(speaker+ ': ' +content)
print(clean)
print(session)