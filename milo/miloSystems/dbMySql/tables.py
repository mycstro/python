TABLES = {}
ALTERS = {}
INSERTS = {}

TABLES['current_addresses'] = (
    "CREATE TABLE `current_addresses` ("
    "   `id` int NOT NULL AUTO_INCREMENT,"
    "   `street_address` varchar(255) NOT NULL,"
    "   `city` varchar(40) NOT NULL,"
    "   `state` varchar(40) NOT NULL,"
    "   PRIMARY KEY (`id`), UNIQUE KEY `id` (`id`)"
    ")  ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1")

TABLES['birth_locations'] = (
    "CREATE TABLE `birth_locations` ("
    "   `id` int NOT NULL AUTO_INCREMENT,"
    "   `birth_city` varchar(40) NOT NULL,"
    "   `birth_state` varchar(40) NOT NULL,"
    "   PRIMARY KEY (`id`), UNIQUE KEY `id` (`id`)"
    ")  ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1")

TABLES['users'] = (
    "CREATE TABLE `users` ("
    "  `id` int NOT NULL AUTO_INCREMENT,"
    "  `username` varchar(16) NOT NULL,"
    "  `email` varchar(50) DEFAULT NULL,"
    "  `password` varchar(16) NOT NULL,"
    "  `usercreation` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`id`, `username`),"
    "  UNIQUE KEY `id` (`id`)"
    ") ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;")

INSERTS['users'] = (
    "INSERT INTO `milo_defaults`.`users`"
    "   (`id`, `username`, `email`, `password`)"
    "   VALUES"
    "   ('1', 'milo', 'milo@vspace.com', 'itsmemilo');")

TABLES['profiles'] = (
    "CREATE TABLE `profiles` ("
    "   `id` int NOT NULL AUTO_INCREMENT,"
    "   `first_name` varchar(20) NOT NULL,"
    "   `middle_name` varchar(20) NOT NULL,"
    "   `last_name` varchar(20) NOT NULL,"
    "   `age` int(5) NOT NULL,"
    "   `birthdate` varchar(10) NOT NULL,"
    "   `weight` int(5) NOT NULL,"
    "   `height` int(5) NOT NULL,"
    "   `gender` varchar(20) NOT NULL,"
    "   `phone_number` int(10) NOT NULL,"
    "   `current_address_id` INT NOT NULL,"
    "   `birth_address_id` INT NOT NULL,"
    "   PRIMARY KEY (`id`, `current_address_id`, `birth_address_id`), UNIQUE KEY `id` (`id`)"
    ")  ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;")

ALTERS['profiles'] = (
    "ALTER TABLE `profiles`"   
    "   ADD INDEX `fk_current_add_id_idx` (`current_address_id` ASC),"
    "   ADD INDEX `fk_birt_add_id_idx` (`birth_address_id` ASC),"
    "   ADD CONSTRAINT `fk_current_add_id` FOREIGN KEY (`current_address_id`) REFERENCES `current_addresses` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,"
    "   ADD CONSTRAINT `fk_birt_add_id` FOREIGN KEY (`birth_address_id`) REFERENCES `birth_locations` (`id`) ON UPDATE CASCADE ON DELETE CASCADE;")

TABLES['users_profiles'] = (
    "CREATE TABLE `users_profiles` ("
    "   `id` int NOT NULL AUTO_INCREMENT,"
    "   `profile_id` INT NOT NULL,"
    "   `user_id` INT NOT NULL,"
    "   PRIMARY KEY (`id`, `profile_id`, `user_id`)"
    ")  ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;")

ALTERS['users_profiles'] = (
    "ALTER TABLE `users_profiles`"
    "   ADD INDEX `fk_profile_id_idx` (`profile_id` ASC),"
    "   ADD INDEX `fk_user_id_idx` (`user_id` ASC),"
    "   ADD CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,"
    "   ADD CONSTRAINT `fk_profile_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`) ON UPDATE CASCADE ON DELETE CASCADE;")

