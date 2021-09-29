from __future__ import print_function
from logging import debug, warning, error, exception
import mysql.connector as mysqlc
from mysql.connector import errorcode
from functools import wraps, lru_cache
from iniParser import read_config
from unidecode import unidecode
from typing import Set

import sqlite3, re
import os

import tables as t
from .models import Show, ShowType, Stream, Service, LinkSite, Link, Episode, EpisodeScore, UnprocessedStream, \
    UnprocessedShow


# Change to the current directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))


class ConnDB:

    def __init__(self):
        print("\nStarting MySql Server Connector")
        self._dbconfig = read_config
        self._f = 'config.ini'
        print("Configuration loaded")

    def dbconnect(self):
        """Connects to MySql Server. """
        try:
            print('\nConnecting to MySql Server...')
            _config = self._dbconfig(self._f, 'mysql')
            conn = mysqlc.connect(**_config)
            if conn.is_connected():
                print("MySql Server is connected.")
                global CONN, CURSOR
                CONN = conn
                CURSOR = conn.cursor()
                return conn
            else:
                print('MySql Server connection failed')
        except mysqlc.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("The credentials you've entered is incorrect")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            conn.close()
        finally:
            print('\nMySql Server connection is open')

    def dbclose(self):

        """Close connection to MySql Server. """
        global CONN, CURSOR
        try:
            if CONN.is_connected():
                print("Closing MySql Server connection!")
                CONN.close()
                CONN = ""
                CURSOR = ""
                print("MySql Server has been disconnected")
            else:
                print("MySql Server connection is closed.")
        except mysqlc.Error as error:
            print(error)


class CheckDB:

    def __init__(self):
        print("Checking Database")
        if CURSOR:
            self.cursor = CURSOR
            self._conn1 = CONN
        else:
            self._conn1 = ConnDB().dbconnect()
            self.cursor = self._conn1.cursor()

    def check_database(self, db_name):
        try:
            self.cursor.execute("USE {}".format(db_name))
            print("Database {} exist".format(db_name))
        except mysqlc.Error as err:
            print("{}".format(err))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database {} does not exists.".format(db_name))
            else:
                print(err)

    def current_database(self):
        try:
            self.cursor.execute("select database()")
            dbname = self.cursor.fetchone()[0]

            while dbname is not None:
                dbname = self.cursor.fetchone()
                return dbname

        except mysqlc.Error as err:
            return err


class WritDB:

    def __init__(self):
        print("\nPreparing to write to database.")

        if CURSOR:
            self.cursor = CURSOR
            self._conn1 = CONN
        else:
            self._conn1 = ConnDB().dbconnect()
            self.cursor = self._conn1.cursor()

    def create_database(self, db_name):
        for dbname in db_name.values():
            print("Creating database: {}".format(dbname))
            try:
                self.cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(dbname))
                print("\nDatabase: {} created.".format(dbname), end='')
            except mysqlc.Error as err:
                print("Failed creating database: {}".format(err.msg))
            else:
                print("Done")

    def drop_database(self, db_name):
        for dbname in db_name.values():
            print("Dropping database :{}".format(dbname))
            try:
                ConnDB.database = dbname
                print("\nDeleting Database {}:... ".format(ConnDB.database), end='')
                self.cursor.execute("DROP DATABASE {}".format(ConnDB.database))
            except mysqlc.Error as err:
                print("Something went wrong! {}".format(err.msg))
            else:
                print("DONE")


