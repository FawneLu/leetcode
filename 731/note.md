### 日历问题
我们设两个list分别用来存放calendar和overlap。把输入的（start,end）分别和overlap与calendar里的(i,j)做比对，如果i<end, start>j,证明有overlap，则将（max（start，i），min（end,j））存入overlap中。