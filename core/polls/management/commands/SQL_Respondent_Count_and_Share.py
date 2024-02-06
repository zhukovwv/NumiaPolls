from django.core.management.base import BaseCommand

import sqlite3


class Command(BaseCommand):
    help = 'Number of respondents and their share'

    def handle(self, *args, **options):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(DISTINCT user_id) AS respondents_count,'
                       '       COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(DISTINCT user_id) FROM polls_userresponse) AS percentage_respondents '
                       'FROM polls_userresponse;')
        results = cursor.fetchall()

        for row in results:
            print(row)

        conn.close()