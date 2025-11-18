# PHÂN LOẠI FILE THEO ĐỢT - ORDER MANAGEMENT FEATURES

## Tổng quan

Tài liệu này phân loại các file liên quan đến 5 chức năng chính của Order Management thành từng đợt để push lên GitHub. Mỗi đợt bao gồm cả Frontend (FE) và Backend (BE) files.

---

## ĐỢT 1: ORDER CREATION SCREEN
**Chức năng:** Khách hàng tạo đơn hàng giao hàng

### Backend Files (BE_GiaoHang/)
```
controllers/orderController.js
  - createOrder() function (lines 47-409)
  
routes/orderRoutes.js
  - POST /orders route (line 19)
  
models/order.model.js
  - Order schema (toàn bộ file)
  
utils/pricing.js
  - calculatePrice() function (nếu có)
  
index.js
  - Socket.IO setup (lines 26-47) - phần liên quan đến emit order:available:new
```

### Frontend Files (GiaoHang/)
```
src/pages/user/OrderCreate.jsx
  - Toàn bộ component tạo đơn hàng
  
src/features/orders/api/orderService.js
  - createOrder() method (line 6)
  
src/features/orders/api/endpoints.js
  - ORDER_ENDPOINTS.createOrder
  
src/pages/user/components/OrderSummary.jsx
  - Component hiển thị tóm tắt đơn hàng (nếu dùng trong OrderCreate)
  
src/pages/user/components/OrderSummaryModal.jsx
  - Modal tóm tắt đơn hàng (nếu dùng trong OrderCreate)
```

### Dependencies cần có sẵn:
- Authentication middleware (middleware/auth.js)
- User model (models/user.model.js)
- Driver model (models/driver.model.js) - để tìm tài xế phù hợp
- Vehicle model (models/vehicle.model.js) - để kiểm tra xe phù hợp
- Socket.IO setup (index.js)

---

## ĐỢT 2: DRIVER AVAILABLE ORDERS SCREEN
**Chức năng:** Tài xế xem danh sách đơn hàng có sẵn để nhận

### Backend Files (BE_GiaoHang/)
```
controllers/orderController.js
  - getAvailableOrders() function
  
routes/orderRoutes.js
  - GET /orders/driver/available route (line 37)
  
models/order.model.js
  - Order schema (đã có từ đợt 1)
  
models/driver.model.js
  - Driver schema với currentLocation, serviceAreas
  
models/vehicle.model.js
  - Vehicle schema với vehicle type, maxWeightKg
```

### Frontend Files (GiaoHang/)
```
src/pages/driver/Orders.jsx
  - Tab "Đơn có sẵn" (available tab)
  - refetchAvailableOrders() function (lines 97-127)
  - Socket.IO listener cho order:available:new event (lines 248-332)
  
src/features/orders/api/orderService.js
  - getAvailableOrders() method (line 21)
  
src/features/orders/api/endpoints.js
  - ORDER_ENDPOINTS.driverAvailableOrders
```

### Dependencies cần có sẵn:
- Order Creation (đợt 1) - để có đơn hàng hiển thị
- Socket.IO setup (index.js)
- Authentication & Authorization

---

## ĐỢT 3: ORDER ACCEPTANCE FEATURE
**Chức năng:** Tài xế nhận đơn hàng từ danh sách có sẵn

### Backend Files (BE_GiaoHang/)
```
controllers/orderController.js
  - acceptOrderItem() function (lines 438-553)
  - updateOrderStatus() helper function (nếu có)
  
routes/orderRoutes.js
  - PUT /orders/:orderId/items/:itemId/accept route (line 40)
  
models/order.model.js
  - Order schema (đã có từ đợt 1)
  
models/driver.model.js
  - Driver schema (đã có từ đợt 2)
  
index.js
  - Socket.IO emit order:accepted event (trong acceptOrderItem)
```

### Frontend Files (GiaoHang/)
```
src/pages/driver/Orders.jsx
  - handleAcceptOrder() function
  - UI button "Nhận đơn" trong tab "Đơn có sẵn"
  
src/features/orders/api/orderService.js
  - acceptItem() method (line 24)
  
src/features/orders/api/endpoints.js
  - ORDER_ENDPOINTS.acceptItem
```

### Dependencies cần có sẵn:
- Order Creation (đợt 1)
- Driver Available Orders (đợt 2)
- Socket.IO setup

---

## ĐỢT 4: REAL-TIME ORDER TRACKING
**Chức năng:** Khách hàng theo dõi đơn hàng real-time qua Socket.IO

### Backend Files (BE_GiaoHang/)
```
index.js
  - Socket.IO server setup (lines 26-47)
  - customer:join event handler (lines 39-42)
  - Socket.IO emit events:
    * order:accepted (trong acceptOrderItem)
    * order:status:updated (trong updateOrderItemStatus)
    * order:location:updated (nếu có)
  
controllers/orderController.js
  - getOrderDetail() function - để lấy thông tin đơn hàng
  - Socket.IO emit trong acceptOrderItem() và updateOrderItemStatus()
  
routes/orderRoutes.js
  - GET /orders/:orderId route (line 46)
```

