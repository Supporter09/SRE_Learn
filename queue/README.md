## What does queue do?
+ Mục đích: Hàng đợi (Message Queue) đóng vai trò như một "bộ đệm" trung gian, giúp quản lý và điều phối các tác vụ bất đồng bộ trong hệ thống. Thay vì một yêu cầu phải xử lý ngay lập tức, nó sẽ được đẩy vào một hàng đợi và xử lý sau bởi một tiến trình khác.
    + Giảm tải cho ứng dụng: Xử lý các tác vụ nặng (gửi email, xử lý video, tạo báo cáo) ở chế độ nền, giúp ứng dụng web phản hồi người dùng nhanh hơn.
    + Tăng độ tin cậy: Nếu một dịch vụ xử lý bị lỗi, tác vụ vẫn nằm an toàn trong hàng đợi và có thể được xử lý lại sau khi dịch vụ phục hồi.
    + Kết nối các microservices: Là phương tiện giao tiếp hiệu quả giữa các dịch vụ nhỏ lẻ trong một kiến trúc microservices.