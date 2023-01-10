from flask import *

from Session18A import DBHelper
from Session18B import ReservationLogger


app = Flask("ReservationLogger")
db_helper = DBHelper()


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/about")
def add_health_log():
    return render_template("about.html")


@app.route("/add")
def about():
    return render_template("add-reservation-log.html")


@app.route("/logs")
def view_all_logs():

    reservation_logger_object = ReservationLogger()
    sql = reservation_logger_object.fetch_sql_command()

    rows = db_helper.read(sql)

    return render_template("logs.html", result=rows)


@app.route("/cancel/<personID>")
def delete_log(personID):
    reservation_object = ReservationLogger(personID=personID)
    sql = reservation_object.delete_sql_command()
    db_helper.write(sql)

    return render_template("delete_reservation_log.html", message = "Reservation with "+personID+" deleted successfully..")


@app.route("/save", methods=["POST"])
def save_health_data():
    print("Save health Data Executed...")

    reservation_data_object = ReservationLogger(name=request.form['name'],
                                                phone=request.form['txtPhone'],
                                                email=request.form['email'],
                                                address=request.form['address'],
                                                date_from=request.form['date_from'],
                                                date_to=request.form['date_to'],
                                                room_num=request.form['room_num'],
                                                room_type=request.form['room_type'],
                                                meals=request.form['meals'],
                                                comments=request.form['comments'],
                                                )

    print(reservation_data_object)
    sql = reservation_data_object.insert_sql_command()
    print("SQL IS:", sql)
    db_helper.write(sql)

    return "Reservation Record Added :)"


def main():
    app.run()


if __name__ == "__main__":
    main()
