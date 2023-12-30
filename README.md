# v-league-data-api

## 🔨Setup
```
make setup
```
if you can not use ```make``` command or error occurs, use the below command.
```
docker-compose build
docker-compose up -d
```

### Enter container
```
make enter
```
or
```
docker-compose exec python bash
```

## 🏃Run
```
make start
```
or
```
doker-compose start
docker-compose exec python bash
```
### Run python file
```
python3 main.py
```
### Stop containers
```
make stop
```
or
```
docker-compose stop
```

## 🔧Debug
Point your WebDriver tests to http://localhost:4444

👀 To see what is happening inside the container, head to http://localhost:7900/?autoconnect=1&resize=scale&password=secret