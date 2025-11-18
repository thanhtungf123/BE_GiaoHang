# Checklist Commit Driver Module

## NHÓM 1: Driver Onboarding & Authentication

### ✅ Đợt 1: Backend - Driver Onboarding API
- [ ] `BE_GiaoHang/models/driverApplication.model.js`
- [ ] `BE_GiaoHang/models/driver.model.js`
- [ ] `BE_GiaoHang/controllers/driverOnboardingController.js`
- [ ] `BE_GiaoHang/routes/driverOnboardingRoutes.js`
- [ ] `BE_GiaoHang/routes/index.js` (chỉ dòng import driverOnboardingRoutes)

**Command:**
```bash
git add BE_GiaoHang/models/driverApplication.model.js \
        BE_GiaoHang/models/driver.model.js \
        BE_GiaoHang/controllers/driverOnboardingController.js \
        BE_GiaoHang/routes/driverOnboardingRoutes.js \
        BE_GiaoHang/routes/index.js

git commit -m "feat(be/driver): add driver onboarding backend API"
```

---

### ✅ Đợt 2: Frontend - Driver Onboarding UI
- [ ] `GiaoHang/src/pages/driver/DriverLogin.jsx`
- [ ] `GiaoHang/src/pages/driver/components/DriverAuthCard.jsx`
- [ ] `GiaoHang/src/pages/driver/components/DriverSubmitButton.jsx`
- [ ] `GiaoHang/src/features/driver/api/endpoints.js`
- [ ] `GiaoHang/src/features/driver/api/driverService.js` (chỉ phần onboarding)
- [ ] `GiaoHang/src/App.jsx` (chỉ route /driver/login)

**Command:**
```bash
git add GiaoHang/src/pages/driver/DriverLogin.jsx \
        GiaoHang/src/pages/driver/components/DriverAuthCard.jsx \
        GiaoHang/src/pages/driver/components/DriverSubmitButton.jsx \
        GiaoHang/src/features/driver/api/endpoints.js \
        GiaoHang/src/features/driver/api/driverService.js \
        GiaoHang/src/App.jsx

git commit -m "feat(fe/driver): add driver onboarding frontend UI"
```

---

## NHÓM 2: Driver Profile & Settings

### ✅ Đợt 1: Backend - Driver Profile API
- [ ] `BE_GiaoHang/controllers/profileController.js` (chỉ các hàm driver)
- [ ] `BE_GiaoHang/routes/profileRoutes.js` (chỉ các route driver)

**Command:**
```bash
git add BE_GiaoHang/controllers/profileController.js \
        BE_GiaoHang/routes/profileRoutes.js

git commit -m "feat(be/driver): add driver profile management backend API"
```

---

### ✅ Đợt 2: Frontend - Driver Profile UI
- [ ] `GiaoHang/src/pages/driver/Profile.jsx`
- [ ] `GiaoHang/src/features/driver/api/driverService.js` (chỉ phần profile)
- [ ] `GiaoHang/src/features/driver/api/endpoints.js` (chỉ phần profile)
- [ ] `GiaoHang/src/App.jsx` (chỉ route /driver/profile)

**Command:**
```bash
git add GiaoHang/src/pages/driver/Profile.jsx \
        GiaoHang/src/features/driver/api/driverService.js \
        GiaoHang/src/features/driver/api/endpoints.js \
        GiaoHang/src/App.jsx

git commit -m "feat(fe/driver): add driver profile management frontend UI"
```

---

## NHÓM 3: Driver Orders & Revenue Management

### ✅ Đợt 1: Backend - Driver Orders & Revenue API
- [ ] `BE_GiaoHang/controllers/orderController.js` (chỉ các hàm driver)
- [ ] `BE_GiaoHang/controllers/driverRevenueController.js`
- [ ] `BE_GiaoHang/routes/orderRoutes.js` (chỉ các route driver)
- [ ] `BE_GiaoHang/routes/driverRevenueRoutes.js`
- [ ] `BE_GiaoHang/models/driverTransaction.model.js`
- [ ] `BE_GiaoHang/routes/index.js` (chỉ dòng import driverRevenueRoutes)

**Command:**
```bash
git add BE_GiaoHang/controllers/orderController.js \
        BE_GiaoHang/controllers/driverRevenueController.js \
        BE_GiaoHang/routes/orderRoutes.js \
        BE_GiaoHang/routes/driverRevenueRoutes.js \
        BE_GiaoHang/models/driverTransaction.model.js \
        BE_GiaoHang/routes/index.js

git commit -m "feat(be/driver): add driver orders and revenue backend API"
```

---

