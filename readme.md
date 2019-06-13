# Setup

`pipenv install`

# Run app

`pipenv run python main.py`

# Run Tests

`pipenv run pytest .`


# TODO

1. `db_manager` module require additional improvements (separate models and db management functions)
2. landmarks require UI and tests
3. `Route` class closely related to DB
4. need to improve user experience overall
5. robots can use only last route for now

# Answers

**A system with millions of routes vs. a system with < 100 routes**

Better DBMS.
DB optimization for save and retrieve routers.

**A system where routes have thousands of instructions each vs. a system where routes have 1-10 instructions**

Routes parsing could be called in async task

**A system with millions of simultaneous users vs. <10 simultaneous users**

Diferent cache strategies, DB indexes, load balancing for millions of simultaneous users case

**A system where routes are frequently changed and updated vs. one where routes are permanent once initially devised**

Better DBMS for system where routes are frequently changed and updated
Cache for system where routes are permanent once initially devised
