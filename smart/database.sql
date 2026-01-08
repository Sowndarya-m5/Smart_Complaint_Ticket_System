CREATE DATABASE complaint_db;
USE complaint_db;

CREATE TABLE complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100),
    employee_email VARCHAR(100),
    department VARCHAR(50),
    problem TEXT,
    ticket_id VARCHAR(20),
    status VARCHAR(20),
    complaint_date DATE,
    resolve_date DATE,
    complete_date DATE,
    sla_days INT
);




CREATE TABLE manager (
    manager_name VARCHAR(50),
    password VARCHAR(255)
);


INSERT INTO manager (manager_name, password)
VALUES (
    'admin',
    'scrypt:32768:8:1$JYUCAggermZcyOgH$5211b6d4bcbe148c24c6cec69b3db0288b5971e80e82c29dffd92c193fcac6351c24aa3901e697188de618faa89a4ccb997523e83cba1097586e44121efe4464'
);

select * from manager;

'''
manager
user name = admin
password = admin123
'''

drop table admin;

CREATE TABLE admin (
    admin_name VARCHAR(50),
    password VARCHAR(255)
);

insert into admin (admin_name, password)
values(
	'support',
    'scrypt:32768:8:1$e0D2cCznIVqDrnZq$ffd6b766a14ee9fe5d82d9c2b31c0bad90aed0b61516ae24982c94e1a90bb23afd55162f7715b8e166393e216ae48b95caccb69890fb52ff03a4d42673b572ee'
);

select * from admin;


'''
admin 
user name = support
password = abc123
'''