### Frontend Files (GiaoHang/)
```
src/pages/user/OrderTracking.jsx
  - Toàn bộ component tracking đơn hàng
  - Socket.IO client connection
  - Google Maps integration để hiển thị vị trí tài xế
  - Real-time status updates
  
src/pages/user/Orders.jsx
  - Component danh sách đơn hàng của khách hàng
  - Link đến OrderTracking
  
src/features/orders/api/orderService.js
  - getOrderDetail() method (line 12)
  
src/features/orders/api/endpoints.js
  - ORDER_ENDPOINTS.orderDetail
```

### Dependencies cần có sẵn:
- Order Creation (đợt 1)
- Order Acceptance (đợt 3)
- Socket.IO client library (socket.io-client)
- Google Maps API integration

---

## ĐỢT 5: ORDER STATUS UPDATE FLOW
**Chức năng:** Tài xế cập nhật trạng thái đơn hàng (Accepted → PickedUp → Delivering → Delivered)

### Backend Files (BE_GiaoHang/)
```
controllers/orderController.js
  - updateOrderItemStatus() function (lines 565-691)
  - updateOrderStatus() helper function (nếu có riêng)
  - Payment processing logic trong updateOrderItemStatus()
  
controllers/driverRevenueController.js
  - createDriverTransaction() function (nếu có)
  
models/driverTransaction.model.js
  - DriverTransaction schema
  
models/driver.model.js
  - Driver schema với incomeBalance field
  
routes/orderRoutes.js
  - PUT /orders/:orderId/items/:itemId/status route (line 43)
  
index.js
  - Socket.IO emit order:status:updated event
```

### Frontend Files (GiaoHang/)
```
src/pages/driver/Orders.jsx
  - handleUpdateStatus() function (lines 415-425)
  - handleConfirmPaid() function (lines 438-456)
  - UI buttons: "Đã lấy hàng", "Đang giao", "Đã giao hàng"
  - Payment confirmation modal
  - renderOrderSteps() function (lines 524-553)
  
src/features/orders/api/orderService.js
  - updateItemStatus() method (line 27)
  
src/features/orders/api/endpoints.js
  - ORDER_ENDPOINTS.updateItemStatus
```

### Dependencies cần có sẵn:
- Order Acceptance (đợt 3)
- Real-time Tracking (đợt 4) - để customer nhận updates
- Payment processing logic (nếu có)

---

## FILES CHUNG (Cần có trong tất cả các đợt)

### Backend (BE_GiaoHang/)
```
middleware/auth.js
  - authenticate middleware
  - authorize middleware
  - roles constants

config/db.js
  - MongoDB connection

config/config.js
  - Configuration settings

app.js
  - Express app setup
  - Middleware configuration
  - Route mounting
```

### Frontend (GiaoHang/)
```
src/authentication/api/axiosClient.js
  - Axios instance với interceptors

src/authentication/api/endpoints.js
  - API endpoints base URLs

src/features/orders/api/endpoints.js
  - ORDER_ENDPOINTS definitions
```

---

## THỨ TỰ PUSH LÊN GITHUB

### Commit 1: Order Creation Screen
```
git add [files đợt 1 - BE]
git add [files đợt 1 - FE]
git commit -m "feat: Add Order Creation Screen (BE + FE)"
git push origin [branch-name]
```

### Commit 2: Driver Available Orders Screen
```
git add [files đợt 2 - BE]
git add [files đợt 2 - FE]
git commit -m "feat: Add Driver Available Orders Screen (BE + FE)"
git push origin [branch-name]
```

### Commit 3: Order Acceptance Feature
```
git add [files đợt 3 - BE]
git add [files đợt 3 - FE]
git commit -m "feat: Add Order Acceptance Feature (BE + FE)"
git push origin [branch-name]
```

### Commit 4: Real-time Order Tracking
```
git add [files đợt 4 - BE]
git add [files đợt 4 - FE]
git commit -m "feat: Add Real-time Order Tracking (BE + FE)"
git push origin [branch-name]
```

### Commit 5: Order Status Update Flow
```
git add [files đợt 5 - BE]
git add [files đợt 5 - FE]
git commit -m "feat: Add Order Status Update Flow (BE + FE)"
git push origin [branch-name]
```

---

## LƯU Ý QUAN TRỌNG

1. **Thứ tự phụ thuộc:** Các đợt phải được push theo thứ tự vì có phụ thuộc:
   - Đợt 2 phụ thuộc Đợt 1
   - Đợt 3 phụ thuộc Đợt 1 và 2
   - Đợt 4 phụ thuộc Đợt 1 và 3
   - Đợt 5 phụ thuộc Đợt 3 và 4

2. **Files chung:** Các files chung (middleware, config, etc.) cần được push trước hoặc cùng với đợt đầu tiên.

3. **Socket.IO:** Socket.IO setup trong `index.js` cần được cập nhật dần theo từng đợt:
   - Đợt 1: Thêm emit `order:available:new`
   - Đợt 3: Thêm emit `order:accepted`
   - Đợt 4: Thêm `customer:join` handler
   - Đợt 5: Thêm emit `order:status:updated`

4. **Testing:** Sau mỗi đợt, nên test để đảm bảo chức năng hoạt động trước khi push đợt tiếp theo.

---

**Document Version:** 1.0  
**Created:** December 2024  
**Last Updated:** December 2024



