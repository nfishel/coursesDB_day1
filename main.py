from flask import Flask, request, render_template, redirect
import queries as q

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
  if request.method == "GET":
    # show the page with the form
    return render_template("add.html")
  else: # post request method (filled out the from)
    # get all the info from the form
    name = request.form.get("courseName")
    teacher = request.form.get("teacher")
    room = request.form.get("room")
    dept = request.form.get("department")
    # use the above data to run the query to insert a course
    course_id = q.add_new_course(name, teacher, room, dept)
    return render_template("success.html", name=name)
    

@app.route("/show")
def show():
  # frist grab all the courses
  course_list = q.get_all_courses()
  return render_template("show.html", courses=course_list)

@app.route("/edit/<int:id>")
def edit(id):
  # ask the database for the all the infor on this one course
  course_info = q.get_course_info(id)
  return render_template("edit.html", info=course_info)
  
  


if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)