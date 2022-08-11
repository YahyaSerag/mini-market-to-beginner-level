from market import app, db

if __name__ == "__main__":
    # db.create_all()
    # db.drop_all()

    app.run(debug=True, port=5000)
