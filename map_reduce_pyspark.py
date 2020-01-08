"""
Map reduce in pyspark
"""

from pyspark import SparkContext

# create the driver
sc = SparkContext("local", "Name of App")

# read a text file in hdfs, return a RDD object
lines = sc.textFile("hdfs:/path/to/words.txt")

# count of a RDD
print(lines.count())

# sample a RDD
print(lines.take(5))

# flatmap: map, then flatten the results
words = lines.flatMap(lambda line: line.split(" "))

# map: narrow transformation (transformation done locally)
tuples = words.map(lambda word: (word, 1))

# reduce step
# wide transformation (data need to shuffle and transmit across nodes)
counts = tuples.reduceByKey(lambda a,b: (a+b))

# reduce step
# wide transformation (data need to shuffle and transmit across nodes)
counts = tuples.reduceByKey(lambda a,b: (a+b))

# coalesce: reduce RDD partitions
# spark action
counts.coalesce(1).saveAsTextFile('hdfs:/path/to/wordcount')