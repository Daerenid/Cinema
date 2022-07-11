# Cinema
Python 3.10.2


1. Tworzenie wirtualnego środowiska
```
>> python -m venv venv 
```
2. Aktywacja wirtualnego środowiska
```
>> venv\Scripts\activate
```
3. Instalacja paczek
```
>> pip install -r requirements.txt
```
4. Baza danych
```
>> flask db init
>> flask db migrate
>> flask db upgrade
```
5. Dodanie rekordów do bazy danych (nowy terminal z odpalonym wirtualnym środowiskiem)
```
>> python basicDB.py
```
6. Ustawienie flask
```
>> set FLASK_ENV=development
>> set FLASK_APP=run.py
```

7. Uruchomienie aplikacji
```
>> flask run
```
