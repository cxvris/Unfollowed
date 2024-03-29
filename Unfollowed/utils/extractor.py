'''
All rights reserved.
'''

from zipfile import ZipFile
from whosgone.utils import jsontools

class IGExtractor:

    # path should point to the location of the instagram provided zip-file
    def __init__(self, path):
        self.path = path
    
    # Reads the content of a zipped file and returns them
    # sub_path represents a file path to read from that is relative to the zip file
    def __read_zipped_file(self, sub_path):
        with ZipFile(self.path) as zip:

            # Quick fix for newer instagram data files
            if sub_path not in zip.namelist():
                sub_path = sub_path.replace(".json", "_1.json")

            with zip.open(sub_path) as file:
                return file.read()
    
    def get_followers(self):
        data = self.__read_zipped_file("followers_and_following/followers.json")
        return jsontools.instantiate_users(data, "relationships_followers")


    def get_following(self):
        data = self.__read_zipped_file("followers_and_following/following.json")
        return jsontools.instantiate_users(data, "relationships_following")