'''
ScriptName：一键分词脚本
Author：Larus
Contatct: hi@larus.memoryview
Introduction: 将需要分词的文本以「text.txt」命名，然后与wordCount.py放在一起。执行wordCount.py脚本即可。
'''

import jieba
import jieba.analyse
import xlwt

wbk = xlwt.Workbook(encoding = 'ascii')
sheet = wbk.add_sheet('wordCount')

word_lst = []
key_list = []
for line in open('text.txt',encoding='utf-8'):
    item = line.strip('\n\r').split('\t')
    tags = jieba.analyse.extract_tags(item[0])
    for t in tags:
        word_lst.append(t)
    
word_dict = {}
with open('wordCount.txt','w') as wf2:

    for item in word_lst:
        if item not in word_dict:
            word_dict[item] = 1
        else:
            word_dict[item] += 1
            
    
    orderList = list(word_dict.values())
    orderList.sort(reverse=True)
        # print orderList
    for i in range(len(orderList)):
        for key in word_dict:
            if word_dict[key]==orderList[i]:
                wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                key_list.append(key)
                word_dict[key]=0
                
for i in range(len(key_list)):
    sheet.write(i, 1, label = orderList[i])
    sheet.write(i, 0, label = key_list[i])
    wbk.save('wordCount.xls') #保存为 wordCount.xls文件
