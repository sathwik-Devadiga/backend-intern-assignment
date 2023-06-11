installation:
pip install flask
pip install httpie



GET request to /funnelHQ/tasks returns the details of all books
POST request to /funnelHQ/tasks creates a book with the ID 3 (As per request body)

GET request to /funnelHQ/tasks/3 returns the details of book 3
PUT request to /funnelHQ/tasks/3 to update fields of book 3
DELETE request to /funnelHQ/tasks/3 deletes book 3
[All request is done one cmd using httpie
example:
http GET http://127.0.0.1:5000/funnlHQ/tasks
echo '{"task_id":"3","title":"flask ml" , "desc":"creating ml module","due_date":"13-06-23","status":"completed"}' | http POST http://127.0.0.1:5000/funnelHQ/tasks  
GET http://127.0.0.1:5000/funnlHQ/tasks/2 
DELETE http://127.0.0.1:5000/funnlHQ/tasks/2 
'{"task_id":2,"title":"flask backend project","desc":"to create delete request","due_date":"13/2/23","status":"completed"}' | PUT http://127.0.0.1:5000/funnelHQ/tasks/2