class WritTabl:

    def __init__(self):
        print("Preparing to Modify Tables")
        if CURSOR:
            self.cursor = CURSOR
            self._conn1 = CONN
        else:
            self._conn1 = ConnDB().dbconnect()
            self.cursor = self._conn1.cursor()

    def modify_table(self, db_name, table):
        ConnDB.database = db_name
        res = isinstance(table, str)
        if res:
            try:
                print("\nModifying table {}:... ".format(table), end='')
                self.cursor.execute("USE {}".format(ConnDB.database))
                self.cursor.execute(table)
            except mysqlc.Error as err:
                print(err.msg)
            else:
                print("DONE")
        else:
            for name, ddl in table.items():
                try:
                    print("\nModifying table {}:... ".format(name), end='')
                    self.cursor.execute("USE {}".format(ConnDB.database))
                    self.cursor.execute(ddl)
                except mysqlc.Error as err:
                    print(err.msg)
                else:
                    print("DONE")

    def update_table(self, db_name, tb_name, set_fd, row_id, fd_name):
        ConnDB.database = db_name
        # prepare query and data
        query = """ UPDATE {}
                    SET {} = %s
                    WHERE id = %s """.format(tb_name, set_fd)
        data = (fd_name, row_id)
        try:
            print("\nMaking changes....")
            self.cursor.execute(query, data)
            # accept the changes
            self._conn1.commit()
            print("Data committed")
        except mysqlc.Error as err:
            print("{}".format(err.msg))

    def delete_row(self, db_name, tb_name, ro_id):
        ConnDB.database = db_name
        query = """ DELETE FROM {}
                    WHERE id = {} """.format(tb_name, ro_id)
        try:
            print("Locating row id {} within {},{}....".format(ro_id, db_name, tb_name))
            self.cursor.execute(query)
            # accept the change
            print("Delecting user with id....", ro_id)
            self._conn1.commit()
        except mysqlc.Error as err:
            print(err.msg)

    def drop_table(self, db_name, tb_name):
        print("Dropping table :{}".format(tb_name))
        try:
            ConnDB.database = db_name
            print("\nLocating table {}:... ".format(tb_name), end='')
            self.cursor.execute("DROP TABLE `{}`.`{}`".format(db_name, tb_name))
        except mysqlc.Error as err:
            print("Something went wrong! {}".format(err.msg))
        else:
            print("DONE")


