### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL? Postgresql is a free and open relational database managment system that works with SQL.

- What is the difference between SQL and PostgreSQL? PostgreSQL is free open source with object-relational methods, SQL is purely relational database and a little less user friendly.

- In `psql`, how do you connect to a database? \c

- What is the difference between `HAVING` and `WHERE`? "HAVING": determines which grouped results, "WHERE": decide which row to use.

- What is the difference between an `INNER` and `OUTER` join? "INNER": only rows that match the coditions are selected; also default selection if not specified. "OUTER": Matches tables with the results being the unmatched data from the table rows.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join? "LEFT OUTER": all the rows from the first table(left) combined with matching rows from the second table(right). "RIGHT OUTER": Matches all the rows from the second table with the first table.

- What is an ORM? What do they do? ORM means object oriented related mapping. Its a framework that helps you use flask with SQL.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`? AJAX is used for getting data from a server API with javascript. "requests" is used with the REST method it allows us to pull data from HTML formsn and used that to manipulate the URL.

- What is CSRF? What is the purpose of the CSRF token? Cross-Site requests forgery, A CSRF token validates the form for our website. So a bad actor cant set up a hidden form field that will cause some damaage.

- What is the purpose of `form.hidden_tag()`? It's used to add the token to our form but we want it hidden. It helps us validate that the form is the right form and not some bad actors form.
