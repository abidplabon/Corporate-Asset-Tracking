Goals:
1.The application might be used by several companies
2.Each company might add all or some of its employees
3.Each company and its staff might delegate one or more devices to employees for a certain period of time
4.Each company should be able to see when a Device was checked out and returned
5.Each device should have a log of what condition it was handed out and returned


Setup:
1.Clone it from github using-
	- git clone 
2.Install required packages
	- pip install - r requirements.txt
3.Setup Database
	- python manage.py makemigrations
	- python manage.py migrate
4.Create Superuser
	- python manage.py createsuperuser
	- Enter email,name,password,confirm password
5.Run the project
	- python manage.py runserver



API Endpoints:

Admin Panel : `http://127.0.0.1:8000/admin/`

1.http://127.0.0.1:8000/api/ - API Root
2.http://127.0.0.1:8000/api/companyprofile/ - Register Company
3.http://127.0.0.1:8000/api/login/ - Login with token
4.http://127.0.0.1:8000/api/employee-records/ - After login to enter an employee records

![Company_Register](https://github.com/abidplabon/Corporate-Asset-Tracking/assets/54079464/b0e711c4-1f7e-4c71-94bf-3c060aa67e41)

![CURD_Employee_Records](https://github.com/abidplabon/Corporate-Asset-Tracking/assets/54079464/d2d302a4-e16d-46b3-b494-4b5da1c73431)

![Employee_Record](https://github.com/abidplabon/Corporate-Asset-Tracking/assets/54079464/be85f7f5-2e26-4af0-93be-78861537798d)

![Login](https://github.com/abidplabon/Corporate-Asset-Tracking/assets/54079464/efc232f3-d823-4ce5-a710-b07916f8b12b)


