## 1. Redis (REmote DIctionary Server) là một hệ thống key-value store lưu trữ dữ liệu trên RAM, nổi bật với tốc độ truy xuất cực nhanh.

### ✅ Các ứng dụng phổ biến của Redis:
- Caching: Lưu cache dữ liệu truy vấn DB, API để giảm tải hệ thống backend.
 
- Session Store: Lưu session (ví dụ Laravel, ExpressJS session).

- Rate Limiting: Đếm số request của client để giới hạn (chống DDoS, brute force).

- Message Broker / Queue: Dùng làm pub/sub, hàng đợi xử lý background jobs (vd: Laravel queue).

- Leaderboard / Counter: Redis rất nhanh với các thao tác số học đơn giản.

## 2. Các directive quan trọng trong cấu hình Redis (redis.conf)
### Security:
- requirepass <password>: Thiết lập password truy cập Redis. ( Cho Redis < 6 )

- bind 127.0.0.1: Chỉ cho phép localhost kết nối Redis.

- protected-mode yes: Bật chế độ bảo vệ (chỉ cho phép localhost nếu không có password).

### Memory:
- maxmemory <bytes>: Giới hạn bộ nhớ Redis sử dụng (nếu vượt sẽ dùng eviction policy).

- maxmemory-policy allkeys-lru: Chính sách khi đầy bộ nhớ: noeviction, allkeys-lru, volatile-lru, allkeys-random, volatile-ttl.

### Persistence:
- save 900 1 / save 300 10: Cấu hình snapshot RDB – sau 900 giây nếu có ít nhất 1 key thay đổi, sẽ dump ra file.

- appendonly yes: Bật chế độ AOF (Append Only File) để log mọi command.

- appendfsync everysec: Ghi AOF mỗi giây (giữa hiệu năng và an toàn).

### Performance
- databases 16: Redis mặc định có 16 DB logical (0-15).

- tcp-keepalive 300: Giữ kết nối TCP để giảm reconnect.

## 3. Setup a single node Redis
- Set up for Linux:
```bash
sudo apt update && sudo apt upgrade

sudo apt install redis-server

# If need any further configuration check /etc/redis/redis.conf

# Start redis service
sudo systemctl enable redis-server
sudo systemctl start redis-server

# Interact
redis-cli
```

- Set up with docker:
```
# docker-compose.yml
services:
  redis:
    image: redis:7
    container_name: redis_single
    ports:
      - "6379:6379"
    volumes:
      - ./data:/data
    command: >
      redis-server
      --requirepass yourstrongpassword
      --appendonly yes
      --maxmemory 256mb
      --maxmemory-policy allkeys-lru
```