from django.core.management.base import BaseCommand

import sqlite3


class Command(BaseCommand):
    help = 'Number of respondents to each answer option and their share'

    def handle(self, *args, **options):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute('''
                SELECT question_id, choice_id,
                       COUNT(DISTINCT user_id) AS respondents_count,
                       COUNT(DISTINCT user_id) * 100 / (
                           SELECT COUNT(DISTINCT user_id)
                           FROM polls_userresponse
                           WHERE question_id = qr.question_id
                       ) AS percentage_respondents
                FROM polls_userresponse qr
                GROUP BY question_id, choice_id
                ORDER BY question_id, choice_id
            ''')
        results = cursor.fetchall()

        for row in results:
            print(row)

        conn.close()
