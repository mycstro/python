from configparser import ConfigParser
from dbMySql.conMySql import *
import sys, os, math, subprocess


# def set_Tk_var():
#     global stv22
#     stv22 = StringVar()
#     global che44
#     che44 = StringVar()
#     global che45
#     che45 = StringVar()
#     global spinbox
#     spinbox = StringVar()
#     global che66
#     che66 = StringVar()
#     global entry1txt
#     entry1txt = StringVar()
#     global che67
#     che67 = StringVar()

def process_command(text):
    ''' Given a string, returns a string in response. '''
    text = text.strip().lower()
    if text == 'dbconnect':
        t = ConnDB()
        t.dbconnect()
    elif text == 'dbclose':
        t = ConnDB()
        t.dbclose()
    elif text in {'currentdb', 'database', 'current database'} :
        t = CheckDB()
        t.current_database()
    # elif text == 'fetch':
    #     print('ok')
    #     t = f()
    #     qu = input("Select. [one, many, all]: ")
    #     quan = qu.strip().lower()
    #     tabl = input("Which table ['users', 'books']: ")
    #     idnum = input("What is the ID number: ")
    #     qry = "Select * From {} WHERE ID = {}".format(tabl, idnum)
    #     if quan == 'one':
    #         t.query_with_fetchone(qry)
    #     elif quan == 'many':
    #         t.query_with_fetchmany(qry)
    #     elif quan == 'all':
    #         t.query_with_fetchall(qry)
    elif text in {'quit', 'exit'}:
        # clear the input field
        try:
            print('Attempting to quit')
        except AttributeError:
            pass
    else:
        print('Unknown Command')

def cmd_run(self, cmd):
    self.cmd = cmd
    subprocess.call(self.cmd, shell=True)

def get_file_uri(filename):
    return 'file://%s' % filename

config_file_skeleton = """[DEFAULTS]
[market]
# If you want to override the current market dectection,
# set your preferred market here.
area =
[directory]
# Download directory path. By default images are saved to
# /home/[user]/[Pictures]/BingWallpapers/
dir_path =
# Limit the size of the downloaded image directory
# Size should be specified in bytes. The minimum 
# limit is the size of 1 image (whatever size that image is)
# Set to negative value for unlimit. Default value is 100MiB
dir_max_size =
[Variablez]
var1 = '' 
[Stringy]
str1 = ''
[People]
cate = Users, Contacts, Other
    [Users]
    UserNames = Admin, Default
        [Profile]
        Profiles = Admin, Default
            [Admin]
            name: {}

            [Default]
    [Contacts]
    [Other]
[What]
# What has happened or What's going to happen
[When]
# When has it happened or When is it going to happen
[Where]
# Where has it happened or Where is it going to happen
[Why]
# Why did it happen or Why is it going to happen
[Who]
# Who did it or Who is going to do it
# Who did it happen to or Who will it happen to

"""

def get_config_file(self):
    """
    Get the path to the program's config file.

    :return: Path to the program's config file.
    """
    config_dir = os.path.join(os.path.expanduser('~/Documents/Code/Python/milo'), '.config',
                              'milo')
    self.init_dir(config_dir)
    config_path = os.path.join(config_dir, 'config.ini')
    if not os.path.isfile(config_path):
        with open(config_path, 'w') as config_file:
            config_file.write(self.config_file_skeleton)
            config_file.close()
    return config_path

def get_config(self, section, cate='cate'):
    config = ConfigParser()
    config.read(self.get_config_file())
    people_cate = config.get(section, cate)
    if people_cate:
        return people_cate

MARKETS = [1, 2]

def get_market(self):
    """

    In order of preference, this program will use:
    * Config value market.area from desktop_wallpaper_changer.ini
    * Default locale, in case that's a valid Bing market
    * Fallback value is 'en-US'.

    :return: Market
    :rtype: str
    """
    config = ConfigParser()
    config.read(self.get_config_file())
    market_area_override = config.get('market', 'area')
    if market_area_override:
        return market_area_override

    default_loc = (1, 2)
    if default_loc in self.MARKETS:
        return default_loc

    return 'en-US'

def get_download_path(self):
    # By default images are saved to '/home/[user]/[Pictures]/.....'
    default_path = check_output("xdg-user-dir Documents", shell=True).strip().decode("utf-8") + "/Code/Python/milo"

    try:
        config = ConfigParser()
        config.read(self.get_config_file())
        path = config.get('directory', 'dir_path')

        return path or default_path
    except Exception:
        return default_path

def get_directory_limit(self):
    """
    Get the directory sized limit
    """
    config = ConfigParser()
    config.read(self.get_config_file())
    try:
        size = config.getint('directory', 'dir_max_size')
        return size
    except Exception:
        return 100 * 1024 * 1024

def init_dir(self, path):
    """
    Create directory if it doesn't exist.

    :param path: Path to a directory.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def p2_dirscan(self, path):
    files = list()
    size = 0

    for e in os.listdir(path):
        entry = path + "/" + e
        if os.path.isfile(entry) and os.path.splitext(entry)[1] == ".jpg":
            s = os.path.getsize(entry)
            files.append((entry, s))
            size = size + s
    files = sorted(files)
    return files, size

def check_limit(self):
    download_path = self.get_download_path()
    (files, size) = self.p2_dirscan(download_path)
    max_size = self.get_directory_limit()
    while (max_size > 0 and size > max_size and len(files) > 1):
        os.remove(files[0][0])
        size = size - files[0][1]
        del files[0]

# # Replaced to /opt/....
# path_to_program = "/home/mycstro/Documents/Code/Python/milo"

def cvert_fttoin(measure):
    fet, inc = map(int, str(measure).split('.')) ## split by decimel
    ments = int(fet) * 12 ## convert feet into inches
    ments += int(inc) ## add remaining inches
    return ments

def cvert_intoft(measure):
    ments = measure / 12
    ments = round(ments, 1)
    return ments

# # wait
def wait_some():
    os.system("sleep 2")

def chop_some(chop):
    x = chop
    x1 = math.modf(x)
    return x1

def process_file(file_name):
    user_names = []
    passwords = []

    try:
        file_conn = open(file_name)
        data = file_conn.readlines()

        for i in range(len(data)):
            if i % 2 == 0:
                user_names.append(data[i][:-1])
            else:
                passwords.append(data[i][:-1])

        file_conn.close()
    except:
        sys.exit('There was a problem reading the file!')

    return user_names, passwords

# def init(top, gui, *args, **kwargs):
#     global w, top_level, root
#     w = gui
#     # treeViews.set_Tk_var()
#     top_level = top
#     # treeViews.init(root, top)
#     root = top
    # self._ppcate = self.get_config('People')
    # print(self._ppcate)

