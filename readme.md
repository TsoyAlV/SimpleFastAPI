1) Устанавливаем соединение с БД postgres, для этого запускаем docker-compose: 
>> docker-compose up
2) Устанавливаем зависимости 
>> pip install requirements.txt
3) Создаем таблицу БД, для чего запускаем script.py
4) Прописываем в терминале 
>> python -m uvicorn main:app --host "localhost" --port 8002
5) Теперь на localhost:8002/docs можно отправлять запросы серверу