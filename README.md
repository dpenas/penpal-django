# Penpal API

This API is made with the idea of finding people to talk to in other languages.

## Usage
If you have Docker installed locally, run `docker-compose up -d` on the main folder.
Create a DB called `penpals` on postgres and run the migrations inside the web container: `python manage.py migrate`
Copy the `.env.example` from the project and name it, in the same folder, as `.env` 

## Current endpoints
- *api/users/* - POST and GET endpoint for creating and retrieving the users.
- *api/users/{id}/messages/sent* - GET endpoint to retrieve the messages that the user has sent.
- *api/users/{id}/messages/received* - GET endpoint to retrieve the messages that the user has received.
- *api/messages* - POST endpoint to send a message `body` from a user `from_user` to another one `to_user` 

## TODO
- *Authentication*: Currently everyone can access and send messages to everyone.
- *Full REST endpoints*: The user should also be deleted and updated.
- *More functionality*: Marking a message as read, creating a profile for the user, deleting messages...
