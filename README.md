

# Assignment 4 – Database Migrations with Flyway, Ansible & CI/CD

## Steps Performed
1. Created MySQL container using Ansible.
2. Created database and user (`sub_user` / `sub_pass`).
3. Used Flyway for schema version control:
   - `V1__create_subscribers.sql` → initial migration
   - `V2__add_status_and_index.sql` → incremental migration
4. Implemented CI/CD using GitHub Actions:
   - Runs Flyway migrations
   - Executes pytest CRUD tests

## How to Run Locally
```bash
ansible-playbook ansible/up.yml
pytest tests/
ansible-playbook ansible/down.yml
