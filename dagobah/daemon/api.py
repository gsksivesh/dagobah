""" HTTP API methods for Dagobah daemon. """

from flask import abort

from dagobah.daemon.daemon import app
from dagobah.daemon.util import validate_dict, api_call

dagobah = app.config['dagobah']


@app.route('/api/jobs', methods=['GET'])
@api_call
def get_jobs():
    return dagobah._serialize().get('jobs', {})


@app.route('/api/head', methods=['GET'])
@api_call
def head_task():
    args = dict(request.args)
    if not validate_dict(request.args,
                         required=['job_name', 'task_name'],
                         job_name=str,
                         task_name=str,
                         stream=str,
                         num_lines=int):
        abort(400)

    job = dagobah.get_job(args['job_name'])
    task = job.tasks.get(args['task_name'], None)
    if not task:
        abort(400)
    return task.head(**args)


@app.route('/api/tail', methods=['GET'])
@api_call
def tail_task():
    args = dict(request.args)
    if not validate_dict(request.args,
                         required=['job_name', 'task_name'],
                         job_name=str,
                         task_name=str,
                         stream=str,
                         num_lines=int):
        abort(400)

    job = dagobah.get_job(args['job_name'])
    task = job.tasks.get(args['task_name'], None)
    if not task:
        abort(400)
    return task.tail(**args)


@app.route('/api/add_job', methods=['POST'])
@api_call
def add_job():
    args = dict(request.form)
    if not validate_dict(request.form,
                         required=['job_name'],
                         job_name=str):
        abort(400)

    dagobah.add_job(args['job_name'])


@app.route('/api/delete_job', methods=['POST'])
@api_call
def delete_job():
    args = dict(request.form)
    if not validate_dict(request.form,
                         required=['job_name'],
                         job_name=str):
        abort(400)

    dagobah.delete_job(args['job_name'])


@app.route('/api/start_job', methods=['POST'])
@api_call
def start_job():
    args = dict(request.form)
    if not validate_dict(request.form,
                         required=['job_name'],
                         job_name=str):
        abort(400)

    job = dagobah.get_job(args['job_name'])
    job.start()


@app.route('/api/retry_job', methods=['POST'])
@api_call
def retry_job():
    args = dict(request.form)
    if not validate_dict(request.form,
                         required=['job_name'],
                         job_name=str):
        abort(400)

    job = dagobah.get_job(args['job_name'])
    job.retry()


@app.route('/api/add_task_to_job', methods=['POST'])
@api_call
def add_task_to_job():
    args = dict(request.form)
    if not validate_dict(request.form,
                         required=['job_name', 'task_command', 'task_name'],
                         job_name=str,
                         task_command=str,
                         task_name=str):
        abort(400)

    dagobah.add_task_to_job(args['job_name'],
                            args['task_command'],
                            args['task_name'])


@app.route('/api/add_dependency', methods=['POST'])
@api_call
def add_dependency():
    args = dict(request.form)
    if not validate_dict(request.form,
                         required=['job_name',
                                   'from_task_name',
                                   'to_task_name'],
                         job_name=str,
                         from_task_name=str,
                         to_task_name=str):
        abort(400)

    job = dagobah.get_job(args['job_name'])
    job.add_dependency(args['from_task_name'], args['to_task_name'])


@app.route('/api/schedule_job', methods=['POST'])
@api_call
def schedule_job():
    args = dict(request.form)
    if not validate_dict(request.form,
                         required=['job_name', 'cron_schedule'],
                         job_name=str,
                         cron_schedule=str):
        abort(400)

    job = dagobah.get_job(args['job_name'])
    job.schedule(args['cron_schedule'])


@app.route('/api/stop_scheduler', methods=['POST'])
@api_call
def stop_scheduler():
    dagobah.scheduler.stop()


@app.route('/api/restart_scheduler', methods=['POST'])
@api_call
def restart_scheduler():
    dagobah.scheduler.restart()


@app.route('/api/terminate_task', methods=['POST'])
@api_call
def terminate_task():
    args = dict(request.form)
    if not validate_dict(request.form,
                         required=['job_name', 'task_name'],
                         job_name=str,
                         task_name=str):
        abort(400)

    job = dagobah.get_job(args['job_name'])
    task = job.tasks.get(args['task_name'], None)
    if not task:
        abort(400)
    task.terminate()


@app.route('/api/kill_task', methods=['POST'])
@api_call
def kill_task():
    args = dict(request.form)
    if not validate_dict(request.form,
                         required=['job_name', 'task_name'],
                         job_name=str,
                         task_name=str):
        abort(400)

    job = dagobah.get_job(args['job_name'])
    task = job.tasks.get(args['task_name'], None)
    if not task:
        abort(400)
    task.kill()