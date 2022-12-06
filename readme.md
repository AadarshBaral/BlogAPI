
# Blog API

This API is a fully functional Blog API created using Django_Rest_Framework

To get started with Django_Rest_Framework,

- Make a virtual environment ` python -m venv env_name `
- Activate virtual environment  ` env_name\Scripts\activate  `
- Install required modules using requirements.txt  ` pip install -r requirements.txt `

Add rest_framework on settings on instlled apps section

```
INSTALLED_APPS = [
    ......,
    'rest_framework',
    .......
]

```
Now sync your database for the first time:

    python manage.py migrate

We will also create a super user

    python manage.py createsuperuser --username admin --email admin@example.com


## About the API
With this API, a user can perform all the basic CRUD ( Create, Read, Update and Delete) operations and the
 app is layered with token based authentication.



# Using the API
- Run the server `python manage.py runserver`
- Go to localhost:port/register/ and send a POST request
```
{
    "username" : "here",
    "password" : "here",
}


```
- You will get a token keep the token with you.
- Try to do a GET request with Authorization header and your token
- You can now do a post request as well.

### Adding a post
Post a json request with the fields

    {
        "title" : "",
        "content" : ""
    }
And wallah! You now have a new post.
To Edit the post, go to ` localhost:8000/post_id ` and send a PUT request with the fields updated