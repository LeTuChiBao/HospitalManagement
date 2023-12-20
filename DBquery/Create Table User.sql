CREATE TABLE users (
    username VARCHAR(255) PRIMARY KEY,
    userpassword  VARCHAR(255) NOT NULL,
    fullname VARCHAR(255) NOT NULL,
    adress VARCHAR(255),
    birth DATE,
    phone VARCHAR(20),
    userrole VARCHAR(10) NOT NULL CHECK (userrole IN ('Super', 'Admin', 'Agent'))
);

INSERT INTO users (username, userpassword, fullname, adress, birth, phone ,userrole)
VALUES ('bao.le' , '1234' , 'Le Tu Chi Bao','Dien Ban, Quang Nam','1997-06-11','0966299999','Super')

INSERT INTO users (username, userpassword, fullname, adress, birth, phone ,userrole)
VALUES ('user1' , '1234' , 'Le Tu Chi Bao','Dien Ban, Quang Nam','1997-06-11','0966299999','Agent')

select * from users 

CREATE TABLE medicines (
    medicineno NVARCHAR(255) PRIMARY KEY,
    typeofmedicine  NVARCHAR(255) NOT NULL CHECK (typeofmedicine IN ('tablet', 'injection') ),
    medicinename NVARCHAR(255) NOT NULL CHECK (medicinename IN ('Vitamin A', 'VitaMmin B','VitaMmin D','Acetsminophen','DM','Panadol','Cipla','Novel','Absorica') ),
    lotno NVARCHAR(255),
    issuedate DATE,
	expdate DATE,
	side NVARCHAR(255)
);

DROP TABLE medicines;

ALTER TABLE medicines
DROP COLUMN phone;

INSERT INTO medicines (medicineno, typeofmedicine, medicinename, lotno, issuedate, expdate ,side)
VALUES ('M01' , 'tablet' , 'Vitamin A','L001','2023-06-11','2024-06-11','dizziness,fatigue')

select * from presciptions

CREATE TABLE presciptions (
    presciptionno NVARCHAR(255) PRIMARY KEY,
	medicineno NVARCHAR(255),
	username VARCHAR(255),
    furtherinfo VARCHAR(255),
	bloodpressure VARCHAR(255),
	storageadvice VARCHAR(255),
	dose VARCHAR(255),
	daillydose VARCHAR(255),
	FOREIGN KEY (medicineno) REFERENCES medicines(medicineno),
	FOREIGN KEY (username) REFERENCES users(username),
);

INSERT INTO presciptions (presciptionno, medicineno, username, furtherinfo, bloodpressure, storageadvice ,dose, daillydose )
VALUES ('P02' , 'M01' , 'bao.le','further info','blood pressure','storage advice','dose','dailly dose')

select presciptions.medicineno, * from presciptions
inner join medicines ON presciptions.medicineno = medicines.medicineno