# ACLook - API looking glass

By _Alexandre Corso_

## Build

```
docker build -f Dockerfile -t acorso/aclook .
```

## Run
```
docker run -d --name aclook -p 8179:8179 \
-v /srv/volumes/bird/socket/bird.ctl:/bird.ctl \
acorso/aclook
```

## Some example

- `http://lg.acorso.fr:8179/api/network/45.12.184.0`
- `http://lg.acorso.fr:8179/api/network/45.12.184.0/detail`
- `http://lg.acorso.fr:8179/api/network/45.12.184.0/protocol/ipv4_full_table`
- `http://lg.acorso.fr:8179/api/network/45.12.184.0/protocol/ipv4_core02_ams9`
- `http://lg.acorso.fr:8179/api/asn/35085`