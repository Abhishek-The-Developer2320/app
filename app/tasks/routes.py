from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app.extensions import db
from app.tasks.models import Task
from app.tasks.forms import TaskForm
from app.projects.models import Project

bp = Blueprint("tasks", __name__, template_folder="templates/tasks")

@bp.route("/<int:project_id>/add", methods=["GET", "POST"])
@login_required
def add_task(project_id):
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            project_id=project_id
        )
        db.session.add(task)
        db.session.commit()
        flash("Task added!")
        return redirect(url_for("projects.dashboard"))
    return render_template("task_detail.html", form=form)
