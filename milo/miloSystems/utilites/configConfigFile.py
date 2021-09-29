
from configparser import ConfigParser
from logging import debug, warning, error, exception

class WhitespaceFriendlyConfigParser(ConfigParser):
    def get(self, section, option, *args, **kwargs):
        val = super().get(section, option, *args, **kwargs)
        return val.strip('"')

class Config:
    def __init__(self):
        self.debug = False
        self.module = None
        self.database = None
        self.useragent = None
        self.ratelimit = 1.0

        self.username = None
        self.password = None
        self.oauth_key = None
        self.oauth_secret = None

        self.services = dict()

        #Reddit
        self.subreddit = None
        self.r_username = None
        self.r_password = None
        self.r_oauth_key = None
        self.r_oauth_secret = None

        self.new_show_types = list()
        self.record_scores = False

        self.post_title = None
        self.post_title_postfix_final = None
        self.post_body = None
        self.post_formats = dict()

def from_file(file_path):
    parsed = WhitespaceFriendlyConfigParser()
    success = parsed.read(file_path)

    if len(success) == 0:
        print("Failed to load config file")
        return
    else:
        return success

def load_defaults():
    success = from_file()
    if len(success) == 0:
        print("Failed to load config file")
        return

def configServices(parsed):
    config = Config()

    for key in parsed:
        if key.startswith("service."):
            service = key[8:]
            config.services[service] = parsed[key]

    return config


if __name__ == "__main__":
    cfg = ConfigParser()
    ### *** WRITE config file ***
    """
    cfg['configData1'] = {'conf1': 'one', 'conf2': '12', 'conf3': 'false'}
    cfg['configDate2'] = {}
    cfg['configDate2']['config_string'] = 'string' # set "string"
    cfg['configDate2']['config_bool'] = 'true' # set "bool"
    cfg['configDate2']['config_int'] = '21' # set "int"
    cfg['configDate2']['config_float'] = '10.211' 3 set "float"
    
    with open('config.ini', 'w') as configfile:
        cfg.write(configfile)
    """

    ### *** READ config file ***
    """
    cfg.read('config')
    print(cfg.sections()) # return all sections
    print(cfg.items('configData1')) # return section's list
    print(cfg.get('configData1', 'conf1'))
    print(cfg.get('configData1', 'conf2'))
    print(cfg.get('configData1', 'conf3'))
    
    
    print(cfg.get('configData2', 'config_string')) # get "string" object
    print(cfg.getboolean('configData2, 'config_bool')) # get "bool" object
    print(cfg.getint('configData2, 'config_int')) # get "int" object
    print(cfg.getfloat('configData2, 'config_float')) # get "float" object
    """