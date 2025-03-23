Project Setup

1. Clone the repository
git clone https://github.com/Nafeesp2001/library_management.git
cd library_management

2. Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

3. Install required dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Create a superuser to manage the books
python manage.py createsuperuser

6. Start the server 
python manage.py runserver
 

Now, open your terminal and use cURL to interact with Django REST Api.

7. Create an Admin User using the below command
curl -X POST http://127.0.0.1:8000/api/admin/signup/ \
     -H "Content-Type: application/json" \
     -d '{"email": "admin@example.com", "password": "yourpassword"}'

8. Now once signed up, you can login and get your access token in order to perform CRUD operations.
curl -X POST http://127.0.0.1:8000/api/admin/login/ \
     -H "Content-Type: application/json" \
     -d '{"email": "admin@example.com", "password": "yourpassword"}'

Expected Response:
{
    "refresh": "your_refresh_token_here",
    "access": "your_access_token_here"
}
Copy the access token for further API requests.

9. To list all the books send the GET request
curl -X GET http://127.0.0.1:8000/api/books/ \
     -H "Authorization: Bearer your_access_token_here"

10. To Add a new book {Requires Authentication}
curl -X POST http://127.0.0.1:8000/api/books/ \
     -H "Authorization: Bearer your_access_token_here" \
     -H "Content-Type: application/json" \
     -d '{
          "title": "1984",
          "author": "George Orwell",
          "isbn": "9780451524935",
          "published_date": "1949-06-08"
     }'

11. Update book details 
curl -X PUT http://127.0.0.1:8000/api/books/1/ \
     -H "Authorization: Bearer your_access_token_here" \
     -H "Content-Type: application/json" \
     -d '{
          "title": "1984 - Updated Edition",
          "author": "George Orwell",
          "isbn": "9780451524935",
          "published_date": "1950-06-08"
     }'

12. Delete the book 
curl -X DELETE http://127.0.0.1:8000/api/books/1/ \
     -H "Authorization: Bearer your_access_token_here"

13. Student view to see all the books
http://127.0.0.1:8000/api/student/