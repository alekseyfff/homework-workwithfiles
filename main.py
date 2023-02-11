import json

final_dict = {}

with open('purchase_log.txt') as purchases:
  for i, line in enumerate(purchases):
    dict_ = json.loads(line)

    key = dict_['user_id']
    value = dict_['category']

    final_dict[key] = value


with open('visit_log.csv', 'r') as f, open('funnel.csv','w') as f_2:
  for i, line in enumerate(f):
    line = line.strip().split(',')
    if line[0] in final_dict.keys():
      line.append(final_dict[line[0]])
      ad_line = ','.join(line)

      f_2.write(ad_line + '\n')




