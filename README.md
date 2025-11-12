

# Assignment 4 – Database Migrations with Flyway, Ansible & CI/CD

It demonstrates how to automate database migrations using Flyway, provision environments using Ansible, and integrate everything into a CI/CD pipeline with GitHub Actions.

# Part A – Tools Comparison (Q1)

See Q1_Tools_Analysis.md for the comparison between Flyway and Liquibase, including:

- Overview and key features

- CI/CD integration strategy with diagram

- Table comparing ease of use, rollback, and integration

- Summary on why Flyway fits better for lightweight DevOps pipelines

# Part B – Flyway + Ansible + CI/CD
1️. Run Locally (Manual Mode)
Step 1 – Start MySQL
```docker run --name a4-mysql \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=subscriptions \
  -p 3306:3306 -d mysql:8
```
Step 2 – Run Initial Migration
```
docker run --rm --network host \
  -v $(pwd)/flyway:/flyway \
  flyway/flyway:10 \
  -url=jdbc:mysql://localhost:3306/subscriptions \
  -user=root -password=rootpass \
  -locations=filesystem:/flyway/migrations_initial migrate
```
Step 3 – Run Incremental Migration
```
docker run --rm --network host \
  -v $(pwd)/flyway:/flyway \
  flyway/flyway:10 \
  -url=jdbc:mysql://localhost:3306/subscriptions \
  -user=root -password=rootpass \
  -locations=filesystem:/flyway/migrations_incremental migrate
```
Step 4 – Run CRUD Tests
```
pip install -r requirements.txt
pytest -q
```
Step 5 – Teardown
```
docker rm -f a4-mysql
```
2️. Run via Ansible
To Bring Environment Up
```
ansible-playbook ansible/up.yml
```

This:

Starts the MySQL container

Waits for readiness

Creates DB user

Runs initial Flyway migrations

To Tear Down
```
ansible-playbook ansible/down.yml
```
3️. Run via GitHub Actions (CI/CD)

The CI job:

Spins up a MySQL service (in GitHub-hosted runner)

Runs Flyway initial + incremental migrations inside Docker

Executes CRUD tests using pytest

Prints deployment confirmation

Trigger: On every push to main branch.

4. Test Cases (pytest)

Test	Description
- test_create_subscriber	Inserts a new record
- test_read_subscriber	Reads record by email
- test_update_subscriber	Updates subscriber name
- test_delete_subscriber	Deletes subscriber entry


