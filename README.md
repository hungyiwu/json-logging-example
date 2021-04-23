# demo json logging

## run demo
```
docker-compose build
docker-compose up -d
curl localhost:10080
tail ./log/app.log
```

## goal
log json and only json per line, while still keeping `asctime`, `levelname` and other native useful information.