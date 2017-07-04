# container-torrify

Torrify a Container into a TOR Hidden Service

```sh
# run a container with a network application
$ docker run -d --name hello_world_container kitematic/hello-world-nginx

# and just link it to this container
$ docker run -tid --link hello_world_container --name hello_world_torrified_container iotdocktor/container-torrify
```

The .onion URLs will be displayed to stdout at startup.

To keep onion keys, or you already have Hostname/PrivateKey for Tor Hidden Service
just mount volume `/var/lib/tor/hidden_service/`

```sh
$ docker run -d --link hello_world_container --name hello_world_torrified_container --volume /path/to/keys:/var/lib/tor/hidden_service/ iotdocktor/container-torrify
```

### Setup port

By default, ports are the same as linked containers, but a default port can be mapped using `PORT_MAP` environment variable.

__Caution__: Using `PORT_MAP` with multiple ports on single service will cause `tor` to fail.


### In-Container Tools

A command line tool `onions` is available in container to get `.onion` url when container is running.

```sh
# Get services
$ docker exec -ti hello_world_torrified_container onions


# Get json
$ docker exec -ti hello_world_torrified_container onions --json

```

