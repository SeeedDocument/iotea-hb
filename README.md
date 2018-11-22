We deployed the website on CentOS7. Following steps will show you how to deploy.

**Step 1.** Install Python3

	sudo yum -y install epel-release
	sudo yum -y install python36

**Step 2.** Install Python pip and virtual enviroment

	wget https://bootstrap.pypa.io/get-pip.py
	sudo python36 get-pip.py
	sudo pip install virtualenv

**Setp 3.** Clone our website from GitHub

	sudo yum -y install git
	git clone https://github.com/SeeedDocument/iotea-hb.git

**Step 4.** Create and activate virtual enviroment

	virtualenv -p python36 iotea-hb
	cd iotea-hb
	source bin/activate

**Step 5.** Install dependent libraries

	pip install pymysql
	pip install dbutils
	pip install flask
	pip install websocket-client
	pip install cofigparser

**Step 6.** Create database

	sudo yum -y install mariadb mariabd-server
	sudo systemctl enable mariadb
	sudo systemctl start mariadb
	mysql -uroot -p

and then use iotea_hb.sql to create a table.

**Step 7.** Create db.ini, and write these codes to it

    [db]
    db_port = 3306
    db_user = root
    db_host = localhost
    db_pass = 
    db_name = iotea

change db.ini's path in db.py

	# in db.py
	#cf.read("/data/www/python3_iotea_hb/iotea/conf/db.ini")
	cf.read("/home/<your_username>/iotea-hb/db.ini")

**Step 8.** Change port in app.py and start the website: 

	# in app.py
	#app.run(debug=True, port=6000)
	app.run(debug=True, port=8080)

	# in terminal
	pip install gunicorn
	gunicorn -w 5 -b 0.0.0.0:8080 app:app

now visit [127.0.0.1:8080](127.0.0.1:8080) in your web browser, you can see the website, but real-time data is not displayed.

**Step 9.** Get loriot data

Open another terminal, reenter virtual enviroment and start loriot app: 

	cd iotea-hb
	source bin/activate
	gunicorn loriot:app 

Wait for a while, you will see data displayed in website, or you can change wss in loriot.py:

	# in loriot.py
	#ws = create_connection("wss://cn1.loriot.io/app?token=vnwEuwAAAA1jbjEubG9yaW90LmlvRpscoh9Uq1L7K1zbrcBz6w==")
	ws = create_connection(<your_wss>)
