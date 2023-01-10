import datetime


class ReservationLogger:

    def __init__(self, personID=None, name=None, phone=None, email=None, address=None, date_from=None, date_to=None,
                 room_num=None, room_type=None, meals=None, comments=None):

        self.personID = personID
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.date_from = date_from
        self.date_to = date_to
        self.room_num = room_num
        self.room_type = room_type
        self.meals = meals
        self.comments = comments
        dt = str(datetime.datetime.today())
        idx = dt.rindex(".")
        self.log_time_stamp = dt[0: idx]

    def insert_sql_command(self):
        sql = "insert into ReservationLogger values(null, '{name}', " \
              "'{phone}', '{email}', '{address}', '{date_from}','{date_to}',{room_num},'{room_type}','{meals}'," \
              "'{comments}')".format_map(vars(self))
        return sql

    def delete_sql_command(self):
        return "delete from ReservationLogger where personID = {}".format(self.personID)

    def fetch_sql_command(self):
        return "select * from ReservationLogger"
