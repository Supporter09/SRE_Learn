## Ý nghĩa của Kafka 🚀
- Xử lý dữ liệu thời gian thực: Kafka cho phép bạn xây dựng các ứng_dụng có khả năng phản ứng ngay lập tức với các luồng dữ liệu mới, chẳng hạn như phân tích log, theo dõi hoạt động người dùng trên web, hay xử lý giao dịch tài chính.
- Tích hợp hệ thống: Nó hoạt động như một trung tâm trung chuyển, giúp các hệ thống khác nhau (microservices, cơ sở dữ liệu, ứng dụng cũ) có thể trao đổi dữ liệu một cách dễ dàng mà không cần kết nối trực tiếp với nhau. Điều này giúp hệ thống trở nên linh hoạt và dễ bảo trì hơn.
- Độ tin cậy và khả năng chịu lỗi cao: Dữ liệu trong Kafka được lưu trữ một cách bền bỉ và được nhân bản qua nhiều máy chủ. Nếu một máy chủ gặp sự cố, dữ liệu của bạn vẫn an toàn và hệ thống vẫn tiếp tục hoạt động.
- Khả năng mở rộng: Kafka được thiết kế để xử lý một lượng dữ liệu khổng lồ. Bạn có thể dễ dàng thêm các máy chủ mới vào cụm (cluster) để tăng khả năng xử lý khi nhu cầu tăng lên.

## Các thành phần chính 🧩
- Broker: Đây là một máy chủ Kafka. Một cụm Kafka thường bao gồm nhiều broker để đảm bảo khả năng chịu lỗi và cân bằng tải. Broker chịu trách nhiệm nhận, lưu trữ và gửi tin nhắn.

- Topic: Là một danh mục hoặc một "kênh" để chứa các tin nhắn. Ví dụ, bạn có thể có topic user-activity để lưu các hành động của người dùng hoặc topic order-placed để lưu thông tin đơn hàng.

- Partition: Mỗi topic được chia thành nhiều partition. Dữ liệu của một topic sẽ được phân bổ đều vào các partition này. Việc chia partition giúp tăng khả năng xử lý song song và khả năng mở rộng.

- Producer: Là ứng dụng gửi (ghi) tin nhắn vào một topic trong Kafka.

- Consumer: Là ứng dụng đọc (nhận) tin nhắn từ một topic. Nhiều consumer có thể cùng đọc từ một topic.

## Important directives
### Kafka Image Directives

- KAFKA_CFG_ZOOKEEPER_CONNECT: Specifies Zookeeper connection string (e.g. zookeeper:2181)
- ALLOW_PLAINTEXT_LISTENER: Allows unencrypted connections (yes/no)
- KAFKA_CFG_LISTENERS: Configures broker listeners (e.g. PLAINTEXT://:9092)
- KAFKA_CFG_ADVERTISED_LISTENERS: Advertised listeners for clients ( usually IP/DNS clients use to connect with specific broker)
- KAFKA_CFG_BROKER_ID: Unique ID for each broker instance
- KAFKA_CFG_NUM_PARTITIONS: Default number of partitions per topic
- KAFKA_CFG_AUTO_CREATE_TOPICS_ENABLE: Allow automatic topic creation
- KAFKA_HEAP_OPTS: JVM heap size settings
- KAFKA_CFG_LOG_RETENTION_HOURS: How long to keep messages
- KAFKA_CFG_LOG_RETENTION_BYTES: Maximum size of log files
- KAFKA_CFG_DEFAULT_REPLICATION_FACTOR: Default number of replicas for each partition (e.g. 3)
- KAFKA_CFG_MIN_INSYNC_REPLICAS: Minimum replicas that must acknowledge writes (e.g. 2)
- KAFKA_CFG_OFFSETS_TOPIC_REPLICATION_FACTOR: Replication factor for internal offset topics
- KAFKA_CFG_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: Replication factor for transaction topics


## Cách cài đặt single node
1. Zookeeper ( Kafka < 2.8)
- docker-compose.yml:
```
services:
  zookeeper:
    image: docker.io/bitnami/zookeeper:3.8
    environment:
      - ALLOW_ANONYMOUS_LOGIN=yes
    volumes:
      - "zookeeper_data:/bitnami"
    ports:
      - "2181:2181"

  kafka:
    image: docker.io/bitnami/kafka:3.2
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    volumes:
      - "kafka_data:/bitnami"
    environment:
      - KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181
      - ALLOW_PLAINTEXT_LISTENER=yes

    volumes:
    zookeeper_data:
        driver: local
    kafka_data:
        driver: local
```


## Một vài câu lệnh thường dùng: 
- Docker compose thì phải tương tác với container
```bash
docker exec -it <container_id_or_name> kafka-topics.sh --create --topic demo --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 
```

- Create topic:
```bash
kafka-topics.sh --create --topic demo --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 
```

- List topic:
```bash
kafka-topics.sh --list --bootstrap-server localhost:9092
```

- View topic:
```bash
kafka-topics.sh --describe --topic demo --bootstrap-server localhost:9092
```

- Push message into topic:
```bash
kafka-console-producer.sh --broker-list localhost:9092 --topic demo
```

- Read message from topic:
```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic demo --from-beginning
```

- Delete message from topic:
```bash
kafka-topics.sh --delete --topic demo --bootstrap-server localhost:9092
```