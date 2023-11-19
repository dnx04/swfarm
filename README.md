# swfarm

One should install this farm on cloud-hosted vulnbox for best configuration and performance.

## Usage:
- Change the [./server/app/config.py](./server/app/config.py) file to your liking
    (don't forget to change the `SERVER_PASSWORD`).
- `docker compose up --build -d` (or `make`)

## Run your exploit
`./swfarm/client/start_sploit.py <python/perl/ruby exploit file> --server-url <server url> --server-pass <server pass`
