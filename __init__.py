import os

global VLPB_LIB_PATH
VLPB_LIB_PATH = os.path.dirname(os.path.realpath(__file__)) + "/src/"

########################
##  Global Functions  ##
########################
import os.path

def strip_path_level(path, level = 0):
    head = path
    for i in range(0, level):
        (head, tail) = os.path.split(head)
    return head
