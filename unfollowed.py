from unfollowed.utils import IGExtractor
from unfollowed.core.output import TextOutput, HTMLOutput
from unfollowed.core import settings
import os

if __name__ == "__main__":
    settings.initialize()

    zip_path = input("Please enter the file path for your instagram data file: ")
    while not os.path.exists(zip_path) or not zip_path.endswith(".zip"):
        zip_path = input("Input was invalid, please try again: ")

    igextract = IGExtractor(zip_path)

    followers = igextract.get_followers()
    following = igextract.get_following()

    output = None
        
    if settings.use_html():
        output = HTMLOutput(followers, following)
    else:
        output = TextOutput(followers, following)

    output.create_output()
