from cs50 import SQL

# connect to database
db = SQL("sqlite:///courses.db")


# C.R.U.D. functions to query the database

# this function will add a new course to our courses table
def add_new_course(name, teacher, room, dept):
  query = """INSERT INTO courses
              (name, teacher, room, department)
              VALUES (?, ?, ?, ?)"""
  row_id = db.execute(query, name, teacher, room, dept)
  # this returns the id of the row that was added
  return row_id

# this function will grab all the courses from our courses table
def get_all_courses():
  query = """SELECT * FROM courses ORDER BY department"""
  # this returns a list of dictionaries
  return db.execute(query)


# this function will get all the info on one course based on it's id
def get_course_info(id):
  query = """SELECT * FROM courses WHERE id = ?"""
  info = db.execute(query, id)[0]
  # this will return one dictionary of course info
  return info
