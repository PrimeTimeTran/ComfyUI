# Tools

- [PostgresApp](https://postgresapp.com/)
- [PGAdmin](https://www.pgadmin.org/download/)

Install
cd /usr/local/bin

Configure data path
initdb -D ~/pg

Start PG
pg_ctl -D /Users/future/pg -l logfile start

Create DB
createdb mydatabase

View DBs
psql -l

Connect to your DB
psql -d mydatabase

You should enter PG REPL

Display all tables
\dts

View available commands
\?

Exit PG
\q
