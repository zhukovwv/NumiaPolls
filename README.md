# NumiaPolls Project
George Zhukov, 2024

To run local NumiaPolls app backend do the following:

```bash
cd NumiaPolls
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
To run  NumiaPolls app backend with Gunicorn + Nginx do the following:
```bash
sudo docker build -t django-image:latest .
sudo docker-compose up                    
```
-- Общее количество участников опроса
```sql
SELECT COUNT(DISTINCT user_id) AS total_participants
FROM polls_userresponse;
```

-- Для каждого вопроса
```sql
SELECT
    question_id,
    COUNT(DISTINCT user_id) AS participants_count,
    COUNT(DISTINCT user_id) * 100 / total_participants AS participants_percentage,
    RANK() OVER (ORDER BY COUNT(DISTINCT user_id) DESC) AS question_rank
FROM
    polls_userresponse
    CROSS JOIN (
        SELECT COUNT(DISTINCT user_id) AS total_participants
        FROM polls_userresponse
    ) AS total_counts
GROUP BY
    question_id
ORDER BY
    question_rank;
```

-- Для каждого варианта ответа на каждый вопрос
```sql
SELECT
    question_id,
    choice_id,
    COUNT(DISTINCT user_id) AS participants_count,
    COUNT(DISTINCT user_id) * 100 / total_participants AS participants_percentage
FROM
    polls_userresponse
    CROSS JOIN (
        SELECT COUNT(DISTINCT user_id) AS total_participants
        FROM polls_userresponse
    ) AS total_counts
GROUP BY
    question_id,
    choice_id
ORDER BY
    question_id,
    participants_count DESC;
```

