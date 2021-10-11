#openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
#openssl req  -nodes -new -x509  -keyout server.key -out server.cert -days 365

openssl genrsa 2048 > ssl.key
openssl req -new -x509 -nodes -sha1 -days 365 -key ssl.key > ssl.cert
