import pymysql


def get_connection():

    conn = pymysql.connect(

        host="mysql-32ebd944-dlu-b688.f.aivencloud.com",

        port=17574,

        user="avnadmin",

        password="AVNS_Fnjdqp0jL8Y2Itgmb5C",

        database="company1",

        ssl={
            "ca": "ca.pem"
        }

    )

    return conn