# /* Table structure for table `python_internet_modules` */
TABLES['python_internet_modules'] = (
    "CREATE TABLE `python_internet_modules` ("
	"   `id` int NOT NULL AUTO_INCREMENT,"
    "   `protocol` varchar(20) NOT NULL,"
    "   `common_function` varchar(60) NOT NULL,"
    "   `port_no` int(11) NOT NULL,"
    "   `python_modules` varchar(200) NOT NULL,"
    "PRIMARY KEY (`id`),"
    "UNIQUE KEY `id` (`id`)"
")	ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;")

# /*Data for the table `python_internet_modules` */
INSERTS['python_internet_modules'] = (
    "INSERT INTO `milo_defaults`.`python_internet_modules`"
    "   (`id`, `protocol`, `common_function`, `port_no`, `python_modules`)"
    "   VALUES"
    "   (1, 'HTTP', 'Web pages', 80, 'httplib, urllib, xmlrpclib'),"
    "   (2, 'NNTP', 'Usenet news', 119, 'nntplib'),"
    "   (3, 'FTP', 'File transfers', 20, 'ftplib, urllib'),"
    "   (4, 'SMTP', 'Sending email', 25, 'smtplib'),"
    "   (5, 'POP3', 'Fetching email', 110, 'poplib'),"
    "   (6, 'IMAP4', 'Fetching email', 143, 'imaplib'),"
    "   (7, 'Telnet', 'Command lines', 23, 'telnetlib'),"
    "   (8, 'Gopher', 'Document transfers', 70, 'gopherlib, urllib'),"
    "   (9, 'SSH', 'Secure command lines', 22, 'paramiko, jumpssh');")

TABLES['milo_statement_strings'] = (
    "CREATE TABLE `milo_statement_strings` ("
    "   `id` int(11) NOT NULL AUTO_INCREMENT,"
    "   `listener` varchar(20) NOT NULL,"
    "   `common_string` varchar(200) NOT NULL,"
    "   `port_no` int(11) NOT NULL,"
    "   `common_function` varchar(200) NOT NULL,"
    "   PRIMARY KEY (`id`, `port_no`),"
    "   UNIQUE KEY `id` (`id`)"
    ") ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;")

INSERTS['milo_statement_strings'] = (
    "INSERT INTO `milo_defaults`.`milo_statement_strings`"
    "   (`id`, `listener`, `common_string`, `port_no`, `common_function`)"
    "   VALUES"
    "   (1, 'greeting1', 'Welcome to VSpace', 1, 'First Greeting'),"
    "   (2, 'greeting2', 'Welcome to the backend of VSpace', 2, 'Second Greeting'),"
    "   (3, 'returngreeting1', 'Welcome back', 3, 'Returning Greeting'),"
    "   (4, 'subgreeting1', 'I will be your host for your stay', 4, 'Sub Greeting'),"
    "   (5, 'subgreeting2', 'Allow me to check you into the ledger', 5, 'Sub Greeting');")

TABLES['api-information'] = (
    "CREATE TABLE `api-information` ("
    "   `id` int(11) NOT NULL AUTO_INCREMENT,"
    "   `api_name` varchar(50) NOT NULL,"
    "   `api_link` varchar(255) NOT NULL,"
    "   `api_description` varchar(255) NOT NULL,"
    "   `api_key` varchar(255) NOT NULL,"
    "   `api_secret` varchar(255) NOT NULL,"
    "   PRIMARY KEY (`id`),"
    "   UNIQUE KEY `id` (`id`)"
    ")  ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;")

INSERTS['api-information'] = (
    "INSERT INTO `milo_defaults`.`api-information`"
    "   (`id`, `api_name`, `api_link`, `api_description`, `api_key`, `api_secret`)"
    "   VALUES"
    "   (1, 'test', 'test.com', 'test', 't3st!k3y', 't3sts!3cr3t');")