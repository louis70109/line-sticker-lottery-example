# LINE Sitkcer Lottery Example

## Prerequisite

- Python 3.x
- LINE account

## Development

Create a [LINE bot channel](https://developers.line.biz/console), put `channel secret` and `channel access token` to `.env` columns.


```shell
docker-compose up
```

Health check:

```shell
curl http://localhost:5000/
```

## Deployment

Heroku: comming soon

Set `https://YOUR_DOMAIN/webhooks/line` to your LINE channel webhook at LINE Developer Console.
