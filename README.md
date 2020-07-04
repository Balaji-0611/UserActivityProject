# UserActivityProject

This project is created for demonstrate Users and their activities as a json format using Django.

Required python packages:
	1. Django
	2. json


Custom Management API Commands:
	adduser,
	modifyuser,
	deleteuser,
	addactivity,
	modifyactivity, 
	deleteactivity
	
Examples for custom management API's:

	python manage.py update_db --action adduser --id u4 --real_name User4 --tz tz4
	
	python manage.py update_db --action deleteuser --id u4 --real_name User4 --tz tz4
	
	python manage.py update_db --action modifyuser --id u4 --real_name user4
	
	