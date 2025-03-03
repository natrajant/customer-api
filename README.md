***Customer API***

Built on FastAPI using Python and MySQL database.

The Customer API supports the following operations:
- GET (all customers or by customer id)
- POST (create a new customer)
- PUT (update an entire customer object)
- PATCH (partially update a customer object)
- DELETE (delete a customer by id)

**Build the environment:**

Checkout the code and from the project's root folder run `docker-compose up` to setup the entire environment

The setup does the following:
- Creates a MySQL container service
- Creates a phpmyadmin container service (UI to interact with MySQL)
- API service


Once completed, you can access the API through port 8000
http://localhost:8000/api/v1/customers

As part of the initial setup process, the schema.sql file is used to setup the database and the table(s) in it.
The data added to the table remains persisted due to the docker volume mounted on mysql service

**API docs:**

FastAPI offers Swagger docs out of the box. The following is the swagger docs url
http://localhost:8000/docs


Future Kubernetes setup:
The helm chart setup under the `hold` folder can be extended to setup the services in a kubernetes environment as part of deployments that can scale independently by changing their replicaSets.

Salt configuration work:
The .env files can be configured to be laid down based on the environment they are running such as dev, qa, e2e (integration) etc.