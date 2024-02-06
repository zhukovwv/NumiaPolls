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
```bash
python manage.py SQL_Total_Participants_of_Polls
```
```sql
SELECT COUNT(DISTINCT user_id) AS total_participants
FROM polls_userresponse;
```

-- Количество ответивших и их доля
```bash
python manage.py SQL_Respondent_Count_and_Share
```
```sql
SELECT COUNT(DISTINCT user_id) AS respondents_count,
       COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(DISTINCT user_id) FROM polls_userresponse) AS percentage_respondents
FROM polls_userresponse;
```

-- Порядковый номер вопроса по количеству ответивших
```bash
python manage.py SQL_Question_Number_by_Respondent_Count
```
```sql
SELECT question_id, RANK() OVER (ORDER BY COUNT(DISTINCT user_id) DESC) AS question_rank
FROM polls_userresponse
GROUP BY question_id;
```

-- Количество ответивших на каждый из вариантов ответа и их доля:
```bash
python manage.py SQL_Respondents_Per_Answer_Option_and_Share
```
```sql
SELECT question_id, choice_id,
       COUNT(DISTINCT user_id) AS respondents_count,
       COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(DISTINCT user_id) FROM polls_userresponse WHERE question_id = qr.question_id) AS percentage_respondents
FROM polls_userresponse qr
GROUP BY question_id, choice_id;
```

