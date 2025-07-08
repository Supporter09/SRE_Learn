## What is the meaning of Load balancer ?
### 1. Definition
A load balancer is a system component that:
- Distributes incoming traffic across multiple servers.
- Ensures high availability, scalability, and fault tolerance.
- Can operate at Layer 4 (TCP/UDP) or Layer 7 (HTTP/HTTPS).


### 2. How it works:
1. Client makes a request → reaches the load balancer.
2. The load balancer selects a backend server based on a strategy:
- Round Robin: alternate requests evenly.
- Least Connections: choose server with the fewest active connections.
- IP Hash: hash client IP to pick server (useful for sticky sessions).
3. Forwards request to that backend server.
4. Backend responds → response flows back through the load balancer to client.

## How to install:
### 1. Install NGINX on Ubuntu
```bash
sudo apt update
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```

### 2. Install NGINX on RedHat/CentOS
```bash
sudo yum install epel-release -y
sudo yum install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx

# If EPEL isn't enabled:
sudo dnf install epel-release -y   # For CentOS 8+, RHEL 8+
```

### 3. Run NGINX in Docker Container
```bash
docker run -d --name nginx-server -p 80:80 nginx
```
Mount local config
```bash
docker run -d --name nginx \
  -v .nginx/config/nginx.conf:/etc/nginx/nginx.conf \
  -v .nginx/html:/usr/share/nginx/html \
  -p 80:80 nginx
```
## High Availability NGINX Setup ( HA ) (https://viblo.asia/p/tim-hieu-ve-nginx-de-high-availability-p3-MkNLr52OJgA)
High availability usually involves 2 or more NGINX nodes + a load balancer + keepalived/corosync.

Basic structure:
- Use Keepalived for virtual IP (VIP) failover between 2 NGINX servers.

Install Keepalived (Ubuntu):
```bash
sudo apt install keepalived -y
```
Example config /etc/keepalived/keepalived.conf:
```
    vrrp_instance VI_1 {
        state MASTER
        interface eth0
        virtual_router_id 51
        priority 100
        advert_int 1
        authentication {
            auth_type PASS
            auth_pass 1234
        }
        virtual_ipaddress {
            192.168.1.100
        }
    }
```

## Common NGINX Commands
```bash
sudo systemctl start nginx        # Start service
sudo systemctl stop nginx         # Stop service
sudo systemctl restart nginx      # Restart service
sudo systemctl reload nginx       # Reload config without downtime
sudo nginx -t                     # Test config file
sudo nginx -s reload              # Reload (alternative)
```

## NGINX Folder Structure
| Path                          | Description                         |
| ----------------------------- | ----------------------------------- |
| `/etc/nginx/nginx.conf`       | Main config file                    |
| `/etc/nginx/sites-available/` | Virtual host configs (Debian-based) |
| `/etc/nginx/sites-enabled/`   | Enabled virtual hosts               |
| `/usr/share/nginx/html/`      | Default document root               |
| `/var/log/nginx/access.log`   | Access logs                         |
| `/var/log/nginx/error.log`    | Error logs                          |
| `/etc/nginx/conf.d/`          | Additional config files             |

## NGINX Configuration (nginx.conf) Structure
```
    user www-data;
    worker_processes auto;
    events {
        worker_connections 1024;
    }
    http {
        include       mime.types;
        default_type  application/octet-stream;

        sendfile        on;
        keepalive_timeout  65;

        server {
            listen 80;
            server_name example.com;

            location / {
                root   /usr/share/nginx/html;
                index  index.html index.htm;
            }
        }
    }
```
| Directive                 | Purpose                      |
| ------------------------- | ---------------------------- |
| `worker_processes`        | Number of worker processes   |
| `worker_connections`      | Max connections per worker   |
| `listen`                  | Port to bind server block    |
| `server_name`             | Domain name for server block |
| `location`                | URL path matching            |
| `proxy_pass`              | Forward request to upstream  |
| `include`                 | Import other config files    |
| `access_log`, `error_log` | Logging paths                |

## Reverse Proxy and Forward Proxy
1. What is Proxy Server?
- An intermidiate actor between client and server to ask and recieve resource and hide the true identity for security

2. Forward Proxy ( Open Proxy )
- Can be access by any user
- Two main types:
    - Anonymous proxy (proxy ẩn danh) => Not show the original IP of client
    - Trаnspаrent proxy (proxy minh bạch): Opposite side, and working by forward request with HTTP Header => Original IP can be found and this type of proxy might beneficial caching a website
- Being used by client ( web browser )

3. Reverse Proxy
- Stand before the real server to handle the income requests and divide it for real servers and send back the results => hide identity of real servers for security problems
- Being used by server ( web server ) => Usually being installed in a private network of one or many servers => All requests must go through reverse proxy.

| Feature          | Reverse Proxy                             | Forward Proxy                       |
| ---------------- | ----------------------------------------- | ----------------------------------- |
| Clients          | Internet users                            | Internal users                      |
| Servers          | Backend servers (e.g., app/web servers)   | Internet resources (e.g., websites) |
| Purpose          | Load balancing, security, caching         | Bypass filters, privacy, caching    |
| Visibility       | Client doesn't know backend IP            | Server doesn't know client IP       |
| Common Use Cases | Web server fronting many backend services | Corporate firewall, content filters |
| Example Tool     | NGINX, HAProxy                            | Squid, Privoxy                      |
