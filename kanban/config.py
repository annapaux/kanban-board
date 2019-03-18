app.config.update(dict(
    DATABASE=os.path.join(app.instance_path, 'kanban.sqlite'),
    DEBUG=True,
    SECRET_KEY='dev',
    USERNAME='admin',
    PASSWORD='admin'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
