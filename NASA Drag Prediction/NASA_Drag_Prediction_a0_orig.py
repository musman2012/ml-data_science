#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import io
import requests
import numpy

#s=requests.get("E:\Dan Research\Orig Data\Orig_a0_part1.csv").content
c=pd.read_csv(r"E:\Dan Research\Twisted Data\A0\twis_a0_part1.csv") 
c2=pd.read_csv(r"E:\Dan Research\Twisted Data\A0\twis_a0_part2.csv")
c3=pd.read_csv(r"E:\Dan Research\Twisted Data\A0\twis_a0_part4.csv")
c4=pd.read_csv(r"E:\Dan Research\Twisted Data\A0\twis_a0_part5.csv")
c5=pd.read_csv(r"E:\Dan Research\Twisted Data\A0\twis_a0_part6.csv")
c6=pd.read_csv(r"E:\Dan Research\Twisted Data\A0\twis_a0_part7.csv")
c7=pd.read_csv(r"E:\Dan Research\Twisted Data\A0\twis_a0_part8.csv")
c8=pd.read_csv(r"E:\Dan Research\Twisted Data\A0\twis_a0_part9.csv")
c9=pd.read_csv(r"E:\Dan Research\Twisted Data\A0\twis_a0_part10.csv")
c10=pd.read_csv(r"E:\Dan Research\Twisted Data\A0\twis_a0_part11.csv")
print(c)


# In[7]:


from astropy.table import Table, Column

t = Table(names=('Inputs', 'Covariance', 'Correlation'), dtype=('S5','f4', 'f4'))

c.X = c.X[:].astype(numpy.float)
c.Y = c.Y[:].astype(numpy.float)
c.Z = c.Z[:].astype(numpy.float)
c.Cp = c.Cp[:].astype(numpy.float)
cov_matrix = numpy.cov(c.X[:], c.Y[:])
corr_matrix = numpy.corrcoef(c.X[:], c.Y[:])

t.add_row(('X,Y,1', cov_matrix[0,1], corr_matrix[0,1]))

cov_matrix = numpy.cov(c.X[:], c.Z[:])
corr_matrix = numpy.corrcoef(c.X[:], c.Z[:])

t.add_row(('X,Z,1', cov_matrix[0,1], corr_matrix[0,1]))

cov_matrix = numpy.cov(c.Y[:], c.Z[:])
corr_matrix = numpy.corrcoef(c.Y[:], c.Z[:])

t.add_row(('Y,Z,1', cov_matrix[0,1], corr_matrix[0,1]))

##################### Part 2 ###########################

c2.X = c2.X[:].astype(numpy.float)
c2.Y = c2.Y[:].astype(numpy.float)
c2.Z = c2.Z[:].astype(numpy.float)
c2.Cp = c2.Cp[:].astype(numpy.float)
#cov_matrix = numpy.cov(c2.X[:], c2.Y[:])
#corr_matrix = numpy.corrcoef(c2.X[:], c2.Y[:])

#t.add_row(('X,Y,2', cov_matrix[0,1], corr_matrix[0,1]))

cov_matrix = numpy.cov(c2.X[:], c2.Z[:])
corr_matrix = numpy.corrcoef(c2.X[:], c2.Z[:])

t.add_row(('X,Z,2', cov_matrix[0,1], corr_matrix[0,1]))

#cov_matrix = numpy.cov(c2.Y[:], c2.Z[:])
#corr_matrix = numpy.corrcoef(c2.Y[:], c2.Z[:])

#t.add_row(('Y,Z,2', cov_matrix[0,1], corr_matrix[0,1]))

##################### Part 3 ###########################

c3.X = c3.X[:].astype(numpy.float)
c3.Y = c3.Y[:].astype(numpy.float)
c3.Z = c3.Z[:].astype(numpy.float)
c3.Cp = c3.Cp[:].astype(numpy.float)
#cov_matrix = numpy.cov(c3.X[:], c3.Y[:])
#corr_matrix = numpy.corrcoef(c3.X[:], c3.Y[:])

#t.add_row(('X,Y,3', cov_matrix[0,1], corr_matrix[0,1]))

cov_matrix = numpy.cov(c3.X[:], c3.Z[:])
corr_matrix = numpy.corrcoef(c3.X[:], c3.Z[:])

t.add_row(('X,Z,3', cov_matrix[0,1], corr_matrix[0,1]))

#cov_matrix = numpy.cov(c3.Y[:], c3.Z[:])
#corr_matrix = numpy.corrcoef(c3.Y[:], c3.Z[:])

#t.add_row(('Y,Z,3', cov_matrix[0,1], corr_matrix[0,1]))

##################### Part 4 ###########################

c4.X = c4.X[:].astype(numpy.float)
c4.Y = c4.Y[:].astype(numpy.float)
c4.Z = c4.Z[:].astype(numpy.float)
c4.Cp = c4.Cp[:].astype(numpy.float)
#cov_matrix = numpy.cov(c4.X[:], c4.Y[:])
#corr_matrix = numpy.corrcoef(c4.X[:], c4.Y[:])

#t.add_row(('X,Y,4', cov_matrix[0,1], corr_matrix[0,1]))

cov_matrix = numpy.cov(c4.X[:], c4.Z[:])
corr_matrix = numpy.corrcoef(c4.X[:], c4.Z[:])

t.add_row(('X,Z,4', cov_matrix[0,1], corr_matrix[0,1]))

