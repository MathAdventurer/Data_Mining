# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 18:08:50 2018

@author: Neal
"""

jon = """琼恩·雪诺（Jon Snow）是美国作家乔治·R·R·马丁的著名长篇史诗奇幻小说系列《冰与火之歌》中的主要人物之一，POV章节数暂排第二。
琼恩出生于伊耿历283 AC年，身份是临冬城公爵艾德·史塔克的私生子，在篡夺者战争结束后被从南方带回，并同艾德的嫡生子女一同在临冬城长大。
他拥有一只患有白化症的冰原狼“白灵”。在小说故事的开始，琼恩北上加入守夜人去镇守绝境长城。
关于琼恩身世的争议很大，故事中艾德·史塔克本人对琼恩母亲的身份守口如瓶，琼恩也一直不知道自己母亲是谁。
有很多传言说他是艾德与星坠城的亚夏拉·戴恩小姐之子，艾德则对国王劳勃·拜拉席恩说琼恩的母亲是一个叫薇拉的女子，而甜姐岛伯爵高德瑞奇·波内尔则认为琼恩是艾德和咬人湾一个渔夫的女儿所生。
但是书迷群中许多读者推测琼恩是雷加·坦格利安与莱安娜·史塔克之子。"""

file_path = "./week3/data/GOT.txt"

f = open(file_path,"a+")  # a+ 用于创建文件
f.write(jon)
f.close()

#open file with write mode and manage the file by variable wf
with open(file_path,'w',encoding='utf8') as wf:
    #save the string to the file
    wf.write(jon)


#open file and manage the file by variable rf
with open(file_path,'r',encoding='utf8') as rf:
    # read the whole content to jon_new in one batch
    jon_new = rf.read()
print(jon_new)

print("\n=======Read in lines==========")
#open file and manage the file by variable rf
with open(file_path,'r',encoding='utf8') as rf:
    # read the whole content to jon_new in batches of lines
    for line in rf:
        print(line,end='')


