# Penpal API

This API is made with the idea of finding people to talk to in other languages.

## Current endpoints
- *api/users/* - POST and GET endpoint for creating and retrieving the users.
- *api/users/{id}/messages/sent* - GET endpoint to retrieve the messages that the user has sent.
- *api/users/{id}/messages/received* - GET endpoint to retrieve the messages that the user has received.
- *api/messages* - POST endpoint to send a message `body` from a user `from_user` to another one `to_user` 

## TODO
- *Authentication*: Currently everyone can access and send messages to everyone.
- *Full REST endpoints*: The user should also be deleted and updated.
- *More functionality*: Marking a message as read, creating a profile for the user, deleting messages...