#cov_matrix = numpy.cov(c4.Y[:], c4.Z[:])
#corr_matrix = numpy.corrcoef(c4.Y[:], c4.Z[:])

#t.add_row(('Y,Z,4', cov_matrix[0,1], corr_matrix[0,1]))

##################### Part 5 ###########################

c5.X = c5.X[:].astype(numpy.float)
c5.Y = c5.Y[:].astype(numpy.float)
c5.Z = c5.Z[:].astype(numpy.float)
c5.Cp = c5.Cp[:].astype(numpy.float)
#cov_matrix = numpy.cov(c5.X[:], c5.Y[:])
#corr_matrix = numpy.corrcoef(c5.X[:], c5.Y[:])

#t.add_row(('X,Y,5', cov_matrix[0,1], corr_matrix[0,1]))

cov_matrix = numpy.cov(c5.X[:], c5.Z[:])
corr_matrix = numpy.corrcoef(c5.X[:], c5.Z[:])

t.add_row(('X,Z,5', cov_matrix[0,1], corr_matrix[0,1]))

#cov_matrix = numpy.cov(c5.Y[:], c5.Z[:])
#corr_matrix = numpy.corrcoef(c5.Y[:], c5.Z[:])

#t.add_row(('Y,Z,5', cov_matrix[0,1], corr_matrix[0,1]))


##################### Part 6 ###########################

c6.X = c6.X[:].astype(numpy.float)
c6.Y = c6.Y[:].astype(numpy.float)
c6.Z = c6.Z[:].astype(numpy.float)
c6.Cp = c6.Cp[:].astype(numpy.float)
#cov_matrix = numpy.cov(c6.X[:], c6.Y[:])
#corr_matrix = numpy.corrcoef(c6.X[:], c6.Y[:])

#t.add_row(('X,Y,6', cov_matrix[0,1], corr_matrix[0,1]))

cov_matrix = numpy.cov(c6.X[:], c6.Z[:])
corr_matrix = numpy.corrcoef(c6.X[:], c6.Z[:])

t.add_row(('X,Z,6', cov_matrix[0,1], corr_matrix[0,1]))

#cov_matrix = numpy.cov(c6.Y[:], c6.Z[:])
#corr_matrix = numpy.corrcoef(c6.Y[:], c6.Z[:])

#t.add_row(('Y,Z,6', cov_matrix[0,1], corr_matrix[0,1]))


##################### Part 7 ###########################

c7.X = c7.X[:].astype(numpy.float)
c7.Y = c7.Y[:].astype(numpy.float)
c7.Z = c7.Z[:].astype(numpy.float)
c7.Cp = c7.Cp[:].astype(numpy.float)
#cov_matrix = numpy.cov(c6.X[:], c6.Y[:])
#corr_matrix = numpy.corrcoef(c6.X[:], c6.Y[:])

#t.add_row(('X,Y,6', cov_matrix[0,1], corr_matrix[0,1]))

cov_matrix = numpy.cov(c7.X[:], c7.Z[:])
corr_matrix = numpy.corrcoef(c7.X[:], c7.Z[:])

t.add_row(('X,Z,7', cov_matrix[0,1], corr_matrix[0,1]))


##################### Part 8 ###########################

c8.X = c8.X[:].astype(numpy.float)
c8.Y = c8.Y[:].astype(numpy.float)
c8.Z = c8.Z[:].astype(numpy.float)
c8.Cp = c8.Cp[:].astype(numpy.float)
#cov_matrix = numpy.cov(c6.X[:], c6.Y[:])
#corr_matrix = numpy.corrcoef(c6.X[:], c6.Y[:])

#t.add_row(('X,Y,6', cov_matrix[0,1], corr_matrix[0,1]))

cov_matrix = numpy.cov(c8.X[:], c8.Z[:])
corr_matrix = numpy.corrcoef(c8.X[:], c8.Z[:])

t.add_row(('X,Z,8', cov_matrix[0,1], corr_matrix[0,1]))


##################### Part 9 ###########################

c9.X = c9.X[:].astype(numpy.float)
c9.Y = c9.Y[:].astype(numpy.float)
c9.Z = c9.Z[:].astype(numpy.float)
c9.Cp = c9.Cp[:].astype(numpy.float)
#cov_matrix = numpy.cov(c6.X[:], c6.Y[:])
#corr_matrix = numpy.corrcoef(c6.X[:], c6.Y[:])

#t.add_row(('X,Y,6', cov_matrix[0,1], corr_matrix[0,1]))

cov_matrix = numpy.cov(c9.X[:], c9.Z[:])
corr_matrix = numpy.corrcoef(c9.X[:], c9.Z[:])

t.add_row(('X,Z,9', cov_matrix[0,1], corr_matrix[0,1]))


##################### Part 10 ###########################

c10.X = c10.X[:].astype(numpy.float)
c10.Y = c10.Y[:].astype(numpy.float)
c10.Z = c10.Z[:].astype(numpy.float)
c10.Cp = c10.Cp[:].astype(numpy.float)
#cov_matrix = numpy.cov(c6.X[:], c6.Y[:])
#corr_matrix = numpy.corrcoef(c6.X[:], c6.Y[:])

#t.add_row(('X,Y,6', cov_matrix[0,1], corr_matrix[0,1]))

cov_matrix = numpy.cov(c10.X[:], c10.Z[:])
corr_matrix = numpy.corrcoef(c10.X[:], c10.Z[:])

t.add_row(('X,Z,10', cov_matrix[0,1], corr_matrix[0,1]))

print(t)


# In[ ]:




