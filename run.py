from flaskblog import create_app

app, manager = create_app()

if __name__ == '__main__':
    app.run(debug=True)
#    manager.run()
