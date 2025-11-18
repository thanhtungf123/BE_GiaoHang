# ERD Text Summary - Hệ thống Giao Hàng

## Danh sách các Entity và thuộc tính chính

### 1. User (Người dùng)
- **PK**: _id
- **UK**: email, phone
- **Thuộc tính**: name, passwordHash, role (Customer|Driver|Admin), roles[], address, isEmailVerified, avatarUrl
- **Quan hệ**:
  - 1-1 với Driver (có thể là tài xế)
  - 1-N với Order (tạo nhiều đơn)
  - 1-N với Feedback, Violation, ChatMessage, DriverApplication, WithdrawalRequest, Otp

### 2. Driver (Tài xế)
- **PK**: _id
- **FK**: userId → User, vehicleId → Vehicle (optional)
- **Thuộc tính**: status (Pending|Active|Rejected|Blocked), rating, totalTrips, incomeBalance, isOnline, currentLocation (GeoJSON), bankAccountName, bankAccountNumber, bankName, bankCode
- **Quan hệ**:
  - N-1 với User (thuộc về một User)
  - 1-N với Vehicle (có nhiều xe)
  - 1-N với OrderItem (nhận nhiều item)
  - 1-N với Feedback, Violation, ChatMessage, DriverTransaction, WithdrawalRequest

### 3. Vehicle (Phương tiện)
- **PK**: _id
- **FK**: driverId → Driver
- **Thuộc tính**: type (TruckSmall|TruckMedium|TruckLarge|TruckBox|DumpTruck|PickupTruck|Trailer), licensePlate, maxWeightKg, pricePerKm, status (Active|Maintenance|Inactive), vehicleDocs[], photoUrl
- **Quan hệ**:
  - N-1 với Driver (thuộc về một Driver)

### 4. Order (Đơn hàng)
- **PK**: _id
- **FK**: customerId → User, paymentId → Payment
- **Thuộc tính**: pickupAddress, pickupLocation (GeoJSON), dropoffAddress, dropoffLocation (GeoJSON), items[] (OrderItem embedded), totalPrice, paymentStatus, paymentMethod, paymentBy (sender|receiver), status (Created|InProgress|Completed|Cancelled)
- **Quan hệ**:
  - N-1 với User (thuộc về một Customer)
  - 1-N với OrderItem (chứa nhiều item - embedded)
  - 1-1 với Payment
  - 1-N với Feedback, Violation, ChatMessage, Insurance, DriverTransaction

### 5. OrderItem (Item trong đơn) - Embedded trong Order
- **PK**: _id
- **FK**: driverId → Driver (optional)
- **Thuộc tính**: vehicleType, weightKg, distanceKm, loadingService, insurance, priceBreakdown{}, status (Created|Accepted|PickedUp|Delivering|Delivered|Cancelled), acceptedAt, pickedUpAt, deliveredAt, cancelledAt, itemPhotos[], offeredToDrivers[]
- **Quan hệ**:
  - Embedded trong Order (không có collection riêng)
  - N-1 với Driver (được nhận bởi một Driver)

### 6. Payment (Thanh toán)
- **PK**: _id
- **FK**: orderId → Order
- **Thuộc tính**: orderItemId, method (MoMo|VNPay|ZaloPay|COD), amount, status (Pending|Paid|Failed|Refunded), transactionCode
- **Quan hệ**:
  - N-1 với Order (thanh toán cho một Order)

### 7. Feedback (Đánh giá)
- **PK**: _id
- **FK**: orderId → Order, customerId → User, driverId → Driver
- **Thuộc tính**: orderItemId, overallRating (1-5), serviceRating, driverRating, vehicleRating, punctualityRating, comment, photos[], status (Pending|Approved|Rejected), adminResponse, driverResponse, isAnonymous, helpfulCount
- **Quan hệ**:
  - N-1 với Order, Driver, User (một Feedback đánh giá một Order, một Driver, từ một User)

### 8. Violation (Báo cáo vi phạm)
- **PK**: _id
- **FK**: reporterId → User, driverId → Driver, orderId → Order (optional), adminId → User (optional)
- **Thuộc tính**: orderItemId, violationType (LatePickup|LateDelivery|RudeBehavior|DamagedGoods|Overcharging|UnsafeDriving|NoShow|Other), description, photos[], status (Pending|Investigating|Resolved|Dismissed), adminNotes, penalty, warningCount, severity (Low|Medium|High|Critical), isAnonymous
- **Quan hệ**:
  - N-1 với Driver (bị báo cáo)
  - N-1 với User (người báo cáo)
  - N-1 với User (admin xử lý - optional)
  - N-1 với Order (liên quan - optional)

