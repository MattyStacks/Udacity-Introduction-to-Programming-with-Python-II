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

def extract_place(filename):
    split_filename = filename.split("_")
    extracted_place = split_filename[1]
    #SHORTHAND return filename.split("_")[1]
    return extracted_place

def make_place_directories(places):
    for place in places:
        os.mkdir(place)

def organize_photos(directory):
    # 1. Get a list of the file names
    os.chdir(directory)
    originals = os.listdir()

    print(originals)
    places = []  

    for file in originals:
        place = extract_place(file)
        if place not in places:
            places.append(place)

    print(places)

    # print(extract_place("2016-11-04_Berlin_09/42/22.jpg"))
    # print(extract_place("2018-01-03_Oahu_21/51/57.jpg"))
    # print(extract_place("2018-01_Scottland_11/51/27.jpg"))

    make_place_directories(places)

    for file in originals:
        place = extract_place(file)
        os.rename(file, os.path.join(place, file))

if __name__ == '__main__':
    organize_photos("Photos")