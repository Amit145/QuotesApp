REM build docker compose
cd ./QuotesAppAPI
docker-compose build

REM run
docker-compose up --scale quotes-web=1
