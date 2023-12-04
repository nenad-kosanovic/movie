# movie
Implement a python server using flask that can create, fetch, update & delete information aboout movies. Each movie should atleast store the following information:
- Name
- Language
- Genres (can be multiple)
- Runtime
- Description


Also implement a GoLang client which communicates with the above server to create/update/delete some movies. 
IMPORTANT NOTE: Use proto as means of serialisation for sending requests b/w client & server

This exercise will touch upon:
- protos (Google Protobufs)
- Golang HTTP Server & request handling
- Python HTTP client
- Usage of protos in HTTP requests