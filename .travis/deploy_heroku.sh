#!/bin/sh
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
heroku plugins:install heroku-container-registry
docker login -u $DOCKER_USER -p $DOCKER_PASS --password=$HEROKU_PASSWORD registry.heroku.com
heroku container:push web --app $HEROKU_APP_NAME