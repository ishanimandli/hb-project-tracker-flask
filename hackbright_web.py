"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template,redirect

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    # github = "jhacks"

    first, last, github = hackbright.get_student_by_github(github)

    return render_template("student_info.html", first = first, last = last, github = github)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-insert")
def create_student_form():
    """Show form for searching for a student."""

    return render_template("create_student.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    first_name = request.form.get('f_name')
    last_name = request.form.get("l_name")
    github = request.form.get('github_name')

    hackbright.make_new_student(first_name,last_name,github)
    return render_template("acknowledge_student.html")  




if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
