from django.core.management.base import BaseCommand

import sqlite3


class Command(BaseCommand):
    help = 'Serial number of the question according to the number of respondents '

    def handle(self, *args, **options):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute("""
                SELECT question_id,
                       (SELECT COUNT(DISTINCT user_id)
                        FROM polls_userresponse ur2
                        WHERE ur2.question_id = ur.question_id
                        GROUP BY ur2.question_id) AS respondent_count,
                       (SELECT COUNT(DISTINCT user_id)
                        FROM polls_userresponse ur2
                        WHERE ur2.question_id = ur.question_id
                        GROUP BY ur2.question_id) * 100 / (SELECT COUNT(DISTINCT user_id) FROM polls_userresponse) AS percentage_respondents
                FROM polls_userresponse ur
                GROUP BY question_id
                ORDER BY respondent_count DESC""")
        results = cursor.fetchall()

        for row in results:
            print(row)

        conn.close()