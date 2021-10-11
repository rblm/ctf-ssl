# ctf-ssl

This is a repo for a CTF challenge. Do not reuse.

Generates unique four word passwords in SSL Django.

Run the docker file as follows

docker pull rblm/ctf-ssl:1.0

docker run -d --name ctf -p 443:443 -p 80:80 ctf-ssl:1.0
