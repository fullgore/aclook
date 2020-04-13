# ACLook - API looking glass

By _Alexandre Corso_

## Build

Create the docker 
```
docker build -f Dockerfile -t acorso/aclook .
```

## Run
We need the bird socket
```
docker run -d --name aclook -p 8179:8179 \
-v /srv/volumes/bird/socket/bird.ctl:/bird.ctl \
acorso/aclook
```

## Some example

- `http://lg.acorso.fr:8179/api/bird/network/45.12.184.0`
- `http://lg.acorso.fr:8179/api/bird/network/45.12.184.0/detail`
- `http://lg.acorso.fr:8179/api/bird/network/45.12.184.0/protocol/ipv4_core02_ams9`
- `http://lg.acorso.fr:8179/api/bird/asn/35085`

The ASN API can be unavailable due to timeout.