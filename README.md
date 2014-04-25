django-sample
=============

Sample Django deployment



To drop the `polls` app you can generate the drop SQL statements, then pipe it to the database shell.

    ./manage.py sqlclear polls | ./manage.py dbshell