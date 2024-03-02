import os
'''
What we are planning on doing.

1. Get a list of the file names
2. Extract the place names from the file names
3. Make a directory for each place name
4. Move files into the right directories

Functions we ar going to need:
os.listdir() Method

os.rename(current_file_name, os.path.join(dest_dir, new_name))

os.mkdir(path, mode=0o777, *, dir_fd=None)
Create a directory named path with numeric mode mode.

'''


# 1. Get a list of the file names
os.chdir("Photos")
originals = os.listdir()

print(originals)