### 9. ChatMessage (Tin nhắn chat)
- **PK**: _id
- **FK**: orderId → Order, driverId → Driver, customerId → User, senderId → User
- **Thuộc tính**: orderItemId, senderRole (Customer|Driver|System), message, isSystem, readByCustomerAt, readByDriverAt
- **Quan hệ**:
  - N-1 với Order, Driver, User (customer), User (sender)

### 10. DriverApplication (Đơn đăng ký tài xế)
- **PK**: _id
- **FK**: userId → User
- **Thuộc tính**: status (Pending|Approved|Rejected), adminNote, emailVerifiedAt, docs{}, reviewedAt, submittedAt
- **Quan hệ**:
  - N-1 với User (của một User)

### 11. DriverTransaction (Giao dịch tài xế)
- **PK**: _id
- **FK**: driverId → Driver, orderId → Order (optional)
- **Thuộc tính**: orderItemId, amount, fee, netAmount, type (OrderEarning|Withdrawal|Bonus|Penalty), status (Pending|Completed|Failed|Cancelled), description, paymentMethod, transactionDate
- **Quan hệ**:
  - N-1 với Driver (của một Driver)
  - N-1 với Order (từ một đơn - optional)

### 12. WithdrawalRequest (Yêu cầu rút tiền)
- **PK**: _id
- **FK**: driverId → Driver, userId → User, processedBy → User (optional), transactionId → DriverTransaction (optional)
- **Thuộc tính**: requestedAmount, actualAmount, systemFee, status (Pending|Approved|Rejected|Completed|Cancelled), bankAccountName, bankAccountNumber, bankName, bankCode, confirmedAccountNumber, driverNote, rejectionReason, approvedAt, rejectedAt, completedAt
- **Quan hệ**:
  - N-1 với Driver, User (của một Driver/User)
  - N-1 với User (admin xử lý - optional)
  - N-1 với DriverTransaction (tạo giao dịch - optional)

### 13. Insurance (Bảo hiểm)
- **PK**: _id
- **FK**: orderId → Order
- **Thuộc tính**: provider, amount, status (Active|Claiming|Closed)
- **Quan hệ**:
  - N-1 với Order (bảo hiểm cho một Order)

### 14. Otp (Mã OTP)
- **PK**: _id
- **FK**: userId → User
- **Thuộc tính**: code, purpose (verify_email|reset_password), expiresAt, used
- **Quan hệ**:
  - N-1 với User (của một User)

### 15. Voucher (Mã khuyến mãi)
- **PK**: _id
- **UK**: code
- **Thuộc tính**: discountPercent, discountAmount, expiryDate, status (Active|Expired|Used)
- **Quan hệ**: Standalone (có thể áp dụng cho Order)

## Sơ đồ quan hệ chính

```
User (1) ────────< (1) Driver
  │                    │
  │                    ├───< (N) Vehicle
  │                    ├───< (N) OrderItem
  │                    ├───< (N) Feedback
  │                    ├───< (N) Violation
  │                    ├───< (N) ChatMessage
  │                    ├───< (N) DriverTransaction
  │                    └───< (N) WithdrawalRequest
  │
  ├───< (N) Order ────< (1) Payment
  │       │                │
  │       ├───< (N) OrderItem (embedded)
  │       ├───< (N) Feedback
  │       ├───< (N) Violation
  │       ├───< (N) ChatMessage
  │       ├───< (N) Insurance
  │       └───< (N) DriverTransaction
  │
  ├───< (N) Feedback
  ├───< (N) Violation
  ├───< (N) ChatMessage
  ├───< (N) DriverApplication
  ├───< (N) WithdrawalRequest
  └───< (N) Otp
```

## Ghi chú quan trọng

1. **OrderItem là embedded document** trong Order, không có collection riêng trong MongoDB
2. **GeoJSON Point** được sử dụng cho:
   - Order.pickupLocation, Order.dropoffLocation
   - Driver.currentLocation
3. **Quan hệ 1-1**: User ↔ Driver (một User có thể là một Driver)
4. **Quan hệ 1-N chính**:
   - User → Order (một User tạo nhiều Order)
   - Driver → Vehicle (một Driver có nhiều Vehicle)
   - Order → OrderItem (một Order chứa nhiều OrderItem)
   - Driver → OrderItem (một Driver nhận nhiều OrderItem)
5. **Indexes quan trọng**:
   - GeoJSON indexes trên pickupLocation, dropoffLocation, currentLocation (2dsphere)
   - Indexes trên các FK phổ biến (orderId, driverId, customerId, userId)
   - Indexes trên status fields để query nhanh


