# Kế hoạch Commit Code Driver Module

## Tổng quan
Chia code driver thành 4 nhóm chính, mỗi nhóm commit 2 đợt (mỗi đợt gồm FE + BE).

---

## NHÓM 1: Driver Onboarding & Authentication
**Mô tả**: Đăng ký trở thành tài xế, xác thực, và quản lý hồ sơ đăng ký

### Đợt 1: Backend - Driver Onboarding API
**Commit message**: `feat(driver): add driver onboarding backend API`

**Files Backend:**
```
BE_GiaoHang/models/driverApplication.model.js
BE_GiaoHang/models/driver.model.js
BE_GiaoHang/controllers/driverOnboardingController.js
BE_GiaoHang/routes/driverOnboardingRoutes.js
BE_GiaoHang/routes/index.js (chỉ phần import driverOnboardingRoutes)
```

**Mô tả**: 
- Model Driver và DriverApplication
- API nộp hồ sơ đăng ký tài xế
- API xem hồ sơ của mình
- API admin duyệt hồ sơ
- API lấy danh sách quận/huyện

---

### Đợt 2: Frontend - Driver Onboarding UI
**Commit message**: `feat(driver): add driver onboarding frontend UI`

**Files Frontend:**
```
GiaoHang/src/pages/driver/DriverLogin.jsx
GiaoHang/src/pages/driver/components/DriverAuthCard.jsx
GiaoHang/src/pages/driver/components/DriverSubmitButton.jsx
GiaoHang/src/features/driver/api/endpoints.js
GiaoHang/src/features/driver/api/driverService.js (chỉ phần apply, myApplication, adminList, adminReview, adminGetOne, getOne, getDistricts)
GiaoHang/src/App.jsx (chỉ phần route /driver/login)
```

**Mô tả**:
- Trang đăng nhập tài xế
- Component đăng ký trở thành tài xế
- Service API cho onboarding
- Routing cho driver login

---

## NHÓM 2: Driver Profile & Settings
**Mô tả**: Quản lý hồ sơ tài xế, cập nhật thông tin, avatar, ngân hàng, khu vực hoạt động

### Đợt 1: Backend - Driver Profile API
**Commit message**: `feat(driver): add driver profile management backend API`

**Files Backend:**
```
BE_GiaoHang/controllers/profileController.js (chỉ các hàm: getDriverProfile, updateServiceAreas, updateDriverBankInfo)
BE_GiaoHang/routes/profileRoutes.js (chỉ các route driver: /driver, /driver/service-areas, /driver/bank)
```

**Mô tả**:
- API lấy thông tin profile tài xế
- API cập nhật khu vực hoạt động
- API cập nhật thông tin ngân hàng

---

### Đợt 2: Frontend - Driver Profile UI
**Commit message**: `feat(driver): add driver profile management frontend UI`

**Files Frontend:**
```
GiaoHang/src/pages/driver/Profile.jsx
GiaoHang/src/features/driver/api/driverService.js (chỉ phần: getDriverInfo, updateProfile, uploadAvatar, updateBank, updateServiceAreas)
GiaoHang/src/features/driver/api/endpoints.js (chỉ phần: updateServiceAreas, info, updateProfile, uploadAvatar, updateBank)
GiaoHang/src/App.jsx (chỉ phần route /driver/profile)
GiaoHang/src/layouts/DriverDashboardLayout.jsx (nếu có link đến profile)
```

**Mô tả**:
- Trang quản lý hồ sơ tài xế
- Form cập nhật thông tin cá nhân
- Upload avatar
- Cập nhật thông tin ngân hàng
- Cập nhật khu vực hoạt động

---

## NHÓM 3: Driver Orders & Revenue Management
**Mô tả**: Quản lý đơn hàng, doanh thu, giao dịch của tài xế

### Đợt 1: Backend - Driver Orders & Revenue API
**Commit message**: `feat(driver): add driver orders and revenue backend API`

**Files Backend:**
```
BE_GiaoHang/controllers/orderController.js (chỉ các hàm driver: setDriverOnline, getDriverOrders, getAvailableOrders, acceptOrderItem, updateOrderItemStatus)
BE_GiaoHang/controllers/driverRevenueController.js
BE_GiaoHang/routes/orderRoutes.js (chỉ các route driver: /driver/online, /driver/my-orders, /driver/available, /:orderId/items/:itemId/accept, /:orderId/items/:itemId/status)
BE_GiaoHang/routes/driverRevenueRoutes.js
BE_GiaoHang/models/driverTransaction.model.js
BE_GiaoHang/routes/index.js (chỉ phần import driverRevenueRoutes)
```

**Mô tả**:
- API bật/tắt online
- API lấy danh sách đơn hàng của tài xế
- API lấy đơn hàng có sẵn
- API nhận đơn hàng
- API cập nhật trạng thái đơn hàng
- API thống kê doanh thu
- API lấy danh sách giao dịch
- Model DriverTransaction

---

### Đợt 2: Frontend - Driver Orders & Revenue UI
**Commit message**: `feat(driver): add driver orders and revenue frontend UI`

