from django.core.management.base import BaseCommand

import sqlite3


class Command(BaseCommand):
    help = 'Total number of polls participants'

    def handle(self, *args, **options):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(DISTINCT user_id) AS total_participants '
                       'FROM polls_userresponse;')
        results = cursor.fetchall()

        for row in results:
            print(row)

        conn.close()