### ✅ Đợt 2: Frontend - Driver Orders & Revenue UI
- [ ] `GiaoHang/src/pages/driver/Orders.jsx`
- [ ] `GiaoHang/src/pages/driver/Home.jsx`
- [ ] `GiaoHang/src/pages/driver/Overview.jsx`
- [ ] `GiaoHang/src/pages/driver/Revenue.jsx`
- [ ] `GiaoHang/src/features/orders/api/orderService.js` (chỉ các hàm driver)
- [ ] `GiaoHang/src/features/revenue/api/revenueService.js`
- [ ] `GiaoHang/src/features/revenue/api/endpoints.js`
- [ ] `GiaoHang/src/App.jsx` (chỉ routes driver orders/revenue)

**Command:**
```bash
git add GiaoHang/src/pages/driver/Orders.jsx \
        GiaoHang/src/pages/driver/Home.jsx \
        GiaoHang/src/pages/driver/Overview.jsx \
        GiaoHang/src/pages/driver/Revenue.jsx \
        GiaoHang/src/features/orders/api/orderService.js \
        GiaoHang/src/features/revenue/api/revenueService.js \
        GiaoHang/src/features/revenue/api/endpoints.js \
        GiaoHang/src/App.jsx

git commit -m "feat(fe/driver): add driver orders and revenue frontend UI"
```

---

## NHÓM 4: Driver Withdrawal & Vehicle Management

### ✅ Đợt 1: Backend - Driver Withdrawal & Vehicle API
- [ ] `BE_GiaoHang/controllers/withdrawalController.js` (chỉ các hàm driver)
- [ ] `BE_GiaoHang/controllers/vehicleController.js` (chỉ các hàm driver)
- [ ] `BE_GiaoHang/routes/withdrawalRoutes.js` (chỉ các route driver)
- [ ] `BE_GiaoHang/routes/vehicleRoutes.js` (chỉ các route driver)
- [ ] `BE_GiaoHang/models/withdrawalRequest.model.js`

**Command:**
```bash
git add BE_GiaoHang/controllers/withdrawalController.js \
        BE_GiaoHang/controllers/vehicleController.js \
        BE_GiaoHang/routes/withdrawalRoutes.js \
        BE_GiaoHang/routes/vehicleRoutes.js \
        BE_GiaoHang/models/withdrawalRequest.model.js

git commit -m "feat(be/driver): add driver withdrawal and vehicle management backend API"
```

---

### ✅ Đợt 2: Frontend - Driver Withdrawal & Vehicle UI
- [ ] `GiaoHang/src/pages/driver/Withdrawal.jsx`
- [ ] `GiaoHang/src/pages/driver/VehicleManagement.jsx`
- [ ] `GiaoHang/src/features/withdrawal/api/withdrawalService.js`
- [ ] `GiaoHang/src/features/withdrawal/api/endpoints.js`
- [ ] `GiaoHang/src/features/vehicles/api/vehicleService.js` (chỉ các hàm driver)
- [ ] `GiaoHang/src/App.jsx` (chỉ routes driver withdrawal/vehicles)

**Command:**
```bash
git add GiaoHang/src/pages/driver/Withdrawal.jsx \
        GiaoHang/src/pages/driver/VehicleManagement.jsx \
        GiaoHang/src/features/withdrawal/api/withdrawalService.js \
        GiaoHang/src/features/withdrawal/api/endpoints.js \
        GiaoHang/src/features/vehicles/api/vehicleService.js \
        GiaoHang/src/App.jsx

git commit -m "feat(fe/driver): add driver withdrawal and vehicle management frontend UI"
```

---

## NHÓM 5: Driver Support (Optional)

### ✅ Đợt 1: Backend - Support Features (nếu có)
- [ ] (Các file backend liên quan)

**Command:**
```bash
# Tùy chỉnh theo file thực tế
git commit -m "feat(be/driver): add driver support features backend"
```

---

### ✅ Đợt 2: Frontend - Support Features UI
- [ ] `GiaoHang/src/pages/driver/Chat.jsx`
- [ ] `GiaoHang/src/pages/driver/Contact.jsx`
- [ ] `GiaoHang/src/App.jsx` (chỉ routes driver chat/contact)

**Command:**
```bash
git add GiaoHang/src/pages/driver/Chat.jsx \
        GiaoHang/src/pages/driver/Contact.jsx \
        GiaoHang/src/App.jsx

git commit -m "feat(fe/driver): add driver support features frontend UI"
```

---

## Lưu ý

1. **Kiểm tra trước khi commit:**
   - [ ] Code không có lỗi syntax
   - [ ] Đã test chức năng cơ bản
   - [ ] Không commit file .env, node_modules, dist, build

2. **Sau mỗi đợt commit:**
   - [ ] Push lên branch
   - [ ] Kiểm tra trên GitHub
   - [ ] Test lại chức năng

3. **Nếu file chung (như App.jsx, index.js):**
   - Chỉ commit phần liên quan đến driver
   - Hoặc commit toàn bộ file nếu đã hoàn thành tất cả các phần










