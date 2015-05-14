from os import *
from shutil import *
badprefix = "P"
fnames = listdir('.')
"""
for fname in fnames:
	if fname.startswith(badprefix):
		rename(fname,fname.replace(badprefix,"p"))
		"""
print fnames
for fname in fnames:
	if fname.startswith("roblem"):
		rmdir(fname)
#		move(str(fname),str(fname))
