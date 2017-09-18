
''' 
	rename image with current folder with jpg extension.

'''

import os
from os import rename, listdir

relevant_path = "."
included_extensions = ['jpg']
file_names = [fn for fn in os.listdir(relevant_path)
                      if any(fn.endswith(ext) for ext in included_extensions)]

fnames = listdir(relevant_path)
for i,fname in enumerate(file_names):
	rename(fname,"face_" + str(i+1)+ ".jpg" )

