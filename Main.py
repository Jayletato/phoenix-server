from flask import Flask, render_template
from json import load, dump
import random

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    
    main = dict()
    task = dict()
    

    with open("./templates/tasks.json") as file:
        main = load(file)
    
    with open("./templates/task.json") as file:
        task = load(file)

    #temp = main['template']
    #main[str(random.randint(1, 10000))] = temp

    main["8456"]["tasks"].append(task)

    with open("./templates/tasks.json", "w") as file:
        dump(main, file, indent = 4)
    
    return str(1)


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host = '0.0.0.0')