from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from kanban.auth import login_required
from kanban.db import get_db

bp = Blueprint('kanban', __name__)


@bp.route('/')
def to_main():
    return redirect(url_for('kanban.main'))

@bp.route('/main')
@login_required
def main():
    '''
    Fetches all tasks from the database, and sends
    the information to the kanban/home.html template file.
    '''
    db = get_db()
    user_id = str(g.user['id'])

    todos = db.execute(
        'SELECT t.id, u.id, t.body, t.category, t.deleted'
        ' FROM task t JOIN user u ON t.user_id = u.id'
        ' WHERE u.id= (?) AND t.category=1 AND t.deleted=(?)'
        ' ORDER BY t.created ASC',
        (user_id, False)).fetchall()

    doings = db.execute(
        'SELECT t.id, u.id, t.body, t.category, t.deleted'
        ' FROM task t JOIN user u ON t.user_id = u.id'
        ' WHERE u.id= (?) AND t.category=2 AND t.deleted=(?)'
        ' ORDER BY t.created ASC',
        (user_id, False)).fetchall()

    dones = db.execute(
        'SELECT t.id, u.id, t.body, t.category, t.deleted'
        ' FROM task t JOIN user u ON t.user_id = u.id'
        ' WHERE u.id= (?) AND t.category=3 AND t.deleted=(?)'
        ' ORDER BY t.created ASC',
        (user_id, False)).fetchall()

    return render_template('kanban/home.html', todos=todos, doings=doings, dones=dones)



@bp.route('/add', methods=('GET', 'POST'))
@login_required
def add():
    '''
    When users click the submit button, this function
    adds the new task to the database and redirects to
    the main() where the data will be fetched and displayed.
    '''
    if request.method == 'POST':
        category = request.form['category']
        body = request.form['body']
        error = None

        if not category:
            error = 'Category is required.'
        if not body:
            error = 'Task description is required.'

        if error is not None:
            flash(error)
        else:
            user_id = str(g.user['id'])
            db = get_db()
            db.execute(

                'INSERT INTO task (body, category, deleted, user_id)'
                ' VALUES (?, ?, ?, ?)',
                (body, category, False, user_id)
            )
            db.commit()
    return redirect(url_for('kanban.main'))


@bp.route('/update', methods=('GET', 'POST'))
@login_required
def update():
    '''
    When users click 'doing' or 'done' on an existing
    task, this function updates the task category in the
    database and redirects to main().
    '''
    if request.method == 'POST':
        taskid = request.form['taskid']
        category = request.form['category']
        error = None

        if category == "doing":
            category = 2
        elif category == "done":
            category = 3
        else:
            error = 'Category misspecified.'

        if error is not None:
            flash(error)


        else:
            db = get_db()
            db.execute(
                'UPDATE task SET category = ?'
                ' WHERE id = ?',
                (category, taskid))
            db.commit()

    return redirect(url_for('kanban.main'))

@bp.route('/delete', methods=('GET', 'POST'))
@login_required
def delete():
    '''
    When a user clicks the trash can button to delete the task,
    this function sets the task.deleted column to True.
    It redirects to main(), which filters tasks based on deleted=False.
    '''
    taskid = request.form['taskid']
    db = get_db()
    db.execute(
        'UPDATE task SET deleted = ?'
        'WHERE id = ?',
        (True,taskid))
    db.commit()
    return redirect(url_for('kanban.main'))
