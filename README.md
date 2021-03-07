**Myopinion** -  is a service, where you can write a review/opinion
about different things
(Now in development)
********
**How to run a project:** 

- **Project cloning**

`git clone https://github.com/olegmlavets/myopinion`

- **Creating a file with environment variable(optional)**
 
`touch .env.dev`
with such variables inside:

```
SQL_ENGINE=django.db.backends.postgresql 
SQL_DATABASE=db
SQL_USER=user
SQL_PASSWORD=db_password
SQL_PORT=5432
SQL_HOST=db
EMAIL_HOST_USER=user@mail.com
EMAIL_HOST_PASSWORD=mail_password
```
 - **Project launch**

`docker-compose up`

 - **In the plans**

`Add email notifications via celery`

`Optimize docker containers`
