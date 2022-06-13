import os
from unittest import result

def build_ads_file(file_name, stream_name):
    return file_name + ":" + stream_name

decoy = "benign.txt"

with open("benign.txt:commands.txt") as f:
    for line in f:
        os.system(line + " >> " + "benign.txt:results.txt")
