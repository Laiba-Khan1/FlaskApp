from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to hold student data (in-memory storage)
students = []

# Home route - shows the form and main buttons
@app.route('/')
def home():
    return render_template('index.html')

# Route to add a student
@app.route('/add_student', methods=['POST'])
def add_student():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    city = request.form['city']

    # Add the student to the list
    students.append({
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'city': city
    })

    return redirect(url_for('home'))

# Route to display all students
@app.route('/display_students')
def display_students():
    return render_template('display_students.html', students=students)

# Route to delete all students
@app.route('/delete_students')
def delete_students():
    students.clear()
    return redirect(url_for('home'))

# ? Route to delete a specific student by index
@app.route('/delete_student/<int:index>')
def delete_student(index):
    if 0 <= index < len(students):
        students.pop(index)
    return redirect(url_for('display_students'))

if __name__ == '__main__':
    app.run(debug=True)
