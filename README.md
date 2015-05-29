# gmail_poll_url
Polls gmail and calls a custom URL on a pattern match

## Config file format
````
{
        "username": "YOURUSER@gmail.com",
        "password": "YOURPASSWORD",
        "searchString": "MATCH STRING",
        "url": "URL TO GET ON MATCH"
}

````
Sample docker run command showing how to mount the config file into the container using a data volume on the local docker host
:
````
docker run -d --privileged=true \
              -v /my/local/folder/gmail_config.json:/usr/src/app/gmail_config.json \
              --name gmail_poller \
              signiant/gmail-poll-url
````
