
CREATE TABLE sdptest(id INT NOT NULL AUTO_INCREMENT primary key, name VARCHAR(20));

SELECT * FROM sdptest;

INSERT INTO sdptest (name) VALUES ("paul");

--Convert ui to py : pyuic5 -x input_form.ui -o user_input.py