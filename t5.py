# # # keys = ['Ten', 'Twenty', 'Thirty']
# # # values = [10, 20, 30]

# # # d = {}

# # # # for i,j in zip(keys, values):
# # # #     d[i] = j

# # # d2 = dict(zip(keys, values))
# # # print(d2)

# # # merge python dicts

# # dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# # dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# # d3 = {}
# # d3.update(dict1)
# # d3.update(dict2)
# # print(d3)

# sampleDict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sampleDict['class']['student']['marks']['history'])
# print(sampleDict.get('class').get('student').get('marks', 'NULL').get('history'))