# GIAO HÀNG NHANH
## DELIVERY MANAGEMENT SYSTEM
### Final Release Document
**Đà Nẵng, Tháng 12 2024**

---

## Table of Contents

1. [Record of Changes](#record-of-changes)
2. [Release Package & User Guides](#release-package--user-guides)
   - [Deliverable Package](#deliverable-package)
   - [Installation Guides](#installation-guides)
   - [User Guide (For End-Users)](#user-guide-for-end-users)
3. [User Manual](#user-manual)
   - [1. Authentication & Account Management](#1-authentication--account-management)
     - [1.1 Register](#11-register)
     - [1.2 Login](#12-login)
     - [1.3 Forgot Password & Reset Password](#13-forgot-password--reset-password)
     - [1.4 Change Password](#14-change-password)
     - [1.5 Edit Profile](#15-edit-profile)
     - [1.6 Upload Avatar](#16-upload-avatar)
     - [1.7 Update to Driver](#17-update-to-driver)
     - [1.8 Update Driver Location](#18-update-driver-location)
     - [1.9 Update Service Areas](#19-update-service-areas)
     - [1.10 Update Driver Bank Information](#110-update-driver-bank-information)
   - [2. Order Management](#2-order-management)
     - [2.0 Complete Booking Flow (Customer)](#20-complete-booking-flow-customer)
     - [2.1 Create Order](#21-create-order)
     - [2.2 View Orders](#22-view-orders)
     - [2.3 View Detailed Order](#23-view-detailed-order)
     - [2.4 Track Order (Real-time with Socket.IO)](#24-track-order-real-time-with-socketio)
     - [2.5 Cancel Order](#25-cancel-order)
     - [2.6 Update Order Insurance](#26-update-order-insurance)
   - [3. Driver Operations](#3-driver-operations)
     - [3.0 Complete Order Acceptance Flow (Driver)](#30-complete-order-acceptance-flow-driver)
     - [3.1 View Available Orders](#31-view-available-orders)
     - [3.2 Accept Order](#32-accept-order)
     - [3.3 Update Order Status](#33-update-order-status)
     - [3.4 Set Driver Status](#34-set-driver-status)
     - [3.5 View Delivery History](#35-view-delivery-history)
     - [3.6 Cancel Ride](#36-cancel-ride)
   - [4. Payment & Financial](#4-payment--financial)
     - [4.1 Payment](#41-payment)
     - [4.2 View Payment List](#42-view-payment-list)
   - [5. Feedback & Rating](#5-feedback--rating)
     - [5.1 Driver Rating](#51-driver-rating)
     - [5.2 View Reviews from Customer](#52-view-reviews-from-customer)
     - [5.3 Respond to Feedback (Driver)](#53-respond-to-feedback-driver)
     - [5.4 Delete Feedback](#54-delete-feedback)
     - [5.5 Update Feedback Status (Admin)](#55-update-feedback-status-admin)
   - [6. Vehicle Management](#6-vehicle-management)
     - [6.1 View Vehicle Type](#61-view-vehicle-type)
     - [6.2 Vehicle Management](#62-vehicle-management)
   - [7. Driver Onboarding](#7-driver-onboarding)
     - [7.1 Driver Onboarding](#71-driver-onboarding)
     - [7.2 View My Application](#72-view-my-application)
     - [7.3 View Application Detail](#73-view-application-detail)
     - [7.4 View Driver Registration List (Admin)](#74-view-driver-registration-list-admin)
     - [7.5 Approve/Reject Driver Application (Admin)](#75-approvereject-driver-application-admin)
     - [7.6 Get Districts List](#76-get-districts-list)
   - [8. Revenue & Withdrawal](#8-revenue--withdrawal)
     - [8.1 View Revenue Overview (Driver)](#81-view-revenue-overview-driver)
     - [8.2 View Revenue Statistics (Driver)](#82-view-revenue-statistics-driver)
     - [8.3 View Transactions History (Driver)](#83-view-transactions-history-driver)
     - [8.4 Withdrawal Request (Driver)](#84-withdrawal-request-driver)
     - [8.5 View Withdrawal History (Driver)](#85-view-withdrawal-history-driver)
     - [8.6 View Platform Revenue (Admin)](#86-view-platform-revenue-admin)
     - [8.7 Manage Withdrawals (Admin)](#87-manage-withdrawals-admin)
     - [8.8 View Withdrawal Statistics (Admin)](#88-view-withdrawal-statistics-admin)
   - [9. Violation & Reporting](#9-violation--reporting)
     - [9.1 Report Violation](#91-report-violation)
     - [9.2 View My Reports (Customer)](#92-view-my-reports-customer)
     - [9.3 View Report List (Admin)](#93-view-report-list-admin)
     - [9.4 Update Violation Status (Admin)](#94-update-violation-status-admin)
     - [9.5 View Violation Statistics (Admin)](#95-view-violation-statistics-admin)
   - [10. Admin Management](#10-admin-management)
     - [10.1 View Dashboard Statistics](#101-view-dashboard-statistics)
     - [10.2 View Account List](#102-view-account-list)
     - [10.3 View Account Detail](#103-view-account-detail)
     - [10.4 Admin Ban/Unban Account](#104-admin-banunban-account)
     - [10.5 View Driver List](#105-view-driver-list)
     - [10.6 View Driver Detail](#106-view-driver-detail)
     - [10.7 Payout to Driver](#107-payout-to-driver)
     - [10.8 Reset Driver Balance with Penalty](#108-reset-driver-balance-with-penalty)
     - [10.9 View Driver Revenue Statistics](#109-view-driver-revenue-statistics)
     - [10.10 View All Orders](#1010-view-all-orders)
   - [11. AI Chat Assistant](#11-ai-chat-assistant)
     - [11.1 Chat with AI Assistant](#111-chat-with-ai-assistant)
   - [12. File Upload & Management](#12-file-upload--management)
     - [12.1 Upload Single Image](#121-upload-single-image)
     - [12.2 Upload Multiple Images](#122-upload-multiple-images)
   - [13. Additional Features](#13-additional-features)
     - [13.1 Browse Vehicles](#131-browse-vehicles)
     - [13.2 Chat Page](#132-chat-page)
     - [13.3 Contact Page](#133-contact-page)
     - [13.4 Reports Page (Customer)](#134-reports-page-customer)

---

## Record of Changes

| Date | A*, M, D | In charge | Change Description |
|------|----------|-----------|-------------------|
| 01/10/2024 | A | Development Team | Add authentication system (login, register, OTP verification) |
| 05/10/2024 | A | Development Team | Add order creation and management system |
| 10/10/2024 | A | Development Team | Add driver onboarding and application system |
| 15/10/2024 | A | Development Team | Add real-time order tracking with Socket.IO |
| 20/10/2024 | A | Development Team | Add payment integration (VNPay) |
| 25/10/2024 | A | Development Team | Add feedback and rating system |
| 30/10/2024 | A | Development Team | Add violation reporting system |
| 05/11/2024 | A | Development Team | Add revenue management and withdrawal system |
| 10/11/2024 | A | Development Team | Add vehicle management for drivers |
| 15/11/2024 | M | Development Team | Update order status flow and driver assignment logic |
| 20/11/2024 | A | Development Team | Add AI chat assistant feature |
| 25/11/2024 | M | Development Team | Update payment flow and add multiple payment methods |
| 30/11/2024 | A | Development Team | Add admin dashboard and statistics |
| 05/12/2024 | M | Development Team | Update UI/UX and optimize performance |
| 10/12/2024 | A | Development Team | Add real-time chat between customer and driver |
| 15/12/2024 | M | Development Team | Update security and authentication middleware |

*A - Added, M - Modified, D - Deleted

---

## Release Package & User Guides

### Deliverable Package

| No. | Deliverable Item | Description |
|-----|------------------|-------------|
| 1 | Project Schedule/Tracking | Report_Project_Tracking |
| 2 | Project Backlog | Report_Project_Management_Plan |
| 3 | Source Codes | GiaoHang-Backend (Node.js, Express, MongoDB) <br> GiaoHang-Frontend (React, Vite) |
| 4 | Final Report Document | Report5_Final_Release_Document_GiaoHang |
| 5 | Test Cases Document | Report_Test_Documentation |

### Installation Guides

#### User Guide (For End-Users)

**System Requirements (Client):**

**Hardware:**
- A device (computer, tablet, or smartphone) with an internet connection
- Minimum 2GB RAM
- 100MB free storage space

**Software (Browsers):**
- The application works best on modern browsers such as:
  - Google Chrome (latest version)
  - Microsoft Edge (latest version)
  - Firefox (latest version)
  - Safari (latest version)

**Access URLs:**
- Login Page: `http://localhost:5173/auth/login`
- Registration Page: `http://localhost:5173/auth/register`
- Driver Login: `http://localhost:5173/driver/login`
- Admin Login: `http://localhost:5173/admin/login`

#### Installation Instruction

**Minimum Hardware Requirements**
- CPU: 2 Core
- RAM: 4GB
- Storage (Free space): 10GB

**Software Requirements**

| No. | Name | Version | Description |
|-----|------|---------|-------------|
| 1. | Visual Studio Code | Latest | Code editor |
| 2. | Git | Latest | Version control |
| 3. | Node.js | 18.x or higher | JavaScript runtime environment (to run Back-End & Front-End) |
| 4. | MongoDB | Latest | Database to store application data |
| 5. | Web browser | Chrome, Edge (latest ver) | Used for running and testing (development) |
| 6. | Postman | Latest | Tool for testing APIs (Back-End) |

**Backend Installation Steps:**

1. Navigate to the backend directory:
```bash
cd BE_GiaoHang
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env` file from `.env.example`:
```bash
cp .env.example .env
```

4. Configure environment variables in `.env`:
```env
PORT=8080
MONGODB_URI=mongodb://localhost:27017/giaohang
JWT_SECRET=your_jwt_secret_key_min_32_chars
JWT_REFRESH_SECRET=your_jwt_refresh_secret_key_min_32_chars
CLIENT_URL=http://localhost:5173
CORS_ORIGINS=http://localhost:5173
EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
GEMINI_API_KEY=your_gemini_api_key
```

5. Start MongoDB service

6. Run the backend server:
```bash
# Development mode
npm run dev

# Production mode
npm start
```

**Frontend Installation Steps:**

1. Navigate to the frontend directory:
```bash
cd GiaoHang
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env` file (if needed):
```env
VITE_API_URL=http://localhost:8080
```

4. Run the frontend development server:
```bash
npm run dev
```

5. Build for production:
```bash
npm run build
```

---

## User Manual

### User Manual Guide

Tài liệu này mô tả các chức năng của hệ thống GiaoHang được nhóm theo từng module chức năng, giúp người dùng dễ dàng tìm hiểu và sử dụng hệ thống.

---

## 1. Authentication & Account Management

### 1.1 Register

Chức năng đăng ký tài khoản cho phép khách hàng mới tạo tài khoản để sử dụng dịch vụ giao hàng.

**Bước 1:** Truy cập website và điều hướng đến màn hình đăng ký

**Bước 2:** Nhập tên, số điện thoại, địa chỉ email và mật khẩu

**Bước 3:** Click nút "Send code" để xác nhận email. Mã xác thực sẽ được gửi đến email bạn đã nhập

**Bước 4:** Hệ thống sẽ gửi mã OTP đến email đã đăng ký

**Bước 5:** Copy mã từ email và paste vào ô nhập, sau đó click "Verify"

**Bước 6:** Click "Register" để hoàn tất đăng ký

### 1.2 Login

This guide explains the functionalities available on the Login screen of the GiaoHang delivery system and provides step-by-step instructions for users to perform actions like logging in, resetting passwords, or navigating to registration.

**Functionality:**
- Submits the entered email/phone and password to authenticate the user
- If login is successful, the system automatically determines the user's role (Customer, Driver, or Admin)
- The system redirects the user to the appropriate landing screen based on their determined role
- Displays an error message if credentials are invalid or the account is deactivated

**Các bước:**
1. Đảm bảo bạn đã nhập email/số điện thoại và mật khẩu hợp lệ
2. Click nút "Sign in" màu xanh
3. Chờ thông báo xác nhận hoặc lỗi
4. Nếu đăng nhập thất bại, kiểm tra thông tin đăng nhập và thử lại

### 1.3 Forgot Password & Reset Password

Chức năng quên mật khẩu cho phép người dùng đặt lại mật khẩu khi quên mật khẩu. Quá trình này yêu cầu người dùng nhớ email của mình.

**Bước 1:** Truy cập website và điều hướng đến màn hình đăng nhập

**Bước 2:** Click "Forget password"

**Bước 3:** Nhập email để đặt lại mật khẩu

**Bước 4:** Click "Send reset link"

**Bước 5:** Hệ thống sẽ gửi link đặt lại mật khẩu, click "Reset Password"

**Bước 6:** Nhập mật khẩu mới và xác nhận mật khẩu

**Bước 7:** Click "Reset Password" để hoàn tất đặt lại mật khẩu

### 1.4 Change Password

Chức năng đổi mật khẩu cho phép người dùng (Customer và Driver) thay đổi mật khẩu khi đã đăng nhập vào hệ thống.

**Bước 1:** Đăng nhập vào hệ thống

**Bước 2:** Click vào avatar/ảnh đại diện của bạn ở góc trên bên phải navbar

**Bước 3:** Chọn "Đổi mật khẩu" từ dropdown menu

**Bước 4:** Nhập mật khẩu hiện tại

**Bước 5:** Nhập mật khẩu mới (tối thiểu 6 ký tự)

**Bước 6:** Xác nhận mật khẩu mới

**Bước 7:** Click "Đổi mật khẩu" để hoàn tất

**Lưu ý:** 
- Mật khẩu mới phải có ít nhất 6 ký tự
- Bạn phải nhập đúng mật khẩu hiện tại để có thể đổi mật khẩu
- Sau khi đổi mật khẩu thành công, bạn sẽ cần đăng nhập lại với mật khẩu mới

### 1.5 Edit Profile

Sau khi đăng nhập vào hệ thống, người dùng có thể cập nhật thông tin cá nhân trên màn hình profile.

**Bước 1:** Truy cập website và đăng nhập

**Bước 2:** Click nút "Profile" trong menu điều hướng

**Bước 3:** Nhập thông tin của bạn (tên, địa chỉ, số điện thoại)

**Bước 4:** Click "Save Information" để lưu thông tin

**Bước 5:** Click nút "Edit" nếu bạn muốn chỉnh sửa thông tin

**Bước 6:** Nhập thông tin bạn muốn cập nhật hoặc thay đổi

**Bước 7:** Click "Save information" để hoàn tất cập nhật thông tin cá nhân

### 1.6 Upload Avatar

Chức năng upload avatar cho phép người dùng cập nhật ảnh đại diện của mình.

**Bước 1:** Đăng nhập vào hệ thống

**Bước 2:** Truy cập trang Profile

**Bước 3:** Click vào ảnh đại diện hiện tại hoặc nút "Upload Avatar"

**Bước 4:** Chọn file ảnh từ máy tính (định dạng: JPG, PNG, tối đa 10MB)

**Bước 5:** Xem preview ảnh đã chọn

**Bước 6:** Click "Upload" để tải ảnh lên

**Bước 7:** Ảnh đại diện được cập nhật và hiển thị trên toàn hệ thống

**Lưu ý:**
- Ảnh sẽ được lưu trữ trên Cloudinary
- Kích thước tối đa: 10MB
- Định dạng hỗ trợ: JPG, PNG, GIF

### 1.7 Update to Driver

Chức năng nâng cấp lên tài xế cho phép người dùng đăng ký trở thành tài xế trong hệ thống.

**Bước 1:** Đăng ký tài khoản khách hàng trước

**Bước 2:** Từ màn hình chính, click "Become a Driver" hoặc "Apply as Driver"

**Bước 3:** Điền form đăng ký:
   - Thông tin cá nhân
   - Số CMND/CCCD
   - Số bằng lái xe
   - Thông tin xe
   - Khu vực phục vụ

**Bước 4:** Upload các tài liệu cần thiết:
   - CMND/CCCD (mặt trước và mặt sau)
   - Bằng lái xe
   - Giấy đăng ký xe
   - Tài liệu bảo hiểm

**Bước 5:** Gửi đơn đăng ký

**Bước 6:** Chờ admin phê duyệt:
   - Trạng thái đơn: "Pending"
   - Admin sẽ xem xét tài liệu
   - Bạn sẽ được thông báo khi được phê duyệt/từ chối

**Bước 7:** Sau khi được phê duyệt:
   - Vai trò tài khoản của bạn được cập nhật thành "Driver"
   - Bạn có thể bắt đầu nhận đơn hàng
   - Hoàn tất đăng ký xe của bạn

### 1.8 Update Driver Location

Chức năng cập nhật vị trí cho phép tài xế cập nhật vị trí hiện tại của mình để hệ thống có thể gợi ý đơn hàng phù hợp và tính toán khoảng cách chính xác.

**Bước 1:** Đăng nhập với tài khoản Driver

**Bước 2:** Truy cập trang Profile hoặc Driver Dashboard

**Bước 3:** Tìm phần "Update Location" hoặc "Cập nhật vị trí"

**Bước 4:** Cập nhật vị trí bằng một trong các cách:

   **Cách 1: Tự động lấy vị trí GPS**
   - Cho phép trình duyệt/ứng dụng truy cập vị trí của bạn (nếu chưa cho phép)
   - Click "Get Current Location" hoặc "Lấy vị trí hiện tại"
   - Hệ thống tự động lấy tọa độ GPS từ thiết bị
   - Xem preview vị trí trên bản đồ

   **Cách 2: Nhập thủ công tọa độ**
   - Nhập latitude (vĩ độ): -90 đến 90
   - Nhập longitude (kinh độ): -180 đến 180
   - Hoặc chọn vị trí trên bản đồ

**Bước 5:** Xem preview vị trí trên bản đồ (nếu có)

**Bước 6:** Click "Update Location" hoặc "Cập nhật vị trí" để lưu

**Bước 7:** Hệ thống xác nhận:
   - Vị trí đã được cập nhật thành công
   - Thời gian cập nhật (locationUpdatedAt)
   - Vị trí được lưu dưới dạng GeoJSON format

**API Endpoint:**
- **Method:** PUT
- **URL:** `/api/profile/driver/location`
- **Body:**
  ```json
  {
    "latitude": 16.0544,
    "longitude": 108.2022
  }
  ```

**Validation:**
- Latitude phải là số từ -90 đến 90
- Longitude phải là số từ -180 đến 180
- Cả hai trường đều bắt buộc

**Lưu ý quan trọng:**
- Vị trí được cập nhật tự động khi tài xế bật chế độ online
- Vị trí chính xác giúp hệ thống:
  - Gợi ý đơn hàng gần nhất (trong bán kính 2km)
  - Tính toán khoảng cách chính xác từ tài xế đến điểm đón
  - Sắp xếp đơn hàng theo khoảng cách gần nhất
- Vị trí nên được cập nhật định kỳ khi tài xế di chuyển
- Hệ thống sử dụng công thức Haversine để tính khoảng cách
- Vị trí được lưu trong database dưới dạng GeoJSON format: `[longitude, latitude]`

**Tự động cập nhật:**
- Khi bật chế độ online, hệ thống có thể tự động cập nhật vị trí
- Ứng dụng mobile có thể cập nhật vị trí theo thời gian thực khi di chuyển
- Vị trí được cập nhật mỗi khi tài xế mở ứng dụng hoặc nhận đơn mới

**Sử dụng trong hệ thống:**
- Tìm đơn hàng gần nhất: Hệ thống chỉ hiển thị đơn hàng trong bán kính 2km từ vị trí tài xế
- Kiểm tra khoảng cách khi nhận đơn: Tài xế chỉ có thể nhận đơn nếu khoảng cách từ vị trí hiện tại đến điểm đón ≤ 2km
- Sắp xếp đơn hàng: Đơn hàng gần nhất được hiển thị trước
- Tracking real-time: Khách hàng có thể theo dõi vị trí tài xế khi đang giao hàng

**Troubleshooting:**
- Nếu không lấy được vị trí GPS: Kiểm tra quyền truy cập vị trí của trình duyệt/ứng dụng
- Nếu vị trí không chính xác: Cập nhật lại vị trí hoặc nhập thủ công
- Nếu không thấy đơn hàng: Kiểm tra vị trí có được cập nhật chưa và có trong khu vực phục vụ không

### 1.9 Update Service Areas

Chức năng cập nhật khu vực phục vụ cho phép tài xế chọn các quận/huyện mà họ muốn nhận đơn hàng.

**Bước 1:** Đăng nhập với tài khoản Driver

**Bước 2:** Truy cập trang Profile

**Bước 3:** Tìm phần "Service Areas" hoặc "Khu vực phục vụ"

**Bước 4:** Chọn các quận/huyện từ danh sách:
   - Quận Cẩm Lệ
   - Quận Hải Châu
   - Quận Liên Chiểu
   - Quận Ngũ Hành Sơn
   - Quận Sơn Trà
   - Quận Thanh Khê
   - Huyện Hòa Vang
   - Huyện Hoàng Sa

**Bước 5:** Có thể chọn nhiều khu vực cùng lúc

**Bước 6:** Click "Save" để lưu cài đặt

**Bước 7:** Hệ thống sẽ chỉ hiển thị đơn hàng trong các khu vực đã chọn

**Lưu ý:**
- Chọn nhiều khu vực sẽ tăng cơ hội nhận đơn hàng
- Có thể thay đổi khu vực phục vụ bất cứ lúc nào

### 1.10 Update Driver Bank Information

Chức năng cập nhật thông tin ngân hàng cho phép tài xế cập nhật thông tin tài khoản ngân hàng để nhận tiền rút.

**Bước 1:** Đăng nhập với tài khoản Driver

**Bước 2:** Truy cập trang Profile

**Bước 3:** Tìm phần "Bank Information" hoặc "Thông tin ngân hàng"

**Bước 4:** Nhập thông tin ngân hàng:
   - Tên ngân hàng
   - Số tài khoản
   - Tên chủ tài khoản
   - Mã ngân hàng (nếu có)

**Bước 5:** Xác nhận lại số tài khoản

**Bước 6:** Click "Save" để lưu thông tin

**Bước 7:** Thông tin ngân hàng được lưu và sử dụng cho các yêu cầu rút tiền

**Lưu ý:**
- Thông tin ngân hàng phải chính xác để nhận tiền
- Có thể cập nhật thông tin bất cứ lúc nào
- Thông tin được mã hóa và bảo mật

---

## 2. Order Management

### 2.0 Complete Booking Flow (Customer)

Luồng đặt xe hoàn chỉnh mô tả toàn bộ quy trình từ khi khách hàng bắt đầu đặt xe đến khi đơn hàng được tạo và gửi đến tài xế.

#### Tổng Quan Luồng

```
KHÁCH HÀNG ĐĂNG NHẬP
       ↓
CHỌN "ĐẶT XE" / "BOOK VEHICLE"
       ↓
NHẬP THÔNG TIN ĐỊA CHỈ
  - Địa chỉ lấy hàng (pickupAddress)
  - Địa chỉ giao hàng (dropoffAddress)
  - Tọa độ GPS (pickupLocation, dropoffLocation)
       ↓
THÊM ITEMS (HÀNG HÓA)
  - Trọng lượng (weightKg)
  - Khoảng cách (distanceKm) - tự động tính
  - Dịch vụ bổ sung (bốc xếp, bảo hiểm)
       ↓
HỆ THỐNG TÍNH GIÁ
  - Tính giá theo khoảng cách
  - Tính phí bốc xếp (nếu có)
  - Tính phí bảo hiểm (nếu có)
  - Hiển thị tổng giá
       ↓
CHỌN PHƯƠNG THỨC THANH TOÁN
  - Cash (Tiền mặt)
  - Banking (Chuyển khoản)
  - Wallet (Ví điện tử)
       ↓
CHỌN NGƯỜI THANH TOÁN
  - Sender (Người gửi trả)
  - Receiver (Người nhận trả)
       ↓
XEM TỔNG KẾT ĐƠN HÀNG
  - Kiểm tra lại thông tin
  - Xem chi tiết giá
       ↓
XÁC NHẬN VÀ TẠO ĐƠN
       ↓
HỆ THỐNG XỬ LÝ
  - Tạo đơn hàng (Order.status = "Created")
  - Tạo items (Item.status = "Created", driverId = null)
  - Tính toán giá cả
  - Tìm tài xế phù hợp (trong bán kính 2km)
  - Phát tín hiệu Socket.IO cho tài xế
       ↓
THÔNG BÁO THÀNH CÔNG
  - Đơn hàng đã được tạo
  - Đang tìm tài xế
  - Có thể theo dõi đơn hàng
       ↓
CHỜ TÀI XẾ NHẬN ĐƠN
  - Đơn hiển thị trong "Đơn có sẵn" của tài xế
  - Khách hàng có thể theo dõi trạng thái
```

#### Chi Tiết Từng Bước

**Bước 1: Truy cập trang đặt xe**
- Đăng nhập với tài khoản Customer
- Từ Dashboard, click "Book Vehicle" hoặc "Đặt xe"
- Hoặc từ menu điều hướng, chọn "Create Order"

**Bước 2: Nhập địa chỉ lấy hàng**
- Nhập địa chỉ lấy hàng vào ô tìm kiếm
- Chọn từ danh sách gợi ý (Google Maps API)
- Xác nhận vị trí trên bản đồ
- Hệ thống tự động lấy tọa độ GPS (latitude, longitude)

**Bước 3: Nhập địa chỉ giao hàng**
- Nhập địa chỉ giao hàng vào ô tìm kiếm
- Chọn từ danh sách gợi ý
- Xác nhận vị trí trên bản đồ
- Hệ thống tự động tính khoảng cách (distanceKm)

**Bước 4: Thêm hàng hóa (Items)**
- Click "Add Item" hoặc "Thêm hàng"
- Nhập thông tin cho mỗi item:
  - **Trọng lượng (weightKg)**: Số kg hàng hóa
  - **Khoảng cách (distanceKm)**: Tự động tính từ địa chỉ
  - **Dịch vụ bốc xếp (loadingService)**: Có/không (phí bổ sung)
  - **Bảo hiểm (insurance)**: Có/không (phí bổ sung)
  - **Ảnh hàng hóa (itemPhotos)**: Upload ảnh (tùy chọn)
- Có thể thêm nhiều items trong một đơn hàng
- Mỗi item có thể yêu cầu loại xe khác nhau

**Bước 5: Hệ thống tính giá tự động**
- Tính giá cơ bản: `pricePerKm × distanceKm`
- Tính phí bốc xếp: Nếu có `loadingService` (+50,000 VND)
- Tính phí bảo hiểm: Nếu có `insurance` (tùy giá trị hàng)
- Tổng giá mỗi item = Giá cơ bản + Phí bốc xếp + Phí bảo hiểm
- Tổng giá đơn hàng = Tổng tất cả items

**Bước 6: Chọn phương thức thanh toán**
- **Cash (Tiền mặt)**: Thanh toán khi nhận hàng
- **Banking (Chuyển khoản)**: Thanh toán qua VNPay
- **Wallet (Ví điện tử)**: Thanh toán qua ví (nếu có)

**Bước 7: Chọn người thanh toán**
- **Sender (Người gửi trả)**: Thanh toán khi tài xế lấy hàng (PickedUp)
- **Receiver (Người nhận trả)**: Thanh toán khi tài xế giao hàng (Delivered)

**Bước 8: Xem tổng kết đơn hàng**
- Xem lại tất cả thông tin:
  - Địa chỉ lấy/giao hàng
  - Danh sách items và giá
  - Tổng giá đơn hàng
  - Phương thức thanh toán
  - Ghi chú (nếu có)

**Bước 9: Xác nhận và tạo đơn**
- Click "Create Order" hoặc "Tạo đơn hàng"
- Hệ thống xử lý:
  - Validate dữ liệu
  - Tính toán giá cả
  - Tạo đơn hàng trong database
  - Tìm tài xế phù hợp (trong bán kính 2km, có xe phù hợp)
  - Phát tín hiệu Socket.IO cho tài xế

**Bước 10: Kết quả**
- Đơn hàng được tạo thành công
- Order status: "Created"
- Item status: "Created"
- Item driverId: null (chưa có tài xế)
- Đơn hiển thị trong "My Orders" với trạng thái "Đang tìm tài xế"
- Tài xế nhận được thông báo đơn mới qua Socket.IO

#### Lưu ý Quan Trọng

- **Tìm tài xế phù hợp**: Hệ thống chỉ gửi đơn cho tài xế:
  - Trong bán kính 2km từ điểm đón
  - Có xe phù hợp với trọng tải yêu cầu
  - Đang online (isOnline = true)
  - Trong khu vực phục vụ phù hợp

- **Tính giá tự động**: Giá được tính dựa trên:
  - Khoảng cách thực tế (từ Google Maps)
  - Trọng lượng hàng hóa
  - Dịch vụ bổ sung (bốc xếp, bảo hiểm)

- **Socket.IO Real-time**: Tài xế nhận thông báo ngay khi đơn được tạo

- **Nhiều items**: Một đơn có thể có nhiều items, mỗi item có thể được tài xế khác nhận

---

### 2.1 Create Order

### Create Order (For Customer)

The order creation feature allows customers to create delivery orders by selecting pickup and dropoff locations, vehicle type, and additional services.

**Steps to Create an Order:**

1. After logging in, click the "Create Order" button from the home screen

2. Enter pickup address:
   - Type or search for the pickup location
   - Select from the dropdown suggestions
   - Confirm the location on the map

3. Enter dropoff address:
   - Type or search for the dropoff location
   - Select from the dropdown suggestions
   - Confirm the location on the map

4. Add order items:
   - Click "Add Item"
   - Enter weight (kg)
   - Select vehicle type (if needed)
   - Choose additional services:
     - Loading service (bốc xếp)
     - Insurance (bảo hiểm)
   - The system will calculate the distance and price automatically

5. Review order summary:
   - Check all information
   - Review total price
   - Verify pickup and dropoff addresses

6. Proceed to payment:
   - Click "Proceed to Payment"
   - Choose payment method (VNPay, MoMo, COD)
   - Complete payment process

7. Order created successfully:
   - You will receive a confirmation
   - Order will appear in "My Orders"
   - System will notify available drivers

### View Orders (For Customer)

The view orders function allows customers to see all their orders with different statuses.

**Steps to View Orders:**

1. From the home screen, click "Orders" in the navigation menu

2. View orders by status:
   - **Pending**: Orders waiting for driver acceptance
   - **In Progress**: Orders being delivered
   - **Completed**: Finished orders
   - **Cancelled**: Cancelled orders

3. Click on an order to view details:
   - Order information
   - Driver information (if assigned)
   - Order items
   - Payment status
   - Timeline

### 2.4 Track Order (Real-time with Socket.IO)

The order tracking feature allows customers to track their orders in real-time using Socket.IO technology.

**Steps to Track Order:**

1. From "My Orders", click on an order that is "In Progress"

2. View real-time tracking:
   - Driver's current location (updated in real-time via Socket.IO)
   - Order status updates (automatically synchronized)
   - Estimated delivery time
   - Route visualization on map

3. Real-time features:
   - Location updates every few seconds
   - Automatic status synchronization
   - Push notifications for status changes
   - Live chat with driver

4. Contact driver:
   - Click "Chat" to message the driver (real-time chat)
   - Click "Call" to contact the driver (if available)

**Technical Details:**
- Uses Socket.IO for real-time communication
- Customer joins room: `customer:{customerId}`
- Driver joins room: `driver:{driverId}`
- Automatic reconnection on network issues

### Cancel Order (For Customer)

The cancel order function allows customers to cancel orders that haven't been accepted by a driver yet.

**Steps to Cancel Order:**

1. From "My Orders", find an order with status "Pending"

2. Click "Cancel Order" button

3. Enter cancellation reason (optional)

4. Confirm cancellation

5. If payment was made, refund will be processed according to payment method

### 2.6 Update Order Insurance

Chức năng cập nhật bảo hiểm cho đơn hàng cho phép khách hàng thêm hoặc cập nhật bảo hiểm cho đơn hàng đã tạo.

**Bước 1:** Truy cập "My Orders"

**Bước 2:** Chọn đơn hàng cần cập nhật bảo hiểm (trạng thái "Pending")

**Bước 3:** Click "Update Insurance" hoặc "Cập nhật bảo hiểm"

**Bước 4:** Chọn mức bảo hiểm:
   - Không có bảo hiểm
   - Bảo hiểm cơ bản
   - Bảo hiểm nâng cao

**Bước 5:** Xem giá cập nhật (nếu có thay đổi)

**Bước 6:** Click "Update" để xác nhận

**Bước 7:** Hệ thống cập nhật giá đơn hàng và thông tin bảo hiểm

**Lưu ý:**
- Chỉ có thể cập nhật khi đơn hàng ở trạng thái "Pending"
- Giá đơn hàng sẽ được tính lại nếu thay đổi bảo hiểm
- Bảo hiểm giúp bảo vệ hàng hóa trong quá trình vận chuyển

### 5.1 Driver Rating

Chức năng đánh giá tài xế cho phép khách hàng đánh giá và nhận xét về dịch vụ sau khi đơn hàng đã được giao thành công. Hệ thống hỗ trợ đánh giá chi tiết với nhiều tiêu chí khác nhau.

**Điều kiện để đánh giá:**
- Đơn hàng phải ở trạng thái "Completed" (Đã hoàn thành)
- Item trong đơn hàng phải ở trạng thái "Delivered" (Đã giao hàng)
- Khách hàng chỉ có thể đánh giá đơn hàng của chính mình
- Mỗi đơn hàng/item chỉ có thể đánh giá một lần

**Các bước đánh giá tài xế:**

**Bước 1:** Truy cập "My Orders" hoặc "Đơn hàng của tôi"

**Bước 2:** Tìm đơn hàng đã hoàn thành (trạng thái "Completed")

**Bước 3:** Click vào đơn hàng để xem chi tiết

**Bước 4:** Click nút "Đánh giá dịch vụ" hoặc "Rate & Review" trên item đã được giao

**Bước 5:** Điền form đánh giá:

   a. **Đánh giá tổng quan (Bắt buộc):**
      - Chọn số sao từ 1-5 sao
      - 1 sao: Rất tệ
      - 2 sao: Tệ
      - 3 sao: Bình thường
      - 4 sao: Tốt
      - 5 sao: Rất tốt

   b. **Đánh giá chi tiết (Tùy chọn):**
      - **Chất lượng dịch vụ (Service Rating):** Đánh giá chất lượng dịch vụ vận chuyển
      - **Thái độ tài xế (Driver Rating):** Đánh giá thái độ, cách giao tiếp của tài xế
      - **Tình trạng xe (Vehicle Rating):** Đánh giá tình trạng phương tiện vận chuyển
      - Xe có sạch sẽ không?
      - Xe có đảm bảo an toàn không?
      - Xe có phù hợp với hàng hóa không?
      - **Đúng giờ (Punctuality Rating):** Đánh giá việc tài xế có đến đúng giờ không
      - Tài xế có đến đúng giờ hẹn không?
      - Thời gian giao hàng có đúng như cam kết không?

   c. **Nhận xét chi tiết (Tùy chọn):**
      - Viết nhận xét về trải nghiệm (tối đa 1000 ký tự)
      - Chia sẻ những điểm tốt hoặc cần cải thiện
      - Có thể mô tả chi tiết về dịch vụ

   d. **Upload ảnh minh họa (Tùy chọn):**
      - Upload tối đa 5 ảnh
      - Mỗi ảnh không quá 2MB
      - Chỉ chấp nhận file ảnh (jpg, png, jpeg)
      - Ảnh có thể là: ảnh hàng hóa, ảnh xe, ảnh tài xế, v.v.

   e. **Đánh giá ẩn danh (Tùy chọn):**
      - Có thể chọn đánh giá ẩn danh
      - Tên khách hàng sẽ không hiển thị công khai

**Bước 6:** Xem lại thông tin đánh giá

**Bước 7:** Click "Gửi đánh giá" hoặc "Submit Feedback"

**Bước 8:** Hệ thống xử lý và lưu đánh giá:
   - Đánh giá được lưu vào hệ thống
   - Rating trung bình của tài xế được cập nhật tự động
   - Đánh giá hiển thị công khai (trừ khi chọn ẩn danh)
   - Tài xế nhận được thông báo về đánh giá mới

**Lưu ý quan trọng:**
- Chỉ có thể đánh giá đơn hàng đã hoàn thành
- Mỗi đơn hàng/item chỉ có thể đánh giá một lần
- Đánh giá tổng quan là bắt buộc, các đánh giá chi tiết là tùy chọn
- Đánh giá sẽ ảnh hưởng đến rating trung bình của tài xế
- Có thể xóa đánh giá của mình nếu muốn (xem mục 5.4)
- Tài xế có thể phản hồi lại đánh giá (xem mục 5.3)
- Admin có thể quản lý và ẩn các đánh giá không phù hợp (xem mục 5.5)

**API Endpoint:**
- **POST** `/api/feedback` - Tạo đánh giá mới
  - Body: `{ orderId, orderItemId, overallRating, serviceRating, driverRating, vehicleRating, punctualityRating, comment, photos[], isAnonymous }`
  - Response: `{ success: true, data: feedback }`

**Validation Rules:**
- `overallRating`: Bắt buộc, số từ 1-5
- `serviceRating`: Tùy chọn, số từ 1-5
- `driverRating`: Tùy chọn, số từ 1-5
- `vehicleRating`: Tùy chọn, số từ 1-5
- `punctualityRating`: Tùy chọn, số từ 1-5
- `comment`: Tùy chọn, tối đa 1000 ký tự
- `photos`: Tùy chọn, mảng URL ảnh, tối đa 5 ảnh
- `isAnonymous`: Tùy chọn, boolean

**Tác động của đánh giá:**
- Rating trung bình của tài xế được tính lại tự động
- Đánh giá hiển thị công khai trên profile tài xế
- Khách hàng khác có thể xem đánh giá khi chọn tài xế
- Đánh giá tốt giúp tài xế nhận được nhiều đơn hàng hơn

### 5.2 View Reviews from Customer

Chức năng xem đánh giá cho phép khách hàng xem các đánh giá và nhận xét từ khách hàng khác về tài xế và dịch vụ. Điều này giúp khách hàng có thông tin để đưa ra quyết định khi chọn tài xế.

**Các cách xem đánh giá:**

**Cách 1: Xem đánh giá trên trang đơn hàng**

**Bước 1:** Truy cập "My Orders" hoặc "Đơn hàng của tôi"

**Bước 2:** Click vào một đơn hàng để xem chi tiết

**Bước 3:** Scroll xuống phần "Đánh giá dịch vụ" (nếu có)

**Bước 4:** Xem danh sách đánh giá:
   - Đánh giá từ khách hàng khác về tài xế của đơn hàng này
   - Rating trung bình và thống kê đánh giá
   - Nhận xét chi tiết và ảnh minh họa (nếu có)
   - Phản hồi từ tài xế (nếu có)

**Cách 2: Xem đánh giá của tài xế cụ thể**

**Bước 1:** Truy cập trang thông tin tài xế hoặc profile tài xế

**Bước 2:** Xem phần "Đánh giá" hoặc "Reviews"

**Bước 3:** Xem thống kê đánh giá:
   - Rating trung bình tổng thể
   - Số lượng đánh giá
   - Phân bố đánh giá theo mức sao (1-5 sao)
   - Rating trung bình theo từng tiêu chí:
     * Chất lượng dịch vụ
     * Thái độ tài xế
     * Tình trạng xe
     * Đúng giờ

**Bước 4:** Xem danh sách đánh giá chi tiết:
   - Tên khách hàng (hoặc "Khách hàng ẩn danh")
   - Rating tổng thể và rating chi tiết
   - Nhận xét của khách hàng
   - Ảnh minh họa (nếu có)
   - Ngày đánh giá
   - Phản hồi từ tài xế (nếu có)

**Cách 3: Xem đánh giá của mình**

**Bước 1:** Truy cập "Feedback" hoặc "Đánh giá của tôi"

**Bước 2:** Xem danh sách tất cả đánh giá bạn đã tạo

**Bước 3:** Xem chi tiết từng đánh giá:
   - Thông tin đơn hàng liên quan
   - Đánh giá bạn đã đưa ra
   - Trạng thái đánh giá (Approved, Pending, Rejected)
   - Phản hồi từ tài xế (nếu có)

**Thông tin hiển thị trong đánh giá:**

1. **Thông tin khách hàng:**
   - Tên khách hàng (hoặc "Khách hàng ẩn danh")
   - Avatar (nếu không ẩn danh)

2. **Rating:**
   - Rating tổng thể (1-5 sao)
   - Rating chi tiết (nếu có):
     * Chất lượng dịch vụ
     * Thái độ tài xế
     * Tình trạng xe
     * Đúng giờ

3. **Nội dung đánh giá:**
   - Nhận xét chi tiết
   - Ảnh minh họa (nếu có)

4. **Thông tin bổ sung:**
   - Ngày đánh giá
   - Trạng thái đánh giá
   - Phản hồi từ tài xế (nếu có)
   - Số lượt đánh giá hữu ích

5. **Thống kê tổng hợp:**
   - Rating trung bình tổng thể
   - Số lượng đánh giá
   - Phân bố đánh giá theo mức sao
   - Rating trung bình theo từng tiêu chí

**Lọc và tìm kiếm đánh giá:**

- Lọc theo rating (1-5 sao)
- Lọc theo tiêu chí (dịch vụ, tài xế, xe, đúng giờ)
- Sắp xếp theo: Mới nhất, Cũ nhất, Rating cao nhất, Rating thấp nhất
- Phân trang để xem nhiều đánh giá hơn

**API Endpoints:**
- **GET** `/api/feedback/driver/:driverId` - Lấy đánh giá của tài xế
  - Query params: `page`, `limit`, `rating`
  - Response: `{ success: true, data: feedbacks[], meta: { page, limit, total, totalPages } }`

- **GET** `/api/feedback/customer` - Lấy đánh giá của khách hàng hiện tại
  - Query params: `page`, `limit`
  - Response: `{ success: true, data: feedbacks[], meta: { page, limit, total, totalPages } }`

- **GET** `/api/feedback/order/:orderId` - Lấy đánh giá của đơn hàng
  - Response: `{ success: true, data: feedbacks[] }`

**Lưu ý:**
- Chỉ hiển thị các đánh giá có trạng thái "Approved"
- Đánh giá ẩn danh sẽ không hiển thị tên khách hàng
- Có thể xem đánh giá mà không cần đăng nhập (đối với đánh giá công khai)
- Đánh giá được sắp xếp mặc định theo thời gian mới nhất

### 5.3 Respond to Feedback (Driver)

Chức năng phản hồi đánh giá cho phép tài xế phản hồi lại các đánh giá từ khách hàng.

**Bước 1:** Đăng nhập với tài khoản Driver

**Bước 2:** Truy cập trang "Feedback" hoặc "Đánh giá"

**Bước 3:** Xem danh sách đánh giá từ khách hàng

**Bước 4:** Chọn đánh giá muốn phản hồi

**Bước 5:** Click "Respond" hoặc "Phản hồi"

**Bước 6:** Nhập nội dung phản hồi

**Bước 7:** Click "Submit Response" để gửi phản hồi

**Lưu ý:**
- Phản hồi sẽ hiển thị công khai dưới đánh giá của khách hàng
- Phản hồi một cách lịch sự và chuyên nghiệp
- Có thể phản hồi nhiều lần nếu cần

### 5.4 Delete Feedback

Chức năng xóa đánh giá cho phép khách hàng xóa đánh giá của mình.

**Bước 1:** Truy cập "My Orders" hoặc "Feedback"

**Bước 2:** Tìm đánh giá muốn xóa

**Bước 3:** Click "Delete" hoặc "Xóa"

**Bước 4:** Xác nhận xóa đánh giá

**Bước 5:** Đánh giá được xóa khỏi hệ thống

**Lưu ý:**
- Chỉ có thể xóa đánh giá của chính mình
- Sau khi xóa, không thể khôi phục lại
- Xóa đánh giá không ảnh hưởng đến đơn hàng

### 5.5 Update Feedback Status (Admin)

Chức năng cập nhật trạng thái đánh giá cho phép admin quản lý các đánh giá trong hệ thống.

**Bước 1:** Đăng nhập với tài khoản Admin

**Bước 2:** Truy cập "Feedback Management" hoặc "Quản lý đánh giá"

**Bước 3:** Xem danh sách tất cả đánh giá

**Bước 4:** Chọn đánh giá cần cập nhật trạng thái

**Bước 5:** Chọn trạng thái mới:
   - Active: Hiển thị công khai
   - Hidden: Ẩn khỏi công khai
   - Deleted: Đã xóa

**Bước 6:** Click "Update Status" để lưu

**Bước 7:** Trạng thái đánh giá được cập nhật

**Lưu ý:**
- Admin có thể ẩn các đánh giá không phù hợp
- Có thể khôi phục đánh giá đã ẩn
- Thay đổi trạng thái được ghi nhận trong lịch sử

### Report Violation (For Customer)

The violation reporting function allows customers to report driver violations or misconduct.

**Steps to Report Violation:**

1. From "My Orders", find the relevant order

2. Click "Report Violation" button

3. Select violation type:
   - Late delivery
   - Damaged goods
   - Rude behavior
   - Other

4. Provide details and evidence (photos if available)

5. Submit the report

6. Admin will review and take appropriate action

### 9.2 View My Reports (Customer)

Chức năng xem báo cáo của tôi cho phép khách hàng xem tất cả các báo cáo vi phạm mà họ đã gửi.

**Bước 1:** Truy cập trang "Reports" hoặc "Báo cáo"

**Bước 2:** Xem danh sách báo cáo của bạn:
   - Báo cáo đang chờ xử lý (Pending)
   - Báo cáo đã được xem xét (Reviewed)
   - Báo cáo đã được giải quyết (Resolved)

**Bước 3:** Xem chi tiết mỗi báo cáo:
   - Loại vi phạm
   - Mô tả chi tiết
   - Bằng chứng (ảnh)
   - Trạng thái xử lý
   - Phản hồi từ admin (nếu có)

**Bước 4:** Theo dõi tiến trình xử lý

### 9.3 View Report List (Admin)

Chức năng xem danh sách báo cáo cho phép admin xem tất cả các báo cáo vi phạm trong hệ thống.

**Bước 1:** Đăng nhập với tài khoản Admin

**Bước 2:** Truy cập "Reports" hoặc "Báo cáo vi phạm"

**Bước 3:** Xem danh sách tất cả báo cáo:
   - Báo cáo đang chờ (Pending)
   - Báo cáo đã xem xét (Reviewed)
   - Báo cáo đã giải quyết (Resolved)

**Bước 4:** Lọc báo cáo:
   - Theo trạng thái
   - Theo loại vi phạm
   - Theo tài xế
   - Theo khoảng thời gian

**Bước 5:** Xem chi tiết báo cáo:
   - Thông tin khách hàng
   - Thông tin tài xế
   - Mô tả vi phạm
   - Bằng chứng (ảnh)
   - Lịch sử xử lý

### 9.4 Update Violation Status (Admin)

Chức năng cập nhật trạng thái vi phạm cho phép admin xử lý các báo cáo vi phạm.

**Bước 1:** Truy cập "Reports"

**Bước 2:** Chọn báo cáo cần xử lý

**Bước 3:** Xem xét đầy đủ thông tin:
   - Thông tin khách hàng
   - Thông tin tài xế
   - Mô tả vi phạm
   - Bằng chứng

**Bước 4:** Cập nhật trạng thái:
   - **Pending:** Đang chờ xử lý
   - **Reviewed:** Đã xem xét
   - **Resolved:** Đã giải quyết

**Bước 5:** Thực hiện hành động (nếu cần):
   - Cảnh báo tài xế
   - Tạm ngưng tài khoản tài xế
   - Cấm tài khoản tài xế
   - Đánh dấu đã giải quyết

**Bước 6:** Nhập ghi chú (nếu có)

**Bước 7:** Click "Update Status" để lưu

### 9.5 View Violation Statistics (Admin)

Chức năng xem thống kê vi phạm cho phép admin xem thống kê về các báo cáo vi phạm.

**Bước 1:** Truy cập "Reports"

**Bước 2:** Click "Statistics" hoặc "Thống kê"

**Bước 3:** Xem thống kê tổng quan:
   - Tổng số báo cáo
   - Số báo cáo theo trạng thái
   - Số báo cáo theo loại vi phạm
   - Số báo cáo theo tài xế

**Bước 4:** Xem biểu đồ:
   - Biểu đồ theo thời gian
   - Biểu đồ theo loại vi phạm
   - Biểu đồ theo trạng thái

**Bước 5:** Xuất báo cáo (nếu cần)

---

## 3. Driver Operations

### 3.0 Complete Order Acceptance Flow (Driver)

Luồng nhận đơn hoàn chỉnh mô tả toàn bộ quy trình từ khi tài xế xem đơn có sẵn đến khi hoàn thành giao hàng và nhận thu nhập.

#### Tổng Quan Luồng

```
TÀI XẾ ĐĂNG NHẬP
       ↓
BẬT CHẾ ĐỘ ONLINE
  - Set isOnline = true
  - Cập nhật vị trí hiện tại
       ↓
XEM ĐƠN CÓ SẴN
  - Hệ thống hiển thị đơn trong bán kính 2km
  - Lọc theo khu vực phục vụ
  - Lọc theo loại xe phù hợp
  - Lọc theo trọng tải
       ↓
NHẬN THÔNG BÁO ĐƠN MỚI (Socket.IO)
  - Real-time notification
  - Xem thông tin đơn ngay lập tức
       ↓
XEM CHI TIẾT ĐƠN HÀNG
  - Địa chỉ lấy/giao hàng
  - Trọng lượng, khoảng cách
  - Giá đơn hàng
  - Thông tin khách hàng
       ↓
KIỂM TRA ĐIỀU KIỆN
  - Khoảng cách từ vị trí hiện tại ≤ 2km
  - Có xe phù hợp với trọng tải
  - Trong khu vực phục vụ
       ↓
NHẬN ĐƠN HÀNG
  - Click "Accept Order"
  - Item.driverId = driver._id
  - Item.status = "Accepted"
  - Order.status = "InProgress"
  - Khách hàng được thông báo
       ↓
ĐI ĐẾN ĐIỂM LẤY HÀNG
  - Xem bản đồ đường đi
  - Liên hệ khách hàng (nếu cần)
       ↓
LẤY HÀNG (PickedUp)
  - Click "Picked Up"
  - Item.status = "PickedUp"
  - Ghi nhận pickedUpAt
  - Nếu paymentBy = "sender": Thanh toán ngay
       ↓
BẮT ĐẦU GIAO HÀNG (Delivering)
  - Click "Start Delivery"
  - Item.status = "Delivering"
  - Khách hàng có thể track vị trí
  - Cập nhật vị trí real-time
       ↓
ĐẾN ĐIỂM GIAO HÀNG
  - Xem bản đồ đường đi
  - Liên hệ người nhận
       ↓
GIAO HÀNG THÀNH CÔNG (Delivered)
  - Click "Delivered"
  - Item.status = "Delivered"
  - Ghi nhận deliveredAt
  - Upload ảnh xác nhận (tùy chọn)
  - Nếu paymentBy = "receiver": Thanh toán ngay
       ↓
HỆ THỐNG XỬ LÝ THANH TOÁN
  - Tính phí hoa hồng (20%)
  - Tạo DriverTransaction
  - Cập nhật driver.incomeBalance
  - Tăng driver.totalTrips
  - Order.status = "Completed" (nếu tất cả items đã delivered)
       ↓
NHẬN THU NHẬP
  - Thu nhập được cộng vào số dư
  - Có thể xem trong Revenue
  - Có thể rút tiền sau
       ↓
KHÁCH HÀNG ĐÁNH GIÁ
  - Khách hàng có thể đánh giá và phản hồi
  - Tài xế có thể xem và phản hồi lại
```

#### Chi Tiết Từng Bước

**Bước 1: Đăng nhập và bật chế độ online**
- Đăng nhập với tài khoản Driver
- Truy cập Driver Dashboard
- Bật chế độ online (isOnline = true)
- Cập nhật vị trí hiện tại (nếu chưa có)
- Hệ thống bắt đầu gửi đơn hàng đến bạn

**Bước 2: Xem đơn có sẵn**
- Truy cập trang "Orders" → Tab "Available" hoặc "Đơn có sẵn"
- Hệ thống hiển thị đơn hàng:
  - Trong bán kính 2km từ vị trí hiện tại
  - Trong khu vực phục vụ của bạn
  - Phù hợp với loại xe và trọng tải của bạn
  - Chưa có tài xế nhận (status = "Created", driverId = null)

**Bước 3: Nhận thông báo đơn mới (Real-time)**
- Khi khách hàng tạo đơn mới, bạn nhận được thông báo ngay lập tức qua Socket.IO
- Thông báo hiển thị:
  - Mã đơn hàng
  - Địa chỉ lấy/giao hàng
  - Tổng giá
  - Số lượng items
- Click vào thông báo để xem chi tiết

**Bước 4: Xem chi tiết đơn hàng**
- Click vào đơn hàng để xem đầy đủ thông tin:
  - **Địa chỉ lấy hàng**: Địa chỉ và tọa độ GPS
  - **Địa chỉ giao hàng**: Địa chỉ và tọa độ GPS
  - **Khoảng cách**: Từ điểm lấy đến điểm giao
  - **Items**: Danh sách hàng hóa với trọng lượng
  - **Tổng giá**: Giá đơn hàng
  - **Thông tin khách hàng**: Tên, số điện thoại
  - **Ghi chú**: Yêu cầu đặc biệt (nếu có)

**Bước 5: Kiểm tra điều kiện nhận đơn**
- Hệ thống tự động kiểm tra:
  - **Khoảng cách**: Từ vị trí hiện tại đến điểm đón ≤ 2km
  - **Xe phù hợp**: Có xe có thể chở được trọng lượng yêu cầu
  - **Khu vực**: Đơn hàng trong khu vực phục vụ của bạn
- Nếu không đủ điều kiện, đơn sẽ không hiển thị hoặc không thể nhận

**Bước 6: Nhận đơn hàng**
- Click "Accept Order" hoặc "Nhận đơn"
- Hệ thống xử lý:
  - Gán `item.driverId = driver._id`
  - Cập nhật `item.status = "Accepted"`
  - Ghi nhận `item.acceptedAt = new Date()`
  - Cập nhật `order.status = "InProgress"`
  - Gửi thông báo cho khách hàng
- Đơn chuyển sang tab "Accepted" hoặc "Đơn đã nhận"

**Bước 7: Đi đến điểm lấy hàng**
- Xem bản đồ đường đi từ vị trí hiện tại đến điểm lấy hàng
- Sử dụng Google Maps để điều hướng
- Liên hệ khách hàng nếu cần (số điện thoại hiển thị)
- Cập nhật vị trí khi di chuyển (tự động hoặc thủ công)

**Bước 8: Lấy hàng (PickedUp)**
- Khi đã đến điểm lấy hàng và lấy hàng thành công:
- Click "Picked Up" hoặc "Đã lấy hàng"
- Hệ thống cập nhật:
  - `item.status = "PickedUp"`
  - `item.pickedUpAt = new Date()`
- **Nếu paymentBy = "sender"**: Hệ thống xử lý thanh toán ngay:
  - Tạo DriverTransaction
  - Cập nhật số dư tài xế (80% sau khi trừ phí 20%)
  - Tăng totalTrips

**Bước 9: Bắt đầu giao hàng (Delivering)**
- Sau khi lấy hàng, bắt đầu đi đến điểm giao hàng
- Click "Start Delivery" hoặc "Bắt đầu giao hàng"
- Hệ thống cập nhật:
  - `item.status = "Delivering"`
  - Khách hàng có thể track vị trí real-time
- Cập nhật vị trí định kỳ để khách hàng theo dõi

**Bước 10: Đến điểm giao hàng**
- Xem bản đồ đường đi đến điểm giao hàng
- Sử dụng Google Maps để điều hướng
- Liên hệ người nhận (nếu cần)
- Cập nhật vị trí khi di chuyển

**Bước 11: Giao hàng thành công (Delivered)**
- Khi đã giao hàng thành công:
- Click "Delivered" hoặc "Đã giao hàng"
- Upload ảnh xác nhận giao hàng (tùy chọn)
- Hệ thống cập nhật:
  - `item.status = "Delivered"`
  - `item.deliveredAt = new Date()`
- **Nếu paymentBy = "receiver"**: Hệ thống xử lý thanh toán ngay:
  - Tạo DriverTransaction
  - Cập nhật số dư tài xế (80% sau khi trừ phí 20%)
  - Tăng totalTrips
- Nếu tất cả items trong đơn đều Delivered:
  - `order.status = "Completed"`
  - Khách hàng có thể đánh giá

**Bước 12: Nhận thu nhập**
- Thu nhập được tự động cộng vào số dư:
  - Số tiền thực nhận = 80% tổng giá đơn
  - Phí hệ thống = 20% tổng giá đơn
- Xem trong trang "Revenue":
  - Tổng thu nhập
  - Lịch sử giao dịch
  - Chi tiết từng đơn hàng
- Có thể rút tiền sau khi đủ số dư

**Bước 13: Khách hàng đánh giá (Sau khi hoàn thành)**
- Khách hàng có thể đánh giá và phản hồi
- Tài xế có thể xem đánh giá và phản hồi lại
- Đánh giá ảnh hưởng đến rating của tài xế

#### Lưu ý Quan Trọng

- **Điều kiện nhận đơn**: 
  - Khoảng cách từ vị trí hiện tại đến điểm đón ≤ 2km
  - Có xe phù hợp với trọng tải yêu cầu
  - Đang online (isOnline = true)
  - Trong khu vực phục vụ

- **Thanh toán tự động**:
  - Nếu paymentBy = "sender": Thanh toán khi PickedUp
  - Nếu paymentBy = "receiver": Thanh toán khi Delivered
  - Phí hệ thống = 20%, Thu nhập = 80%

- **Cập nhật vị trí**: 
  - Cập nhật định kỳ khi di chuyển
  - Giúp khách hàng track real-time
  - Giúp hệ thống gợi ý đơn hàng chính xác

- **Socket.IO Real-time**:
  - Nhận thông báo đơn mới ngay lập tức
  - Cập nhật trạng thái real-time cho khách hàng
  - Đồng bộ dữ liệu tự động

- **Nhiều items trong một đơn**:
  - Mỗi item có thể được tài xế khác nhận
  - Tài xế chỉ nhận một item tại một thời điểm
  - Order status = "Completed" khi tất cả items đều Delivered

---

### View Available Orders (For Driver)

The view available orders function allows drivers to see orders that are available for acceptance.

**Steps to View Available Orders:**

1. Log in with driver account

2. From the home screen, click "Available Orders" or "Đơn có sẵn"

3. View orders:
   - Orders are filtered by your service areas
   - Orders show pickup and dropoff locations
   - Orders display distance and estimated price

4. Filter orders:
   - By vehicle type
   - By distance
   - By price range

5. Click on an order to view details:
   - Full pickup and dropoff addresses
   - Order items and weight
   - Total price
   - Customer information

### Accept Order (For Driver)

The accept order function allows drivers to accept available orders.

**Steps to Accept Order:**

1. From "Available Orders", select an order you want to accept

2. Review order details:
   - Check pickup and dropoff locations
   - Verify vehicle type matches your vehicle
   - Review total price

3. Click "Accept Order" button

4. Order status changes:
   - Order moves to "My Orders" → "Accepted"
   - Customer is notified
   - You can now proceed to pickup

### Update Order Status (For Driver)

The update order status function allows drivers to update the progress of order delivery.

**Steps to Update Order Status:**

1. From "My Orders", select an order

2. Update status in sequence:

   **a. Picked Up:**
   - Click "Picked Up" when you have collected the items
   - System records pickup time
   - Order status changes to "Picked Up"

   **b. Delivering:**
   - Click "Start Delivery" when you begin delivery
   - Order status changes to "Delivering"
   - Customer can track your location

   **c. Delivered:**
   - Click "Delivered" when you complete delivery
   - Upload delivery confirmation photo (optional)
   - Order status changes to "Delivered"
   - Revenue is credited to your account

3. If you need to cancel:
   - Click "Cancel Order"
   - Enter cancellation reason
   - Order status changes to "Cancelled"

### 3.4 Set Driver Status

Chức năng đặt trạng thái tài xế cho phép tài xế bật/tắt chế độ online để nhận đơn hàng.

**Bước 1:** Đăng nhập với tài khoản Driver

**Bước 2:** Truy cập Driver Dashboard hoặc trang "Orders"

**Bước 3:** Tìm nút "Go Online" hoặc "Bật chế độ online"

**Bước 4:** Bật chế độ online:
   - Click "Go Online" hoặc toggle switch
   - Trạng thái chuyển sang "Online"
   - Hệ thống bắt đầu gửi đơn hàng có sẵn đến bạn
   - Vị trí của bạn được cập nhật để hệ thống gợi ý đơn gần nhất

**Bước 5:** Tắt chế độ online:
   - Click "Go Offline" hoặc toggle switch
   - Trạng thái chuyển sang "Offline"
   - Hệ thống ngừng gửi đơn hàng mới đến bạn
   - Các đơn đã nhận vẫn có thể tiếp tục xử lý

**Lưu ý:**
- Chỉ khi online, bạn mới nhận được đơn hàng mới
- Các đơn đã nhận có thể tiếp tục xử lý khi offline
- Vị trí được cập nhật tự động khi online

### 3.5 View Delivery History

Chức năng xem lịch sử giao hàng cho phép tài xế xem tất cả các đơn hàng đã hoàn thành (Delivered).

**Bước 1:** Đăng nhập với tài khoản Driver

**Bước 2:** Truy cập trang "Orders" hoặc "Đơn hàng"

**Bước 3:** Chọn tab "Completed" hoặc "Đã hoàn thành"

**Bước 4:** Xem danh sách đơn hàng đã hoàn thành:
   - Tất cả đơn hàng có trạng thái "Delivered"
   - Sắp xếp theo thời gian (mới nhất trước)
   - Hiển thị thông tin cơ bản:
     - Mã đơn hàng
     - Địa chỉ lấy hàng
     - Địa chỉ giao hàng
     - Ngày giao hàng
     - Tổng tiền
     - Thu nhập (sau khi trừ phí 20%)

**Bước 5:** Lọc đơn hàng:
   - Theo khoảng thời gian (hôm nay, tuần này, tháng này)
   - Theo loại xe
   - Theo giá trị đơn hàng

**Bước 6:** Xem chi tiết đơn hàng:
   - Click vào đơn hàng để xem chi tiết
   - Thông tin khách hàng
   - Thông tin đơn hàng đầy đủ
   - Lịch sử trạng thái (timeline)
   - Thông tin thanh toán
   - Thu nhập từ đơn hàng này
   - Đánh giá từ khách hàng (nếu có)

**Bước 7:** Xem thống kê:
   - Tổng số đơn đã hoàn thành
   - Tổng thu nhập từ các đơn đã hoàn thành
   - Thu nhập trung bình mỗi đơn
   - Số đơn theo thời gian

**Lưu ý:**
- Chỉ hiển thị các đơn hàng đã được giao thành công (status = "Delivered")
- Thu nhập đã được cộng vào số dư tài khoản
- Có thể xem lại đánh giá từ khách hàng
- Lịch sử được lưu vĩnh viễn

**Tính năng bổ sung:**
- Xuất báo cáo lịch sử giao hàng (nếu có)
- Tìm kiếm đơn hàng theo mã đơn
- Xem bản đồ đường đi đã thực hiện (nếu có)

### 3.6 Cancel Ride

Chức năng hủy đơn hàng cho phép tài xế hủy đơn hàng đã nhận trong các trường hợp cần thiết.

**Bước 1:** Đăng nhập với tài khoản Driver

**Bước 2:** Truy cập trang "Orders" hoặc "Đơn hàng"

**Bước 3:** Chọn đơn hàng cần hủy:
   - Đơn hàng ở trạng thái "Accepted" (Đã nhận)
   - Đơn hàng ở trạng thái "PickedUp" (Đã lấy hàng)
   - Đơn hàng ở trạng thái "Delivering" (Đang giao hàng)
   - **Lưu ý:** Không thể hủy đơn đã hoàn thành (Delivered)

**Bước 4:** Click "Cancel Order" hoặc "Hủy đơn"

**Bước 5:** Nhập lý do hủy đơn:
   - Lý do bắt buộc (ví dụ: Xe hỏng, Không thể đến địa chỉ, Khách hàng không liên lạc được, v.v.)
   - Mô tả chi tiết (nếu có)

**Bước 6:** Xác nhận hủy đơn:
   - Xem lại thông tin đơn hàng
   - Xác nhận lý do hủy
   - Click "Confirm Cancel" hoặc "Xác nhận hủy"

**Bước 7:** Hệ thống xử lý:
   - Trạng thái item chuyển sang "Cancelled"
   - Ghi nhận thời gian hủy (cancelledAt)
   - Lưu lý do hủy (cancelReason)
   - Khách hàng được thông báo về việc hủy đơn
   - Đơn hàng chuyển sang tab "Cancelled" (Đã hủy)

**Bước 8:** Kiểm tra kết quả:
   - Đơn hàng xuất hiện trong tab "Cancelled"
   - Khách hàng có thể tạo đơn mới hoặc tìm tài xế khác
   - Nếu tất cả items trong đơn đều bị hủy → Order status = "Cancelled"

**Lưu ý quan trọng:**
- Chỉ có thể hủy đơn trước khi hoàn thành (trước status "Delivered")
- Hủy đơn có thể ảnh hưởng đến đánh giá của khách hàng
- Nên liên hệ với khách hàng trước khi hủy (nếu có thể)
- Hủy đơn quá nhiều có thể ảnh hưởng đến tài khoản tài xế
- Đơn đã hủy không thể khôi phục lại

**Trường hợp đặc biệt:**
- Nếu đã lấy hàng (PickedUp) nhưng cần hủy: Phải trả hàng cho khách hàng
- Nếu đang giao hàng (Delivering) nhưng cần hủy: Phải liên hệ với khách hàng ngay
- Nếu đã thanh toán: Hệ thống sẽ xử lý hoàn tiền cho khách hàng (nếu có)

**Xem lịch sử đơn đã hủy:**
- Truy cập tab "Cancelled" hoặc "Đã hủy"
- Xem tất cả đơn đã hủy với lý do hủy
- Có thể lọc theo khoảng thời gian

---

## 4. Payment & Financial

### 8.1 View Revenue Overview (Driver)

Chức năng xem tổng quan doanh thu cho phép tài xế xem tổng quan về thu nhập của mình.

**Bước 1:** Đăng nhập với tài khoản Driver

**Bước 2:** Truy cập trang "Revenue" hoặc "Doanh thu"

**Bước 3:** Xem tổng quan doanh thu:
   - Tổng thu nhập
   - Số dư hiện tại
   - Thu nhập hôm nay
   - Thu nhập tuần này
   - Thu nhập tháng này

**Bước 4:** Xem thống kê:
   - Tổng số đơn đã hoàn thành
   - Thu nhập trung bình mỗi đơn
   - Phí hệ thống đã trừ (20%)

### 8.2 View Revenue Statistics (Driver)

Chức năng xem thống kê doanh thu cho phép tài xế xem thống kê chi tiết theo thời gian.

**Bước 1:** Truy cập trang "Revenue"

**Bước 2:** Click "Statistics" hoặc "Thống kê"

**Bước 3:** Chọn khoảng thời gian:
   - Hôm nay
   - Tuần này
   - Tháng này
   - Tùy chỉnh (chọn ngày bắt đầu và kết thúc)

**Bước 4:** Xem biểu đồ doanh thu:
   - Biểu đồ theo ngày
   - Biểu đồ theo tuần
   - Biểu đồ theo tháng

**Bước 5:** Xem chi tiết:
   - Số đơn hoàn thành
   - Tổng thu nhập
   - Phí hệ thống
   - Thu nhập thực tế

### 8.3 View Transactions History (Driver)

Chức năng xem lịch sử giao dịch cho phép tài xế xem chi tiết tất cả các giao dịch.

**Bước 1:** Truy cập trang "Revenue"

**Bước 2:** Click "Transactions" hoặc "Lịch sử giao dịch"

**Bước 3:** Xem danh sách giao dịch:
   - Giao dịch từ đơn hàng (Order)
   - Giao dịch rút tiền (Withdrawal)
   - Giao dịch chi trả (Payout)

**Bước 4:** Xem chi tiết mỗi giao dịch:
   - Loại giao dịch
   - Số tiền
   - Thời gian
   - Trạng thái
   - Mô tả

**Bước 5:** Lọc giao dịch:
   - Theo loại giao dịch
   - Theo khoảng thời gian
   - Theo trạng thái

### 8.4 Withdrawal Request (Driver)

Chức năng yêu cầu rút tiền cho phép tài xế yêu cầu rút tiền từ số dư của mình.

**Bước 1:** Truy cập trang "Revenue" hoặc "Withdrawal"

**Bước 2:** Click "Request Withdrawal" hoặc "Yêu cầu rút tiền"

**Bước 3:** Nhập số tiền muốn rút:
   - Số tiền tối thiểu: 100,000 VND
   - Số tiền tối đa: Số dư hiện tại

**Bước 4:** Nhập thông tin tài khoản ngân hàng:
   - Tên ngân hàng
   - Số tài khoản
   - Tên chủ tài khoản
   - Xác nhận lại số tài khoản

**Bước 5:** Xem thông tin chi tiết:
   - Số tiền yêu cầu
   - Số tiền thực nhận (80%)
   - Phí hệ thống (20%)
   - Thông tin ngân hàng

**Bước 6:** Nhập ghi chú (nếu có)

**Bước 7:** Click "Submit Request" để gửi yêu cầu

**Bước 8:** Chờ admin phê duyệt:
   - Trạng thái: "Pending"
   - Admin sẽ xem xét và xử lý
   - Bạn sẽ được thông báo khi được xử lý

**Lưu ý:**
- Số tiền thực nhận = 80% số tiền yêu cầu
- Phí hệ thống = 20% số tiền yêu cầu
- Phải xác nhận lại số tài khoản để đảm bảo chính xác

### 8.5 View Withdrawal History (Driver)

Chức năng xem lịch sử rút tiền cho phép tài xế xem tất cả các yêu cầu rút tiền của mình.

**Bước 1:** Truy cập trang "Withdrawal" hoặc "Rút tiền"

**Bước 2:** Click "History" hoặc "Lịch sử"

**Bước 3:** Xem danh sách yêu cầu rút tiền:
   - Yêu cầu đang chờ (Pending)
   - Yêu cầu đã chấp thuận (Approved)
   - Yêu cầu đã từ chối (Rejected)
   - Yêu cầu đã hoàn thành (Completed)

**Bước 4:** Xem chi tiết mỗi yêu cầu:
   - Số tiền yêu cầu
   - Số tiền thực nhận
   - Phí hệ thống
   - Thông tin ngân hàng
   - Trạng thái
   - Thời gian tạo
   - Thời gian xử lý
   - Ghi chú từ admin (nếu có)

**Bước 5:** Lọc yêu cầu:
   - Theo trạng thái
   - Theo khoảng thời gian

### Vehicle Management (For Driver)

The vehicle management function allows drivers to register and manage their vehicles.

**Steps to Manage Vehicles:**

1. From the home screen, click "Vehicles" in the navigation menu

2. View registered vehicles:
   - Vehicle type
   - License plate
   - Maximum weight capacity
   - Vehicle status

3. Add new vehicle:
   - Click "Add Vehicle"
   - Select vehicle type
   - Enter license plate
   - Enter maximum weight (kg)
   - Upload vehicle documents:
     - Vehicle registration
     - Insurance documents
   - Upload vehicle photo
   - Click "Submit"

4. Edit vehicle:
   - Click "Edit" on a vehicle
   - Update information
   - Click "Save"

5. Deactivate vehicle:
   - Click "Deactivate" on a vehicle
   - Confirm deactivation
   - Vehicle will not appear in available orders

### 7.1 Driver Onboarding

Chức năng đăng ký tài xế cho phép người dùng đăng ký trở thành tài xế trong hệ thống.

**Bước 1:** Đăng ký tài khoản khách hàng trước

**Bước 2:** Từ màn hình chính, click "Become a Driver" hoặc "Apply as Driver"

**Bước 3:** Điền form đăng ký:
   - Thông tin cá nhân
   - Số CMND/CCCD
   - Số bằng lái xe
   - Thông tin xe
   - Khu vực phục vụ (chọn từ danh sách quận/huyện)

**Bước 4:** Upload các tài liệu cần thiết:
   - CMND/CCCD (mặt trước và mặt sau)
   - Bằng lái xe (mặt trước và mặt sau)
   - Ảnh chân dung
   - Ảnh xe (nhiều ảnh)
   - Giấy đăng ký xe
   - Tài liệu bảo hiểm

**Bước 5:** Gửi đơn đăng ký

**Bước 6:** Chờ admin phê duyệt:
   - Trạng thái đơn: "Pending"
   - Admin sẽ xem xét tài liệu
   - Bạn sẽ được thông báo khi được phê duyệt/từ chối

**Bước 7:** Sau khi được phê duyệt:
   - Vai trò tài khoản của bạn được cập nhật thành "Driver"
   - Bạn có thể bắt đầu nhận đơn hàng
   - Hoàn tất đăng ký xe của bạn

### 7.2 View My Application

Chức năng xem đơn đăng ký của tôi cho phép người dùng xem trạng thái đơn đăng ký tài xế của mình.

**Bước 1:** Đăng nhập vào hệ thống

**Bước 2:** Truy cập trang Profile hoặc "My Application"

**Bước 3:** Xem thông tin đơn đăng ký:
   - Trạng thái đơn (Pending/Approved/Rejected)
   - Thông tin đã nộp
   - Tài liệu đã upload
   - Ngày nộp đơn
   - Ngày xử lý (nếu có)

**Bước 4:** Xem chi tiết:
   - Thông tin cá nhân
   - Thông tin xe
   - Khu vực phục vụ
   - Tất cả tài liệu đã upload

**Bước 5:** Nếu bị từ chối:
   - Xem lý do từ chối
   - Có thể nộp lại đơn sau khi chỉnh sửa

### 7.3 View Application Detail

Chức năng xem chi tiết đơn đăng ký cho phép xem đầy đủ thông tin một đơn đăng ký cụ thể.

**Bước 1:** Truy cập "My Application" hoặc danh sách đơn đăng ký

**Bước 2:** Click vào đơn đăng ký muốn xem

**Bước 3:** Xem chi tiết đầy đủ:
   - Thông tin người nộp đơn
   - Thông tin cá nhân
   - Thông tin xe
   - Khu vực phục vụ
   - Tất cả tài liệu đã upload
   - Lịch sử xử lý

**Bước 4:** Download tài liệu (nếu cần)

**Lưu ý:**
- Chỉ có thể xem đơn đăng ký của chính mình (trừ admin)
- Admin có thể xem tất cả đơn đăng ký

### 7.4 View Driver Registration List (Admin)

Chức năng xem danh sách đơn đăng ký tài xế cho phép admin xem tất cả đơn đăng ký trong hệ thống.

**Bước 1:** Đăng nhập với tài khoản Admin

**Bước 2:** Truy cập "Driver Applications" hoặc "Quản lý đơn đăng ký tài xế"

**Bước 3:** Xem danh sách đơn đăng ký:
   - Đơn đang chờ (Pending)
   - Đơn đã chấp thuận (Approved)
   - Đơn đã từ chối (Rejected)

**Bước 4:** Lọc đơn đăng ký:
   - Theo trạng thái
   - Theo ngày nộp
   - Theo tên người nộp

**Bước 5:** Xem chi tiết đơn đăng ký:
   - Click vào đơn để xem đầy đủ thông tin
   - Xem tất cả tài liệu đã upload
   - Xem lịch sử xử lý

### 7.5 Approve/Reject Driver Application (Admin)

Chức năng phê duyệt/từ chối đơn đăng ký cho phép admin xử lý các đơn đăng ký tài xế.

**Bước 1:** Truy cập "Driver Applications"

**Bước 2:** Chọn đơn đăng ký cần xử lý

**Bước 3:** Xem xét đầy đủ thông tin:
   - Thông tin cá nhân
   - Tài liệu (CMND, bằng lái, giấy đăng ký xe)
   - Thông tin xe
   - Khu vực phục vụ

**Bước 4:** Phê duyệt đơn:
   - Click "Approve" hoặc "Chấp thuận"
   - Hệ thống tự động cập nhật vai trò người dùng thành "Driver"
   - Người dùng được thông báo

**Bước 5:** Từ chối đơn:
   - Click "Reject" hoặc "Từ chối"
   - Nhập lý do từ chối
   - Người dùng được thông báo và có thể xem lý do

**Lưu ý:**
- Sau khi phê duyệt, người dùng có thể đăng nhập với vai trò Driver
- Đơn đã từ chối có thể được nộp lại sau khi chỉnh sửa

### 7.6 Get Districts List

Chức năng lấy danh sách quận/huyện cung cấp danh sách các quận/huyện có sẵn trong hệ thống.

**Danh sách quận/huyện:**
- Quận Cẩm Lệ
- Quận Hải Châu
- Quận Liên Chiểu
- Quận Ngũ Hành Sơn
- Quận Sơn Trà
- Quận Thanh Khê
- Huyện Hòa Vang
- Huyện Hoàng Sa

**Sử dụng:**
- Hiển thị trong form đăng ký tài xế
- Chọn khu vực phục vụ
- Lọc đơn hàng theo khu vực

### 10.1 View Dashboard Statistics

Chức năng xem thống kê dashboard cho phép admin xem tổng quan về hệ thống.

**Bước 1:** Đăng nhập với tài khoản Admin

**Bước 2:** Truy cập Admin Dashboard

**Bước 3:** Xem thống kê tổng quan:
   - Tổng số người dùng (Customers, Drivers, Admins)
   - Tổng số đơn hàng
   - Đơn hàng hoàn thành
   - Đơn hàng đang xử lý
   - Tổng doanh thu hệ thống
   - Doanh thu tài xế
   - Phí hệ thống thu được

**Bước 4:** Xem biểu đồ:
   - Biểu đồ đơn hàng theo thời gian
   - Biểu đồ doanh thu theo thời gian
   - Biểu đồ người dùng theo thời gian

**Bước 5:** Xem thống kê chi tiết:
   - Thống kê theo ngày
   - Thống kê theo tuần
   - Thống kê theo tháng

### 10.2 View Account List

Chức năng xem danh sách tài khoản cho phép admin xem tất cả tài khoản trong hệ thống.

**Bước 1:** Truy cập "Accounts" hoặc "Quản lý tài khoản"

**Bước 2:** Xem danh sách tài khoản:
   - Tất cả người dùng (Customers, Drivers, Admins)
   - Trạng thái tài khoản (Active/Inactive)
   - Ngày đăng ký
   - Lần đăng nhập cuối

**Bước 3:** Lọc tài khoản:
   - Theo vai trò (Customer/Driver/Admin)
   - Theo trạng thái (Active/Inactive)
   - Theo ngày đăng ký
   - Theo tên/email

**Bước 4:** Tìm kiếm tài khoản:
   - Theo tên
   - Theo email
   - Theo số điện thoại

### 10.3 View Account Detail

Chức năng xem chi tiết tài khoản cho phép admin xem đầy đủ thông tin một tài khoản.

**Bước 1:** Từ danh sách tài khoản, click vào tài khoản muốn xem

**Bước 2:** Xem thông tin chi tiết:
   - Thông tin cá nhân
   - Thông tin tài khoản
   - Lịch sử đơn hàng
   - Lịch sử giao dịch
   - Lịch sử hoạt động

**Bước 3:** Xem thống kê:
   - Số đơn hàng đã tạo (nếu là Customer)
   - Số đơn hàng đã nhận (nếu là Driver)
   - Tổng doanh thu (nếu là Driver)

**Bước 4:** Quản lý tài khoản:
   - Kích hoạt/Vô hiệu hóa tài khoản
   - Cấm tài khoản
   - Xem lịch sử thay đổi

### 10.4 Admin Ban/Unban Account

Chức năng cấm/mở cấm tài khoản cho phép admin quản lý trạng thái tài khoản người dùng.

**Bước 1:** Truy cập "Accounts"

**Bước 2:** Chọn tài khoản cần quản lý

**Bước 3:** Cấm tài khoản:
   - Click "Ban" hoặc "Cấm"
   - Nhập lý do cấm
   - Tài khoản bị vô hiệu hóa
   - Người dùng không thể đăng nhập

**Bước 4:** Mở cấm tài khoản:
   - Click "Unban" hoặc "Mở cấm"
   - Tài khoản được kích hoạt lại
   - Người dùng có thể đăng nhập

**Lưu ý:**
- Tài khoản bị cấm không thể sử dụng hệ thống
- Có thể xem lịch sử cấm/mở cấm

### 10.5 View Driver List

Chức năng xem danh sách tài xế cho phép admin xem tất cả tài xế trong hệ thống.

**Bước 1:** Truy cập "Drivers" hoặc "Quản lý tài xế"

**Bước 2:** Xem danh sách tài xế:
   - Tất cả tài xế
   - Trạng thái (Active/Inactive/Banned)
   - Số đơn đã nhận
   - Tổng doanh thu
   - Đánh giá trung bình

**Bước 3:** Lọc tài xế:
   - Theo trạng thái
   - Theo khu vực phục vụ
   - Theo đánh giá
   - Theo doanh thu

### 10.6 View Driver Detail

Chức năng xem chi tiết tài xế cho phép admin xem đầy đủ thông tin một tài xế.

**Bước 1:** Từ danh sách tài xế, click vào tài xế muốn xem

**Bước 2:** Xem thông tin chi tiết:
   - Thông tin cá nhân
   - Thông tin tài khoản
   - Thông tin xe
   - Khu vực phục vụ
   - Lịch sử đơn hàng
   - Lịch sử giao dịch
   - Lịch sử rút tiền
   - Đánh giá từ khách hàng

**Bước 3:** Xem thống kê:
   - Tổng số đơn đã nhận
   - Tổng số đơn hoàn thành
   - Tổng doanh thu
   - Phí hệ thống đã thu
   - Số dư hiện tại
   - Đánh giá trung bình

### 10.7 Payout to Driver

Chức năng chi trả cho tài xế cho phép admin chi trả tiền trực tiếp cho tài xế.

**Bước 1:** Truy cập "Drivers"

**Bước 2:** Chọn tài xế cần chi trả

**Bước 3:** Click "Payout" hoặc "Chi trả"

**Bước 4:** Nhập thông tin chi trả:
   - Số tiền chi trả
   - Lý do chi trả
   - Ghi chú

**Bước 5:** Xác nhận chi trả:
   - Kiểm tra thông tin
   - Click "Confirm Payout"
   - Tiền được cộng vào số dư tài xế
   - Tạo giao dịch trong lịch sử

**Lưu ý:**
- Chi trả được ghi nhận trong lịch sử giao dịch
- Tài xế có thể xem chi tiết trong trang Revenue

### 10.8 Reset Driver Balance with Penalty

Chức năng reset số dư với phạt cho phép admin reset số dư tài xế và trừ 20% phí phạt.

**Bước 1:** Truy cập "Drivers"

**Bước 2:** Chọn tài xế cần reset số dư

**Bước 3:** Click "Reset Balance" hoặc "Reset số dư"

**Bước 4:** Xem thông tin:
   - Số dư hiện tại
   - Số tiền sẽ bị trừ (20%)
   - Số dư sau khi reset

**Bước 5:** Nhập lý do reset

**Bước 6:** Xác nhận reset:
   - Click "Confirm Reset"
   - Số dư được reset về 0
   - 20% số dư được trừ làm phí phạt
   - Tạo giao dịch trong lịch sử

**Lưu ý:**
- Chỉ sử dụng trong trường hợp đặc biệt
- Hành động này không thể hoàn tác
- Phí phạt được cộng vào doanh thu hệ thống

### 10.9 View Driver Revenue Statistics

Chức năng xem thống kê doanh thu tài xế cho phép admin xem thống kê doanh thu của một tài xế cụ thể.

**Bước 1:** Truy cập "Drivers"

**Bước 2:** Chọn tài xế muốn xem thống kê

**Bước 3:** Click "Revenue Statistics" hoặc "Thống kê doanh thu"

**Bước 4:** Chọn khoảng thời gian:
   - Hôm nay
   - Tuần này
   - Tháng này
   - Tùy chỉnh

**Bước 5:** Xem thống kê:
   - Tổng doanh thu
   - Số đơn hoàn thành
   - Phí hệ thống thu được
   - Thu nhập thực tế của tài xế
   - Biểu đồ doanh thu

### 10.10 View All Orders

Chức năng xem tất cả đơn hàng cho phép admin xem tất cả đơn hàng trong hệ thống.

**Bước 1:** Truy cập "Orders" hoặc "Quản lý đơn hàng"

**Bước 2:** Xem danh sách đơn hàng:
   - Tất cả đơn hàng
   - Đơn hàng theo trạng thái
   - Đơn hàng theo tài xế
   - Đơn hàng theo khách hàng

**Bước 3:** Lọc đơn hàng:
   - Theo trạng thái
   - Theo khoảng thời gian
   - Theo tài xế
   - Theo khách hàng

**Bước 4:** Xem chi tiết đơn hàng:
   - Thông tin đơn hàng
   - Thông tin khách hàng
   - Thông tin tài xế (nếu có)
   - Lịch sử trạng thái
   - Thông tin thanh toán

### 8.6 View Platform Revenue (Admin)

Chức năng xem doanh thu hệ thống cho phép admin xem tổng quan doanh thu của nền tảng.

**Bước 1:** Truy cập "Revenue" hoặc "Doanh thu hệ thống"

**Bước 2:** Xem dashboard doanh thu:
   - Tổng doanh thu hệ thống
   - Doanh thu theo thời kỳ (ngày/tuần/tháng/năm)
   - Biểu đồ doanh thu

**Bước 3:** Xem thống kê:
   - Tổng số đơn hàng
   - Đơn hàng hoàn thành
   - Đơn hàng bị hủy
   - Tổng số tài xế
   - Tài xế đang hoạt động
   - Tổng số khách hàng

**Bước 4:** Xem thu nhập tài xế:
   - Tổng thu nhập tài xế
   - Phí hệ thống đã thu (20%)
   - Thu nhập trung bình mỗi tài xế

**Bước 5:** Xem chi tiết:
   - Doanh thu theo ngày
   - Doanh thu theo tuần
   - Doanh thu theo tháng
   - Top tài xế có doanh thu cao nhất

### 8.7 Manage Withdrawals (Admin)

Chức năng quản lý yêu cầu rút tiền cho phép admin xử lý các yêu cầu rút tiền từ tài xế.

**Bước 1:** Truy cập "Withdrawals" hoặc "Quản lý rút tiền"

**Bước 2:** Xem danh sách yêu cầu rút tiền:
   - Yêu cầu đang chờ (Pending)
   - Yêu cầu đã chấp thuận (Approved)
   - Yêu cầu đã từ chối (Rejected)
   - Yêu cầu đã hoàn thành (Completed)

**Bước 3:** Xem chi tiết yêu cầu:
   - Click vào yêu cầu
   - Xem thông tin tài xế
   - Kiểm tra số tiền yêu cầu
   - Xác minh thông tin tài khoản ngân hàng

**Bước 4:** Xử lý yêu cầu:
   - **Chấp thuận:**
     - Click "Approve" hoặc "Chấp thuận"
     - Trừ tiền từ số dư tài xế
     - Cập nhật trạng thái yêu cầu
     - Tài xế được thông báo
   
   - **Từ chối:**
     - Click "Reject" hoặc "Từ chối"
     - Nhập lý do từ chối
     - Tài xế được thông báo

   - **Hoàn thành:**
     - Click "Complete" sau khi đã chuyển tiền
     - Đánh dấu yêu cầu đã hoàn thành
     - Tài xế được thông báo

**Lưu ý:**
- Số tiền thực nhận = 80% số tiền yêu cầu
- Phí hệ thống = 20% số tiền yêu cầu
- Phải xác minh thông tin tài khoản trước khi chấp thuận

### 8.8 View Withdrawal Statistics (Admin)

Chức năng xem thống kê yêu cầu rút tiền cho phép admin xem thống kê về các yêu cầu rút tiền.

**Bước 1:** Truy cập "Withdrawals"

**Bước 2:** Click "Statistics" hoặc "Thống kê"

**Bước 3:** Xem thống kê tổng quan:
   - Tổng số yêu cầu
   - Số yêu cầu theo trạng thái
   - Tổng số tiền yêu cầu
   - Tổng số tiền đã chuyển
   - Tổng phí hệ thống thu được

**Bước 4:** Xem thống kê theo thời gian:
   - Chọn khoảng thời gian
   - Xem biểu đồ yêu cầu rút tiền
   - Xem biểu đồ số tiền

**Bước 5:** Xuất báo cáo (nếu cần)

---

## 11. AI Chat Assistant

### 11.1 Chat with AI Assistant

Chức năng chat với AI assistant cho phép người dùng tư vấn về dịch vụ giao hàng thông qua trợ lý AI.

**Bước 1:** Truy cập trang chủ hoặc bất kỳ trang nào trong hệ thống

**Bước 2:** Tìm biểu tượng chat AI (thường ở góc dưới bên phải màn hình)

**Bước 3:** Click vào biểu tượng để mở cửa sổ chat

**Bước 4:** Bắt đầu trò chuyện:
   - AI sẽ chào hỏi và giới thiệu về dịch vụ
   - Bạn có thể hỏi về:
     - Các loại xe vận chuyển
     - Giá cả dịch vụ
     - Cách đặt đơn hàng
     - Quy trình giao hàng
     - Chính sách và điều khoản

**Bước 5:** Nhập câu hỏi và nhấn Enter hoặc click nút "Send"

**Bước 6:** AI sẽ trả lời câu hỏi của bạn

**Bước 7:** Tiếp tục trò chuyện hoặc đóng cửa sổ chat

**Lưu ý:**
- AI sử dụng Gemini API để xử lý câu hỏi
- Không cần đăng nhập để sử dụng AI chat
- AI có thể tư vấn về các dịch vụ của hệ thống
- Lịch sử chat được lưu trong phiên làm việc hiện tại

**Tính năng:**
- Trả lời tự động và thông minh
- Hỗ trợ tiếng Việt
- Tư vấn về dịch vụ giao hàng
- Hướng dẫn sử dụng hệ thống

---

## 12. File Upload & Management

### 12.1 Upload Single Image

Chức năng upload một ảnh cho phép người dùng tải lên một ảnh duy nhất.

**Bước 1:** Truy cập trang có chức năng upload ảnh (Profile, Vehicle Management, etc.)

**Bước 2:** Click nút "Upload Image" hoặc "Tải ảnh lên"

**Bước 3:** Chọn file ảnh từ máy tính:
   - Định dạng hỗ trợ: JPG, PNG, GIF
   - Kích thước tối đa: 10MB

**Bước 4:** Xem preview ảnh đã chọn

**Bước 5:** Click "Upload" để tải ảnh lên

**Bước 6:** Ảnh được tải lên Cloudinary và trả về URL

**Bước 7:** URL ảnh được lưu vào hệ thống

**Lưu ý:**
- Ảnh được lưu trữ trên Cloudinary
- URL ảnh có thể sử dụng trong hệ thống
- Ảnh được tối ưu hóa tự động

### 12.2 Upload Multiple Images

Chức năng upload nhiều ảnh cho phép người dùng tải lên nhiều ảnh cùng lúc.

**Bước 1:** Truy cập trang có chức năng upload nhiều ảnh (Driver Onboarding, Vehicle Photos, etc.)

**Bước 2:** Click nút "Upload Images" hoặc "Tải nhiều ảnh"

**Bước 3:** Chọn nhiều file ảnh từ máy tính:
   - Có thể chọn tối đa 10 ảnh cùng lúc
   - Định dạng hỗ trợ: JPG, PNG, GIF
   - Kích thước tối đa mỗi ảnh: 10MB

**Bước 4:** Xem preview tất cả ảnh đã chọn

**Bước 5:** Có thể xóa ảnh không mong muốn trước khi upload

**Bước 6:** Click "Upload All" để tải tất cả ảnh lên

**Bước 7:** Hệ thống tải từng ảnh lên Cloudinary

**Bước 8:** Nhận danh sách URL của tất cả ảnh đã upload

**Lưu ý:**
- Tất cả ảnh được lưu trữ trên Cloudinary
- Có thể theo dõi tiến trình upload
- Nếu một ảnh lỗi, các ảnh khác vẫn được upload thành công

---

## 13. Additional Features

### 13.1 Browse Vehicles

Chức năng duyệt xe cho phép khách hàng xem danh sách các loại xe có sẵn trong hệ thống.

**Bước 1:** Truy cập trang "Vehicles" hoặc "Duyệt xe"

**Bước 2:** Xem danh sách các loại xe:
   - Xe máy
   - Xe tay ga
   - Xe ba gác
   - Xe tải nhỏ
   - Xe tải lớn
   - Xe container

**Bước 3:** Xem thông tin mỗi loại xe:
   - Tên loại xe
   - Tải trọng tối đa
   - Kích thước
   - Giá cước cơ bản
   - Mô tả

**Bước 4:** Lọc xe:
   - Theo loại xe
   - Theo tải trọng
   - Theo giá cước

**Bước 5:** Click vào xe để xem chi tiết

**Bước 6:** Có thể chọn loại xe khi tạo đơn hàng

### 13.2 Chat Page

Trang chat cho phép người dùng trao đổi với tài xế hoặc khách hàng.

**Đối với Khách hàng:**
- Truy cập trang "Chat" từ menu
- Xem danh sách cuộc trò chuyện với các tài xế
- Chọn cuộc trò chuyện để xem tin nhắn
- Gửi tin nhắn cho tài xế đang giao hàng
- Nhận tin nhắn từ tài xế

**Đối với Tài xế:**
- Truy cập trang "Chat" từ menu
- Xem danh sách cuộc trò chuyện với các khách hàng
- Chọn cuộc trò chuyện để xem tin nhắn
- Gửi tin nhắn cho khách hàng
- Nhận tin nhắn từ khách hàng

**Tính năng:**
- Chat real-time (sử dụng Socket.IO)
- Lịch sử tin nhắn
- Thông báo tin nhắn mới
- Gửi ảnh (nếu được hỗ trợ)

### 13.3 Contact Page

Trang liên hệ cung cấp thông tin liên hệ và hỗ trợ.

**Nội dung trang:**
- Thông tin liên hệ:
  - Email hỗ trợ
  - Số điện thoại hotline
  - Địa chỉ văn phòng
- Giờ làm việc
- Form liên hệ (nếu có)
- FAQ (Câu hỏi thường gặp)
- Hướng dẫn sử dụng

**Sử dụng:**
- Khách hàng có thể xem thông tin liên hệ
- Tài xế có thể xem thông tin hỗ trợ
- Admin có thể quản lý thông tin liên hệ

### 13.4 Reports Page (Customer)

Trang báo cáo cho phép khách hàng xem và quản lý các báo cáo vi phạm của mình.

**Bước 1:** Truy cập trang "Reports" hoặc "Báo cáo"

**Bước 2:** Xem danh sách báo cáo:
   - Tất cả báo cáo đã gửi
   - Báo cáo theo trạng thái
   - Báo cáo theo tài xế

**Bước 3:** Xem chi tiết báo cáo:
   - Loại vi phạm
   - Mô tả chi tiết
   - Bằng chứng (ảnh)
   - Trạng thái xử lý
   - Phản hồi từ admin

**Bước 4:** Tạo báo cáo mới:
   - Click "Report Violation" hoặc "Báo cáo vi phạm"
   - Chọn đơn hàng liên quan
   - Chọn loại vi phạm
   - Nhập mô tả
   - Upload bằng chứng (ảnh)
   - Gửi báo cáo

**Bước 5:** Theo dõi tiến trình xử lý báo cáo

**Tính năng:**
- Xem lịch sử báo cáo
- Tạo báo cáo mới
- Xem trạng thái xử lý
- Nhận thông báo khi báo cáo được xử lý

---

## Table of Tables

| Table | Description | Page |
|-------|-------------|------|
| Table 1: Deliverable Package | List of deliverables | 7 |
| Table 2: Software Requirements | Required software for installation | 8 |

## Table of Figures

| Figure | Description | Page |
|--------|-------------|------|
| Figure 1. Login Screen | Login interface for all users | 9 |
| Figure 2. Registration Screen | Customer registration form | 10 |
| Figure 3. Order Creation | Create new delivery order | 11 |
| Figure 4. Order Tracking | Real-time order tracking map | 12 |
| Figure 5. Driver Dashboard | Driver home screen with available orders | 13 |
| Figure 6. Revenue Dashboard | Driver revenue and earnings view | 14 |
| Figure 7. Admin Dashboard | Admin home screen with statistics | 15 |
| Figure 8. Driver Application Review | Admin reviewing driver application | 16 |

---

**Document Version:** 1.0  
**Last Updated:** December 2024  
**Prepared by:** Development Team  
**Reviewed by:** Project Manager

