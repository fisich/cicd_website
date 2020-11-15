#!/bin/sh
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
heroku plugins:install heroku-container-registry
docker login -u $DOCKER_USER -p DOCKER_PASSWORD --password=$HEROKU_API_KEY registry.heroku.com
heroku container:login
heroku container:push web --app $HEROKU_APP_NAME
heroku container:release web --app $HEROKU_APP_NAME