class FetchDB:

    def __init__(self):
        print("Waking Fido for fetch....")
        if CURSOR:
            self.cursor = CURSOR
            self._conn1 = CONN
            print("Cursor located.")
        else:
            self._conn1 = ConnDB().dbconnect()
            self.cursor = self._conn1.cursor()
            print("Cursor created.")

    def query_with_fetchone(self, db_name, select):
        ConnDB.database = db_name
        print("Entering database {}".format(db_name))
        try:
            print("Searching database for {}".format(select))
            self.cursor.execute(select)
            print("Search complete")
            row = self.cursor.fetchone()
            print("Located....".format(row))
            return row
        except mysqlc.Error as err:
            print(err.msg)
            return err.msg

    def query_with_fetchall(self, db_name, select):
        ConnDB.database = db_name

        try:
            self.cursor.execute(select)
            rows = self.cursor.fetchall()

            print('Total Row(s):', self.cursor.rowcount)
            for row in rows:
                print(row)

        except mysqlc.Error as e:
            print(e)

    def iter_row(cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    def query_with_fetchmany(self, db_name, select):
        ConnDB.database = db_name
        _f = FetchDB
        try:
            self.cursor.execute(select)
            for row in _f.iter_row(self.cursor, 10):
                print(row)
        except mysqlc.Error as err:
            print(err.msg)


def exec_sql_script(scriptname):
    scriptfilename = scriptname
    if CURSOR:
        exec_cursor = CURSOR
        exec_conn1 = CONN
    else:
        exec_conn1 = ConnDB().dbconnect()
        exec_cursor = CURSOR

    try:
        print("Reading Script...")
        scriptFile = open(scriptfilename, 'r')
        script = scriptFile.read()
        scriptFile.close()

        print("Running Script...")
        exec_cursor.execute(script)

        exec_conn1.commit()
        print("Changes successfully committed\n")

    except mysqlc.Error as err:
        print("Something went wrong:" "\n{}".format(err.msg))


def living_in(the_database):
    # wow wow
    try:
        db = sqlite3.connect(the_database)
        db.execute("PRAGMA foreign_keys=ON")
    except sqlite3.OperationalError:
        error("Failed to open database, {}".format(the_database))
        return None
    return DatabaseDatabase(db)


# Database

def db_error(f):
    @wraps(f)
    def protected(*args, **kwargs):
        try:
            f(*args, **kwargs)
            return True
        except:
            exception("Database exception thrown")
            return False

    return protected


def db_error_default(default_value):
    value = default_value

    def decorate(f):
        @wraps(f)
        def protected(*args, **kwargs):
            nonlocal value
            try:
                return f(*args, **kwargs)
            except:
                exception("Database exception thrown")
                return value

        return protected

    return decorate


class DatabaseDatabase:
    def __init__(self, db):
        self._db = db
        self.q = db.cursor()

        # Set up collations
        self._db.create_collation("alphanum", _collate_alphanum)

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        return getattr(self._db, attr)

    def get_count(self):
        return self.q.fetchone()[0]

    def save(self):
        self.commit()

    # Setup

    def setup_tables(self):
        self.q.execute("""CREATE TABLE IF NOT EXISTS ShowTypes (
            id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            key     TEXT NOT NULL
        )""")
        self.q.executemany("INSERT OR IGNORE INTO ShowTypes (id, key) VALUES (?, ?)",
                           [(t.value, t.name.lower()) for t in ShowType])

        self.q.execute("""CREATE TABLE IF NOT EXISTS Shows (
            id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name        TEXT NOT NULL,
            length      INTEGER,
            type        INTEGER NOT NULL,
            has_source  INTEGER NOT NULL DEFAULT 0,
            enabled     INTEGER NOT NULL DEFAULT 1,
            delayed     INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY(type) REFERENCES ShowTypes(id)
        )""")

        self.q.execute("""CREATE TABLE IF NOT EXISTS ShowNames (
            show        INTEGER NOT NULL,
            name        TEXT NOT NULL
        )""")

        self.q.execute("""CREATE TABLE IF NOT EXISTS Services (
            id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            key         TEXT NOT NULL UNIQUE,
            name        TEXT NOT NULL,
            enabled     INTEGER NOT NULL DEFAULT 0,
            use_in_post INTEGER NOT NULL DEFAULT 1
        )""")

        self.q.execute("""CREATE TABLE IF NOT EXISTS Streams (
            id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            service     TEXT NOT NULL,
            show        INTEGER,
            show_id     TEXT,
            show_key    TEXT NOT NULL,
            name        TEXT,
            remote_offset   INTEGER NOT NULL DEFAULT 0,
            display_offset  INTEGER NOT NULL DEFAULT 0,
            active      INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY(service) REFERENCES Services(id),
            FOREIGN KEY(show) REFERENCES Shows(id)
        )""")

        self.q.execute("""CREATE TABLE IF NOT EXISTS Episodes (
            show        INTEGER NOT NULL,
            episode     INTEGER NOT NULL,
            post_url    TEXT,
            FOREIGN KEY(show) REFERENCES Shows(id)
        )""")

        self.q.execute("""CREATE TABLE IF NOT EXISTS LinkSites (
            id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            key         TEXT NOT NULL UNIQUE,
            name        TEXT NOT NULL,
            enabled     INTEGER NOT NULL DEFAULT 1
        )""")

        self.q.execute("""CREATE TABLE IF NOT EXISTS Links (
            show        INTEGER NOT NULL,
            site        INTEGER NOT NULL,
            site_key    TEXT NOT NULL,
            FOREIGN KEY(site) REFERENCES LinkSites(id)
            FOREIGN KEY(show) REFERENCES Shows(id)
        )""")

        self.q.execute("""CREATE TABLE IF NOT EXISTS Scores (
            show        INTEGER NOT NULL,
            episode     INTEGER NOT NULL,
            site        INTEGER NOT NULL,
            score       REAL NOT NULL,
            FOREIGN KEY(show) REFERENCES Shows(id),
            FOREIGN KEY(site) REFERENCES LinkSites(id)
        )""")

        self.commit()

    def register_services(self, services):
        self.q.execute("UPDATE Services SET enabled = 0")
        for service_key in services:
            service = services[service_key]
            self.q.execute("INSERT OR IGNORE INTO Services (key, name) VALUES (?, '')", (service.key,))
            self.q.execute("UPDATE Services SET name = ?, enabled = 1 WHERE key = ?", (service.name, service.key))
        self.commit()

    def register_link_sites(self, sites):
        self.q.execute("UPDATE LinkSites SET enabled = 0")
        for site_key in sites:
            site = sites[site_key]
            self.q.execute("INSERT OR IGNORE INTO LinkSites (key, name) VALUES (?, '')", (site.key,))
            self.q.execute("UPDATE LinkSites SET name = ?, enabled = 1 WHERE key = ?", (site.name, site.key))
        self.commit()

    # Services

    @db_error_default(None)
    @lru_cache(10)
    def get_service(self, id=None, key=None) -> Service:
        if id is not None:
            self.q.execute("SELECT id, key, name, enabled, use_in_post FROM Services WHERE id = ?", (id,))
        elif key is not None:
            self.q.execute("SELECT id, key, name, enabled, use_in_post FROM Services WHERE key = ?", (key,))
        else:
            error("ID or key required to get service")
            return None
        service = self.q.fetchone()
        return Service(*service)

    @db_error_default(list())
    def get_services(self, enabled=True, disabled=False) -> [Service]:
        services = list()
        if enabled:
            self.q.execute("SELECT id, key, name, enabled, use_in_post FROM Services WHERE enabled = 1")
            for service in self.q.fetchall():
                services.append(Service(*service))
        if disabled:
            self.q.execute("SELECT id, key, name, enabled, use_in_post FROM Services WHERE enabled = 0")
            for service in self.q.fetchall():
                services.append(Service(*service))
        return services

    @db_error_default(None)
    def get_stream(self, id=None, service_tuple=None) -> Stream:
        if id is not None:
            debug("Getting stream for id {}".format(id))

            self.q.execute(
                "SELECT id, service, show, show_id, show_key, name, remote_offset, display_offset, active FROM Streams WHERE id = ?",
                (id,))
            stream = self.q.fetchone()
            if stream is None:
                error("Stream {} not found".format(id))
                return None
            stream = Stream(*stream)
            return stream
        elif service_tuple is not None:
            service, show_key = service_tuple
            debug("Getting stream for {}/{}".format(service, show_key))
            self.q.execute(
                "SELECT id, service, show, show_id, show_key, name, remote_offset, display_offset, active FROM Streams WHERE service = ? AND show_key = ?",
                (service.id, show_key))
            stream = self.q.fetchone()
            if stream is None:
                error("Stream {} not found".format(id))
                return None
            stream = Stream(*stream)
            return stream
        else:
            error("Nothing provided to get stream")
            return None

    @db_error_default(list())
    def get_streams(self, service=None, show=None, active=True, unmatched=False, missing_name=False) -> [Stream]:
        # Not the best combination of options, but it's only the usage needed
        if service is not None:
            debug("Getting all streams for service {}".format(service.key))
            service = self.get_service(key=service.key)
            self.q.execute("SELECT id, service, show, show_id, show_key, name, remote_offset, display_offset, active FROM Streams \
                            WHERE service = ? AND active = ?", (service.id, 1 if active else 0))
        elif show is not None:
            debug("Getting all streams for show {}".format(show.id))
            self.q.execute("SELECT id, service, show, show_id, show_key, name, remote_offset, display_offset, active FROM Streams \
                            WHERE show = ? AND active = ?", (show.id, active))
        elif unmatched:
            debug("Getting unmatched streams")
            self.q.execute("SELECT id, service, show, show_id, show_key, name, remote_offset, display_offset, active FROM Streams \
                            WHERE show IS NULL")
        elif missing_name:
            self.q.execute("SELECT id, service, show, show_id, show_key, name, remote_offset, display_offset, active FROM Streams \
                            WHERE (name IS NULL OR name = '') AND active = ?", (active,))
        else:
            error("A service or show must be provided to get streams")
            return list()

        streams = self.q.fetchall()
        streams = [Stream(*stream) for stream in streams]
        return streams

    @db_error_default(False)
    def has_stream(self, service_key, key) -> bool:
        service = self.get_service(key=service_key)
        self.q.execute("SELECT count(*) FROM Streams WHERE service = ? AND show_key = ?", (service.id, key))
        return self.get_count() > 0

    @db_error
    def add_stream(self, raw_stream: UnprocessedStream, show_id, commit=True):
        debug("Inserting stream: {}".format(raw_stream))

        service = self.get_service(key=raw_stream.service_key)
        self.q.execute(
            "INSERT INTO Streams (service, show, show_id, show_key, name, remote_offset, display_offset, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (service.id, show_id, raw_stream.show_id, raw_stream.show_key, raw_stream.name, raw_stream.remote_offset,
             raw_stream.display_offset, show_id is not None))
        if commit:
            self.commit()

    @db_error
    def update_stream(self, stream: Stream, show=None, active=None, name=None, show_id=None, show_key=None,
                      remote_offset=None, commit=True):
        debug("Updating stream: id={}".format(stream.id))
        if show is not None:
            self.q.execute("UPDATE Streams SET show = ? WHERE id = ?", (show, stream.id))
        if active is not None:
            self.q.execute("UPDATE Streams SET active = ? WHERE id = ?", (active, stream.id))
        if name is not None:
            self.q.execute("UPDATE Streams SET name = ? WHERE id = ?", (name, stream.id))
        if show_id is not None:
            self.q.execute("UPDATE Streams SET show_id = ? WHERE id = ?", (show_id, stream.id))
        if show_key is not None:
            self.q.execute("UPDATE Streams SET show_key = ? WHERE id = ?", (show_key, stream.id))
        if remote_offset is not None:
            self.q.execute("UPDATE Streams SET remote_offset = ? WHERE id = ?", (remote_offset, stream.id))

        if commit:
            self.commit()

    # Links

    @db_error_default(None)
    def get_link_site(self, id=None, key=None) -> LinkSite:
        if id is not None:
            self.q.execute("SELECT id, key, name, enabled FROM LinkSites WHERE id = ?", (id,))
        elif key is not None:
            self.q.execute("SELECT id, key, name, enabled FROM LinkSites WHERE key = ?", (key,))
        else:
            error("ID or key required to get link site")
            return None
        site = self.q.fetchone()
        if site is None:
            return None
        return LinkSite(*site)

    @db_error_default(list())
    def get_link_sites(self, enabled=True, disabled=False) -> [LinkSite]:
        sites = list()
        if enabled:
            self.q.execute("SELECT id, key, name, enabled FROM LinkSites WHERE enabled = 1")
            for link in self.q.fetchall():
                sites.append(LinkSite(*link))
        if disabled:
            self.q.execute("SELECT id, key, name, enabled FROM LinkSites WHERE enabled = 0")
            for link in self.q.fetchall():
                sites.append(LinkSite(*link))
        return sites

    @db_error_default(list())
    def get_links(self, show=None) -> [Link]:
        if show is not None:
            debug("Getting all links for show {}".format(show.id))

            # Get all streams with show ID
            self.q.execute("SELECT site, show, site_key FROM Links WHERE show = ?", (show.id,))
            links = self.q.fetchall()
            links = [Link(*link) for link in links]
            return links
        else:
            error("A show must be provided to get links")
            return list()

    @db_error_default(None)
    def get_link(self, show, link_site) -> Link:
        debug("Getting link for show {} and site {}".format(show.id, link_site.key))

        self.q.execute("SELECT site, show, site_key FROM Links WHERE show = ? AND site = ?", (show.id, link_site.id))
        link = self.q.fetchone()
        if link is None:
            return None
        link = Link(*link)
        return link

    @db_error_default(False)
    def has_link(self, site_key, key) -> bool:
        site = self.get_link_site(key=site_key)
        self.q.execute("SELECT count(*) FROM Links WHERE site = ? AND site_key = ?",
                       (site.id, key))
        return self.get_count() > 0

    @db_error
    def add_link(self, raw_show: UnprocessedShow, show_id, commit=True):
        debug("Inserting link: {}/{}".format(show_id, raw_show))

        site = self.get_link_site(key=raw_show.site_key)
        if site is None:
            error("  Invalid site \"{}\"".format(raw_show.site_key))
            return
        site_key = raw_show.show_key

        self.q.execute("INSERT INTO Links (show, site, site_key) VALUES (?, ?, ?)",
                       (show_id, site.id, site_key))
        if commit:
            self.commit()

    # Shows

    @db_error_default(list())
    def get_shows(self, missing_length=False, missing_stream=False, enabled=True, delayed=False) -> [Show]:
        shows = list()
        if missing_length:
            self.q.execute(
                "SELECT id, name, length, type, has_source, enabled, delayed FROM Shows WHERE (length IS NULL OR length = '' OR length = 0) AND enabled = ?",
                (enabled,))
        elif missing_stream:
            self.q.execute(
                "SELECT id, name, length, type, has_source, enabled, delayed FROM Shows show \
                WHERE (SELECT count(*) FROM Streams stream WHERE stream.show = show.id AND stream.active = 1) = 0 AND enabled = ?",
                (enabled,))
        elif delayed:
            self.q.execute(
                "SELECT id, name, length, type, has_source, enabled, delayed FROM Shows WHERE delayed = 1 AND enabled = ?",
                (enabled,))
        else:
            self.q.execute("SELECT id, name, length, type, has_source, enabled, delayed FROM Shows WHERE enabled = ?",
                           (enabled,))
        for show in self.q.fetchall():
            shows.append(Show(*show))
        return shows

    @db_error_default(None)
    def get_show(self, id=None, stream=None) -> Show:
        # debug("Getting show from database")

        # Get show ID
        if stream and not id:
            id = stream.show

        # Get show
        if id is None:
            error("Show ID not provided to get_show")
            return None
        self.q.execute("SELECT id, name, length, type, has_source, enabled, delayed FROM Shows WHERE id = ?", (id,))
        show = self.q.fetchone()
        if show is None:
            return None
        show_type = to_show_type(show[4])
        show = Show(*show[:4], show_type, *show[5:])
        return show

    @db_error_default(None)
    def add_show(self, raw_show: UnprocessedShow, commit=True) -> int:
        debug("Inserting show: {}".format(raw_show))

        name = raw_show.name
        length = raw_show.episode_count
        show_type = from_show_type(raw_show.show_type)
        has_source = raw_show.has_source
        self.q.execute("INSERT INTO Shows (name, length, type, has_source) VALUES (?, ?, ?, ?)",
                       (name, length, show_type, has_source))
        show_id = self.q.lastrowid
        self.add_show_names(raw_show.name, *raw_show.more_names, id=show_id, commit=commit)

        if commit:
            self.commit()
        return show_id

    @db_error_default(None)
    def update_show(self, show_id, raw_show, commit=True):
        debug("Updating show: {}".format(raw_show))

        # name = raw_show.name
        length = raw_show.episode_count
        show_type = from_show_type(raw_show.show_type)
        has_source = raw_show.has_source

        self.q.execute("UPDATE Shows SET length = ?, type = ?, has_source = ? WHERE id = ?",
                       (length, show_type, has_source, show_id))

        if commit:
            self.commit()

    @db_error
    def add_show_names(self, *names, id=None, commit=True):
        self.q.executemany("INSERT INTO ShowNames (show, name) VALUES (?, ?)", [(id, name) for name in names])
        if commit:
            self.commit()

    @db_error
    def set_show_episode_count(self, show, length):
        debug("Updating show episode count in database: {}, {}".format(show.name, length))
        self.q.execute("UPDATE Shows SET length = ? WHERE id = ?", (length, show.id))
        self.commit()

    @db_error
    def set_show_delayed(self, show: Show, delayed=True):
        debug("Marking show {} as delayed: {}".format(show.name, delayed))
        self.q.execute("UPDATE Shows SET delayed = ? WHERE id = ?", (delayed, show.id))
        self.commit()

    @db_error
    def set_show_enabled(self, show: Show, enabled=True, commit=True):
        debug("Marking show {} as {}".format(show.name, "enabled" if enabled else "disabled"))
        self.q.execute("UPDATE Shows SET enabled = ? WHERE id = ?", (enabled, show.id))
        if commit:
            self.commit()

    # Episodes

    @db_error_default(True)
    def stream_has_episode(self, stream: Stream, episode_num) -> bool:
        self.q.execute("SELECT count(*) FROM Episodes WHERE show = ? AND episode = ?", (stream.show, episode_num))
        num_found = self.get_count()
        debug("Found {} entries matching show {}, episode {}".format(num_found, stream.show, episode_num))
        return num_found > 0

    @db_error_default(None)
    def get_latest_episode(self, show: Show) -> Episode:
        self.q.execute("SELECT episode, post_url FROM Episodes WHERE show = ? ORDER BY episode DESC LIMIT 1",
                       (show.id,))
        data = self.q.fetchone()
        if data is not None:
            return Episode(data[0], None, data[1], None)
        return None

    @db_error
    def add_episode(self, show_id, episode_num, post_url):
        debug("Inserting episode {} for show {} ({})".format(episode_num, show_id, post_url))
        self.q.execute("INSERT INTO Episodes (show, episode, post_url) VALUES (?, ?, ?)",
                       (show_id, episode_num, post_url))
        self.commit()

    @db_error_default(list())
    def get_episodes(self, show, ensure_sorted=True) -> [Episode]:
        episodes = list()
        self.q.execute("SELECT episode, post_url FROM Episodes WHERE show = ?", (show.id,))
        for data in self.q.fetchall():
            episodes.append(Episode(data[0], None, data[1], None))

        if ensure_sorted:
            episodes = sorted(episodes, key=lambda e: e.number)
        return episodes

    # Scores

    @db_error_default(list())
    def get_show_scores(self, show: Show) -> [EpisodeScore]:
        self.q.execute("SELECT episode, site, score FROM Scores WHERE show=?", (show.id,))
        return [EpisodeScore(show.id, *s) for s in self.q.fetchall()]

    @db_error_default(list())
    def get_episode_scores(self, show: Show, episode: Episode) -> [EpisodeScore]:
        self.q.execute("SELECT site, score FROM Scores WHERE show=? AND episode=?", (show.id, episode.number))
        return [EpisodeScore(show.id, episode.number, *s) for s in self.q.fetchall()]

    @db_error_default(None)
    def get_episode_score_avg(self, show: Show, episode: Episode) -> EpisodeScore:
        debug("Calculating avg score for {} ({})".format(show.name, show.id))
        self.q.execute("SELECT score FROM Scores WHERE show=? AND episode=?", (show.id, episode.number))
        scores = [s[0] for s in self.q.fetchall()]
        if len(scores) > 0:
            score = sum(scores) / len(scores)
            debug("  Score: {} (from {} scores)".format(score, len(scores)))
            return score
        return None

    @db_error
    def add_episode_score(self, show: Show, episode: Episode, site: LinkSite, score: float, commit=True):
        self.q.execute("INSERT INTO Scores (show, episode, site, score) VALUES (?, ?, ?, ?)",
                       (show.id, episode.number, site.id, score))
        if commit:
            self.commit()

    # Searching

    @db_error_default(set())
    def search_show_ids_by_names(self, *names, exact=False) -> Set[Show]:
        shows = set()
        for name in names:
            debug("Searching shows by name: {}".format(name))
            if exact:
                self.q.execute("SELECT show, name FROM ShowNames WHERE name = ?", (name,))
            else:
                self.q.execute("SELECT show, name FROM ShowNames WHERE name = ? COLLATE alphanum", (name,))
            matched = self.q.fetchall()
            for match in matched:
                debug("  Found match: {} | {}".format(match[0], match[1]))
                shows.add(match[0])
        return shows


