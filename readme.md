
Using from the command line:
```
python exercise_picker_cli.py 3 1 2
```


Usage in the browser: 
Run the server:
```
python excercise_server.py
```

Get a random exercise by visiting the following URL in your browser:
```
http://127.0.0.1:5000/api/v1/exercise?l1=3&l2=1&l3=0
```


# Current Scope


# Next Scope
- Add an ETL pipeline to pull in new exercises from other sources such as web articles, youtube videos, etc.
- Add sticky excercises that should be repeated daily, they should deduct from the category count that they came out of so that the user gets an accurate count of how many excercises per level and type they are supposed to do.