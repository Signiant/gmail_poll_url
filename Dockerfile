FROM python:2-onbuild

MAINTAINER devops@signiant.com

CMD [ "python", "./gmailPoller.py", "gmail_config.json" ]