# Helper methods

## Conversions

def to_show_type(db_val: str) -> ShowType:
    for st in ShowType:
        if st.value == db_val:
            return st
    return ShowType.UNKNOWN


def from_show_type(st: ShowType) -> str:
    if st is None:
        return None
    return st.value


## Collations

def _collate_alphanum(str1, str2):
    str1 = _alphanum_convert(str1)
    str2 = _alphanum_convert(str2)

    if str1 == str2:
        return 0
    elif str1 < str2:
        return -1
    else:
        return 1


_alphanum_regex = re.compile("[^a-zA-Z0-9]+")
_romanization_o = re.compile("\bwo\b")


def _alphanum_convert(s):
    # TODO: punctuation is important for some shows to distinguish between seasons (ex. K-On! and K-On!!)
    # 6/28/16: The purpose of this function is weak collation; use of punctuation to distinguish between seasons can be done later when handling multiple found shows.

    # Characters to words
    s = s.replace("&", "and")
    # Japanese romanization differences
    s = _romanization_o.sub("o", s)
    s = s.replace("uu", "u")
    s = s.replace("wo", "o")

    s = _alphanum_regex.sub("", s)
    s = s.lower()
    return unidecode(s)

if __name__ == '__main__':
    CONN = ""
    CURSOR = ""

    class TestCMS:

        def __init__(self):
            print("Testing")
            self.db_name = "test"
            self._dbconfig = read_config
            self._f = 'config.ini'
            self._config = self._dbconfig(self._f, 'mysqldb')
            print("Configuration loaded")

        def testConnDB(self):
            c = ConnDB()
            c.dbconnect()
            c.dbclose()

        def testCheckDB(self):
            CheckDB().check_database(self.db_name)

        def testWritDB(self):
            wrdb = WritDB()
            print("Clearing database....")
            wrdb.drop_database(self._config)
            print("Creating database")
            wrdb.create_database(self._config)
            print("Clearing database....")
            wrdb.drop_database(self._config)

        def testWritTabla(self):
            wrtl = WritTabl()
            wrdb = WritDB()
            _config = {"database": "milo_defaults"}
            print("Clearing {}...".format(_config), end='')
            wrdb.drop_database(_config)
            print("Done")
            print("Creaating {}....".format(_config), end='')
            wrdb.create_database(_config)
            print("Done")
            print("Modifying tables{}".format("...."), end='')
            wrtl.modify_table("milo_defaults", t.TABLES)
            wrtl.modify_table("milo_defaults", t.ALTERS)
            wrtl.modify_table("milo_defaults", t.INSERTS)
            print("Done")

        def testWritTablb(self):
            wrtl = WritTabl()
            wrdb = WritDB()
            _config = {"database": "milo_defaults"}
            print("Updating tables{}".format('....'), end='')
            wrtl.update_table('milo_defaults', 'users', 'username', 1, 'milotester')
            print('Done')
            print("Deleting rows{}".format('....'), end='')
            wrtl.delete_row('milo_defaults', 'users', 1)
            print('Done')
            print("Dropping tables".format('....'), end='')
            wrtl.drop_table('milo_defaults', 'api-information')
            print('Done')
            print("Clearing {}...".format(_config), end='')
            wrdb.drop_database(_config)
            print("Done")
            ConnDB().dbclose()

        def testFetchDB(self):
            print("Creating Test database{}".format("...."), end="\n")
            TestCMS().testWritTabla()
            print("Done")
            f = FetchDB()
            f.query_with_fetchone("milo_defaults", "SELECT * FROM milo_statement_strings")
            f.query_with_fetchall("milo_defaults", "SELECT * FROM users")
            f.query_with_fetchmany("milo_defaults", "SELECT * FROM milo_statement_strings")
            TestCMS().testWritTablb()

        def testWRTL(self):
            db = ConnDB().dbconnect()
            wrtl = WritTabl()
            data = t.INSERTS['users']
            INSERTS = {}
            data2 = INSERTS['users'] = (
                "INSERT INTO `milo_defaults`.`users`"
                "   (`id`, `username`, `email`, `password`)"
                "   VALUES"
                "   ('2', 'mycstro', 'mycstro@vspace.com', 'myc2367');")
            wrtl.modify_table("milo_defaults", data2)

