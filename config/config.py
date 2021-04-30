import configparser
import os


def config_parser(section, key):
    config = configparser.ConfigParser()
    try:
        config.read(os.path.join(os.path.dirname(__file__)+"/config_files/config_prod.ini"))
        result = config.get(section, key)
        return result
    except config.NoOptionError:
        raise Exception("There was a problem with configuration file. The key does not exist.")
    except config.NoSectionError:
        raise Exception("There was a problem with configuration file. The key does not exist.")


def config_parser_section(section):
    parser = config = configparser.ConfigParser()
    try:
        parser.read(os.path.dirname(__file__)+"/config_files/config_prod.ini")
        result = dict(parser.items(section))
        return result
    except config.NoSectionError:
        raise Exception("There was a problem with configuration file. The key does not exist.")


def load_file(filename):
    path_software_list = os.path.join(os.path.dirname(__file__) + "/config_files/"+filename)
    keyword_list = []
    with open(path_software_list, "r") as ins:
        for line in ins:
            keyword_list.append(line.strip())
        ins.close()
    return keyword_list
