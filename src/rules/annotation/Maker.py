""" This function takes the maker configuration file ctl and overrides settings if found in the relevant section of config.json"""
import os.path
import configparser
import io

def read_maker_opts_ctl(CONFIG, ctl):
    config = configparser.RawConfigParser()
    config.optionxform = str # Return options as they are, do not convert to lowercase
    config.read(ctl)
    # All settings are in the "maker" json_section
    # Loop over all the settings
    for c in config.items("maker"):
        # Check for a matching entry in config.json
        if c[0] in CONFIG:
            # Replace with new setting
            config.set("maker", c[0], CONFIG[c[0]])
    # Place the new configuration in a single string:
    output = io.StringIO()
    config.write(output,space_around_delimiters=False)
    return output.getvalue()

def strip_path_level(path, level = 0):
    head = path
    for i in range(0, level):
        (head, tail) = os.path.split(head)
    return head
