from flask import Flask , request , jsonify , make_response
app = Flask(__name__)

""" @app.route('/task')
def hello():
    return 'Hello World!' """

tasks = {
    '1' : {
        "task_id" : "1",
        "title" :"flask api",
        "desc" : "to create a flask rest api",
        "due_date" : "11-06-23",
        "status" : " inprogress" 
    },
    '2' : {
        "task_id" : "2",
        "title" :"flask backend",
        "desc" : "to create get and post request",
        "due_date" : "11-06-23",
        "status" : " incomplete" 
    }
}



@app.route('/funnlHQ/tasks', methods=['GET', 'POST'])
def emp_tasks():
    if request.method == "GET":
        return make_response(jsonify(tasks),200)
    elif request.method == 'POST':
        content = request.json
        task_id = content['task_id']
        tasks[task_id] = content

        task_obj = tasks.get(task_id,{})
        return make_response(jsonify(task_obj),201)
    
@app.route('/funnlHQ/tasks/<task_id>', methods=['GET', 'POST','DELETE'])
def each_task(task_id):
    if request.method == "GET":
        task_obj = tasks.get(task_id,{})
        if task_obj:
            return make_response(jsonify(task_obj),200)
        else:
            return make_response(jsonify(task_obj),404)
    elif request.method == "PUT":
        content = request.json   
        tasks[task_id] = content
        task_obj = tasks.get(task_id,{})
        return make_response(jsonify(task_obj),200)
    elif request.method == "DELETE":
        if task_id in tasks:
            del tasks[task_id]

        return make_response(jsonify({}),204)    





if __name__ == '__main__':
    app.run(debug=True) 