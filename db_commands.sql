
--Log into mysql : /usr/bin/mysql -u root -p
 USE test;
 SHOW tables;
 SELECT * FROM sdptest;

CREATE TABLE sdptest(id INT NOT NULL AUTO_INCREMENT primary key, fname VARCHAR(20), sname VARCHAR(20), dob DATE, dept VARCHAR(20), access SMALLINT(3));

SELECT * FROM sdptest;

INSERT INTO sdptest (fname, sname, dob, dept, access) VALUES ("paul", "Fetherston", '1985-04-14', "sales", 3);

DELETE FROM sdptest WHERE id = 3;

--Convert ui to py : pyuic5 -x input_form.ui -o user_input.py