**Files Frontend:**
```
GiaoHang/src/pages/driver/Orders.jsx
GiaoHang/src/pages/driver/Home.jsx
GiaoHang/src/pages/driver/Overview.jsx
GiaoHang/src/pages/driver/Revenue.jsx
GiaoHang/src/features/orders/api/orderService.js (chỉ các hàm driver: getDriverOrders, getAvailableOrders, acceptItem, updateItemStatus, setDriverOnline)
GiaoHang/src/features/revenue/api/revenueService.js
GiaoHang/src/features/revenue/api/endpoints.js
GiaoHang/src/App.jsx (chỉ phần routes: /driver, /driver/orders, /driver/revenue)
```

**Mô tả**:
- Trang quản lý đơn hàng tài xế
- Trang tổng quan (Home, Overview)
- Trang doanh thu và thống kê
- Service API cho orders và revenue
- Socket.IO integration cho real-time orders

---

## NHÓM 4: Driver Withdrawal & Vehicle Management
**Mô tả**: Rút tiền và quản lý phương tiện

### Đợt 1: Backend - Driver Withdrawal & Vehicle API
**Commit message**: `feat(driver): add driver withdrawal and vehicle management backend API`

**Files Backend:**
```
BE_GiaoHang/controllers/withdrawalController.js (chỉ các hàm driver: createWithdrawalRequest, getMyWithdrawalHistory, getWithdrawalDetail)
BE_GiaoHang/controllers/vehicleController.js (chỉ các hàm driver: getMyVehicles, addVehicle, updateVehicle, deleteVehicle)
BE_GiaoHang/routes/withdrawalRoutes.js (chỉ các route driver: /driver/withdrawal/request, /driver/withdrawal/history, /driver/withdrawal/:id)
BE_GiaoHang/routes/vehicleRoutes.js (chỉ các route driver: /my-vehicles, POST /, PUT /:vehicleId, DELETE /:vehicleId)
BE_GiaoHang/models/withdrawalRequest.model.js
```

**Mô tả**:
- API tạo yêu cầu rút tiền
- API xem lịch sử rút tiền
- API xem chi tiết yêu cầu rút tiền
- API quản lý xe (thêm, sửa, xóa, xem danh sách)
- Model WithdrawalRequest

---

### Đợt 2: Frontend - Driver Withdrawal & Vehicle UI
**Commit message**: `feat(driver): add driver withdrawal and vehicle management frontend UI`

**Files Frontend:**
```
GiaoHang/src/pages/driver/Withdrawal.jsx
GiaoHang/src/pages/driver/VehicleManagement.jsx
GiaoHang/src/features/withdrawal/api/withdrawalService.js
GiaoHang/src/features/withdrawal/api/endpoints.js
GiaoHang/src/features/vehicles/api/vehicleService.js (chỉ các hàm driver: getMyVehicles, addVehicle, updateVehicle, deleteVehicle)
GiaoHang/src/App.jsx (chỉ phần routes: /driver/withdrawal, /driver/vehicles)
```

**Mô tả**:
- Trang rút tiền
- Form tạo yêu cầu rút tiền
- Lịch sử rút tiền
- Trang quản lý phương tiện
- CRUD xe (thêm, sửa, xóa, xem)

---

## NHÓM 5: Driver Support & Additional Features (Optional)
**Mô tả**: Các tính năng hỗ trợ bổ sung

### Đợt 1: Backend - Support Features (nếu có)
**Commit message**: `feat(driver): add driver support features backend`

**Files Backend:**
```
(Các file liên quan đến chat, feedback, violation nếu có phần driver)
```

---

### Đợt 2: Frontend - Support Features UI
**Commit message**: `feat(driver): add driver support features frontend UI`

**Files Frontend:**
```
GiaoHang/src/pages/driver/Chat.jsx
GiaoHang/src/pages/driver/Contact.jsx
GiaoHang/src/App.jsx (chỉ phần routes: /driver/chat, /driver/contact)
```

**Mô tả**:
- Trang chat
- Trang liên hệ

---

## Lưu ý khi commit

1. **Kiểm tra dependencies**: Đảm bảo các import và dependencies đã được cài đặt
2. **Test từng đợt**: Test FE và BE sau mỗi đợt commit
3. **Commit message**: Sử dụng format `feat(driver): ...` hoặc `feat(be/driver): ...` và `feat(fe/driver): ...`
4. **Không commit**: 
   - node_modules
   - .env files
   - Build files (dist, build)
   - Log files

## Thứ tự commit đề xuất

1. ✅ NHÓM 1 - Đợt 1: Backend Onboarding
2. ✅ NHÓM 1 - Đợt 2: Frontend Onboarding
3. ✅ NHÓM 2 - Đợt 1: Backend Profile
4. ✅ NHÓM 2 - Đợt 2: Frontend Profile
5. ✅ NHÓM 3 - Đợt 1: Backend Orders & Revenue
6. ✅ NHÓM 3 - Đợt 2: Frontend Orders & Revenue
7. ✅ NHÓM 4 - Đợt 1: Backend Withdrawal & Vehicle
8. ✅ NHÓM 4 - Đợt 2: Frontend Withdrawal & Vehicle
9. ⚠️ NHÓM 5 (Optional): Support Features










