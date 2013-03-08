#!/usr/bin/python
# -*- coding: utf-8 -*-
# Name    : File Ctime Analyzer
# Author  : wofeiwo#80sec.com
# Version : 1.0
# Date    : 2010-2-1

# 比对文件系统中改动时间异常的文件



import sys,os,string,re

from datetime import datetime, timedelta



if len(sys.argv) <2 and len(sys.argv) >4 :

    print "Usage: %s <WebRoot> [IgnoreTime] [filenumber]" % sys.argv[0]

    sys.exit()



path = os.path.realpath(sys.argv[1])



fsDict = {}

tmp = {}

fsList = []



if len(sys.argv) >= 3 :

    iTime = int(sys.argv[2])

else:

    iTime = 5

    

if len(sys.argv) == 4 :

    fnum = int(sys.argv[3])

else:

    fnum = 5



for root, dirs, names in os.walk(path):

    for f in names:

        file = os.path.join(root, f)

        ctime = datetime.fromtimestamp(os.lstat(file).st_ctime)            

        fsDict[file] = ctime

     

flag = False



for i in fsDict.items():

    for k in tmp.keys():

        flag = False   

        if (i[1] - k >= timedelta(minutes = -iTime)) and (i[1] - k <= timedelta(minutes = iTime)):

            tmp[k].append(i[0])

            flag = True

            break

    if not flag:

        tmp[i[1]] = [i[0]]


a = tmp.keys()

a.sort()



for k in a:

    print "key:", k.isoformat()[:16], "(正负%d分钟)" % iTime

    print "value:"

    if len(tmp[k])>fnum:

        print "%d items." % len(tmp[k])

    else:

        for v in tmp[k]:

            print v

    print "-------------------------------------------------------------------------------"