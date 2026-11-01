# Docker Compose Flask Application with Nginx Reverse Proxy

A containerized Flask web application deployed on Ubuntu with Docker Compose and an Nginx reverse proxy.

![Architecture](assets/architecture.png)

## Overview

The browser reaches Nginx over HTTP on port `80`. Nginx forwards application requests to the Flask service by using the Docker Compose service name `web` and container port `5000`. The Flask application runs under Gunicorn inside a non-root container user. The Flask port is exposed to the Compose network but is not published directly on the Ubuntu host.

## Components

| Component | Purpose | Network exposure |
|---|---|---|
| Ubuntu VM | Hosts Docker Engine and Compose | Lab VM network |
| Nginx `nginx_proxy` | Reverse proxy and HTTP entry point | Host TCP 80 -> container TCP 80 |
| Flask `flask_app` | Python web application served by Gunicorn | Internal Compose network, TCP 5000 |
| `app-network` | Bridge network and service-name discovery | Docker host-local network |

## Repository layout

```text
docker-compose-nginx-ubuntu/
├── app/
│   ├── app.py
│   └── requirements.txt
├── nginx/
│   └── default.conf
├── assets/
│   ├── architecture.png
│   ├── project-cover.png
│   └── request-flow.png
├── docs/
│   ├── CONFIGURATION_REFERENCE.md
│   ├── OPERATIONS_AND_TROUBLESHOOTING.md
│   ├── TECHNICAL_GUIDE.md
│   └── pdf/
├── screenshots/
│   └── README.md
├── scripts/
│   └── install_ubuntu_prerequisites.sh
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Prerequisites

- Ubuntu Linux VM or server
- Docker Engine
- Docker Compose v2 (`docker compose` command)
- TCP port `80` available on the Ubuntu host
- Network access from the browser's machine to the Ubuntu VM

For the lab environment recorded during this build, Ubuntu was `26.04.1 LTS` (Resolute), Docker was `29.1.3`, and Docker Compose was `2.40.3`. Package availability and versions can differ by release.

### Install the Ubuntu packages used in this lab

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-v2
sudo systemctl enable --now docker
docker --version
docker compose version
```

A helper script is provided at `scripts/install_ubuntu_prerequisites.sh`.

## Deploy

Clone this repository or copy the project directory to Ubuntu. From the project directory:

```bash
sudo docker compose config
sudo docker compose build web
sudo docker compose up -d
sudo docker compose ps
```

Expected services:

- `flask_app`: Up
- `nginx_proxy`: Up, with host port `80` mapped to container port `80`

## Test the application

Run these tests on Ubuntu:

```bash
curl -i http://localhost/
curl -i http://localhost/health
curl -i http://localhost/nginx-health
```

Expected behavior:

| URL | Expected result |
|---|---|
| `/` | HTTP 200 and the welcome HTML page |
| `/health` | HTTP 200 JSON with `status`, `hostname`, and UTC `timestamp` |
| `/nginx-health` | HTTP 200 plain text: `Nginx is healthy` |

To access it from another machine on the same reachable network, find the Ubuntu VM address with:

```bash
hostname -I
```

Then open `http://&lt;UBUNTU-VM-IP&gt;/` in the browser. The lab previously displayed `192.168.109.129`, but a DHCP-assigned VM address may change.

## Operations

```bash
# View status
sudo docker compose ps

# Follow service logs
sudo docker compose logs -f --tail=50

# Restart services
sudo docker compose restart

# Stop and remove containers and the Compose network
sudo docker compose down

# Start again
sudo docker compose up -d
```

`docker compose down` removes the containers and project network. It does not delete source files. This project does not currently define a database or persistent application data volume.

## Security and scope

- Flask/Gunicorn runs as a non-root user inside the application image.
- Flask port `5000` is not published to the host; it is available to services on `app-network`.
- Nginx configuration is mounted read-only into its container.
- The current Nginx listener is plain HTTP on port `80`.
- A public domain, TLS certificate, HTTPS listener, production secrets management, and production monitoring are not part of this lab configuration.
- Do not publish passwords, private SSH keys, access tokens, `.env` files, or real internal infrastructure details.

## Troubleshooting

See [Operations and Troubleshooting](docs/OPERATIONS_AND_TROUBLESHOOTING.md) and [Configuration Reference](docs/CONFIGURATION_REFERENCE.md).

## Evidence screenshots

See `screenshots/README.md` for the recommended real screenshots to capture after testing. The architecture graphic is an explanatory diagram, not a terminal screenshot.

## License

No license has been added. Add a license only after choosing the reuse terms you want to grant.
