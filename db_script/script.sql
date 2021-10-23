
CREATE TABLE `admin`(
username VARCHAR(20) NOT NULL,
password VARCHAR(100) NOT NULL,
PRIMARY KEY(username)
);

CREATE TABLE `course`(
code VARCHAR(10) NOT NULL,
name VARCHAR(50) NOT NULL,
PRIMARY KEY(code)
);
CREATE TABLE `college`(
code VARCHAR(10) NOT NULL,
name VARCHAR(50) NOT NULL,
PRIMARY KEY(code)
);

CREATE TABLE `students`(
id VARCHAR(9) NOT NULL,
firstname VARCHAR(50) NOT NULL,
middlename VARCHAR(20) NOT NULL,
lastname VARCHAR(20) NOT NULL,
year INT(1) NOT NULL,
gender VARCHAR(10) NOT NULL,
coursecode VARCHAR(10) NOT NULL,
collegecode VARCHAR(10),
PRIMARY KEY(id),
FOREIGN KEY(coursecode) REFERENCES course(code),
FOREIGN KEY(collegecode) REFERENCES college(code)
);

