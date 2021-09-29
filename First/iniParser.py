from configparser import ConfigParser

# filename = 'config.ini'
# section ='mysql'


def read_config(filename, section):
    """ Read configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of configuration
    :return: a dictionary of parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    result = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            result[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    # print(result)
    return result

def write_config(filename, section, option, value):
    """ Write a dictionary object to the configuration file and return
    :param filename: name of the configuration file
    :param section: section of configuration
    :param option: option in configuration
    :param value: value for option in configuration
    :return: a dictionary of parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    results = {}
    if parser.has_section(section):
        ps = parser.sections()
        if section in ps:
            s = section
            print(s, "...Located")
    else:
        print("Creating {} now...".format(section))
        parser[section] = {}
        with open('config.ini', 'w') as configfile:
            parser.write(configfile)
            print(section, "...has been created")
    if parser.has_option(section, option):
        po = parser.options(section)
        if option in po:
            o = option
            print(s, o, "...Located")
            return o
    else:
        print("Creating {}, {}: {} now".format(section, option, value))
        parser[section][option] = value
        with open('config.ini', 'w') as configfile:
            parser.write(configfile)
            print(section, option, "=", value, "...has been created")
    # return results

# write_config('config.ini', 'mysql1', 'database', 'poo')
# read_config('config.ini', 'mysql1')

