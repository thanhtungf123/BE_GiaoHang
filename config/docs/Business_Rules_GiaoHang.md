# BUSINESS RULES - GIAO HÀNG NHANH
## DELIVERY MANAGEMENT SYSTEM
**Project:** GiaoHang Delivery System  
**Report Date:** December 2024  
**Version:** 1.0

---

## 5. Requirement Appendix

### 5.1 Business Rules

| ID | Rule Definition |
|----|----------------|
| **BR-01** | One email address can only be used to create one account. Email must be unique in the system. |
| **BR-02** | One phone number can only be used to create one account. Phone number must be unique in the system. |
| **BR-03** | User can register with either email or phone number, or both. If email is provided, it must be unique. |
| **BR-04** | OTP (One-Time Password) is valid for 10 minutes from the time of sending. After expiry, OTP cannot be used. |
| **BR-05** | User must verify email successfully before being allowed to log in. If user has email but email is not verified, login is denied. |
| **BR-06** | OTP can only be used once. After successful verification, OTP is marked as used and cannot be reused. |
| **BR-07** | User can request to resend OTP. System generates new OTP code and sends to user's email. |
| **BR-08** | Users can only change their password when they are logged in. Current password verification is required. |
| **BR-09** | New password must be at least 6 characters long. |
| **BR-10** | Only admin users can access the user management page and view all user accounts. |
| **BR-11** | Passwords are not displayed in API responses. Password hash field is excluded from user data. |
| **BR-12** | Admin can view all driver data for monitoring and verification purposes. |
| **BR-13** | Driver data must be linked to a valid User record. Driver profile cannot exist without corresponding User account. |
| **BR-14** | User must have email and email must be verified before submitting driver application. |
| **BR-15** | Driver application can only be submitted once per user. User cannot submit multiple applications. |
| **BR-16** | Driver application status can be: Pending, Approved, or Rejected. Only admin can change application status. |
| **BR-17** | When driver application is approved, user role is automatically updated to "Driver" and Driver profile is created. |
| **BR-18** | Driver must have at least one active vehicle to go online and receive orders. |
| **BR-19** | Driver must be online (isOnline = true) to receive available orders. Offline drivers do not receive order notifications. |
| **BR-20** | Driver can only accept orders within 2km radius from their current location. Orders beyond 2km cannot be accepted. |
| **BR-21** | Distance calculation uses Haversine formula with Earth radius of 6371km. Coordinates format: [longitude, latitude]. |
| **BR-22** | Driver must update their current location before accepting orders. Location is required for distance calculation. |
| **BR-23** | Vehicle type hierarchy: Larger vehicles can accept orders for smaller vehicle types. Hierarchy: PickupTruck (1) < TruckSmall (2) < TruckMedium (3) < TruckBox (4) < TruckLarge/DumpTruck (5) < Trailer (6). |
| **BR-24** | Driver can only accept order items with status "Created". Items with other statuses cannot be accepted. |
| **BR-25** | Each order item can only be accepted by one driver. Once accepted, item is assigned to that driver. |
| **BR-26** | Order item status transitions: Created → Accepted → PickedUp → Delivering → Delivered. Status cannot be skipped or reversed. |
| **BR-27** | Order item can be cancelled at any status. Cancellation sets status to "Cancelled" and records cancellation reason. |
| **BR-28** | Order status is automatically calculated based on item statuses: All items Delivered → Order Completed, All items Cancelled → Order Cancelled, Any item Active → Order InProgress. |
| **BR-29** | Customer can only cancel orders that have not been accepted by any driver. Once driver accepts, customer cannot cancel. |
| **BR-30** | Driver can cancel orders they have accepted. Cancellation requires reason and notifies customer. |
| **BR-31** | Order must have at least one item. Empty orders cannot be created. |
| **BR-32** | Order items must have weightKg and distanceKm. These fields are required for price calculation. |
| **BR-33** | Order price calculation formula: Total = (Distance × PricePerKm) + LoadingFee (if applicable) + InsuranceFee (if applicable). |
| **BR-34** | Price per kilometer is determined by weight: ≤1 ton = 40,000 VND/km, 1-3 tons = 60,000 VND/km, 3-5 tons = 80,000 VND/km, 5-10 tons = 100,000 VND/km, >10 tons = 150,000 VND/km. |
| **BR-35** | If driver vehicle has pricePerKm set, system uses vehicle pricePerKm. Otherwise, uses default price based on weight. |
| **BR-36** | Loading service fee is 50,000 VND. Only charged if loadingService is true. |
| **BR-37** | Insurance fee is 100,000 VND. Only charged if insurance is true. |
| **BR-38** | Customer can update insurance for pending orders only. Once order is accepted, insurance cannot be changed. |
| **BR-39** | Payment method can be "Cash" or "Banking". Payment by can be "sender" (customer pays) or "receiver" (recipient pays). |
| **BR-40** | Payment status can be: Pending, Paid, or Failed. Payment is processed when order item is delivered. |
| **BR-41** | When order item is delivered with paymentBy="sender", payment is processed immediately. Driver receives 80% of amount. |
| **BR-42** | When order item is delivered with paymentBy="receiver", payment is processed when receiver pays. Driver receives 80% of amount. |
| **BR-43** | System commission is 20% of order amount. Driver receives 80% of order amount as net income. |
| **BR-44** | Commission is calculated and deducted automatically when order is delivered. Transaction is recorded in DriverTransaction. |
| **BR-45** | Driver balance (incomeBalance) is updated automatically when order is delivered. Balance increases by net amount (80% of order value). |
| **BR-46** | Driver can only request withdrawal if balance is sufficient. Requested amount cannot exceed current balance. |
| **BR-47** | Withdrawal request requires bank account information: bank name, account name, account number, and confirmation of account number. |
| **BR-48** | Bank account number confirmation must match the original account number. Mismatch prevents withdrawal request. |
| **BR-49** | Withdrawal amount calculation: Driver receives 80% of requested amount, system fee is 20% of requested amount. |
| **BR-50** | Withdrawal request status can be: Pending, Approved, Rejected, or Completed. Only admin can change status. |
| **BR-51** | Withdrawal can only be completed from Approved status. Admin must approve before marking as Completed. |
| **BR-52** | When withdrawal is approved, driver balance is deducted by full requested amount. Transaction is created with type "Withdrawal". |
| **BR-53** | Customer can only rate and review orders that have status "Completed". Incomplete orders cannot be rated. |
| **BR-54** | Customer can only rate order items that have status "Delivered". Items not delivered cannot be rated. |
| **BR-55** | Customer can only create one feedback per order/item. Duplicate feedbacks are not allowed. |
| **BR-56** | Overall rating is required (1-5 stars). Detailed ratings (service, driver, vehicle, punctuality) are optional. |
| **BR-57** | Feedback comment has maximum length of 1000 characters. |
| **BR-58** | Feedback can include up to 5 photos. Each photo must be less than 2MB and in image format. |
| **BR-59** | Feedback can be anonymous. If anonymous, customer name is not displayed publicly. |
| **BR-60** | Driver rating is automatically calculated as average of all approved feedbacks. Rating updates when new feedback is created or deleted. |
| **BR-61** | Only approved feedbacks are counted in driver rating calculation. Pending or rejected feedbacks are excluded. |
| **BR-62** | Driver can respond to customer feedback. Response is displayed publicly below the feedback. |
| **BR-63** | Customer can only delete their own feedback. Deleted feedback is removed from rating calculation. |
| **BR-64** | Admin can update feedback status: Approved (visible), Rejected (hidden), or Pending (under review). |
| **BR-65** | Customer can only report violations for orders they own. Cannot report violations for other customers' orders. |
| **BR-66** | Violation can only be reported for completed orders. Incomplete orders cannot have violations reported. |
| **BR-67** | Customer cannot create duplicate violation reports for the same order/item. Duplicate reports are rejected. |
| **BR-68** | Violation report requires violation type, description, and optionally photos as evidence. |
| **BR-69** | Violation severity can be: Low, Medium, High, or Critical. Default is Medium. |
| **BR-70** | Violation status can be: Pending, Investigating, Resolved, or Dismissed. Only admin can change status. |
| **BR-71** | Admin can apply penalty to driver for violations. Penalty amount is deducted from driver balance. |
| **BR-72** | Admin can reset driver balance with 20% penalty. Remaining 80% is paid out, 20% is kept as penalty fee. |
| **BR-73** | Admin can ban/unban driver accounts. Banned drivers cannot access the system. |
| **BR-74** | Admin can ban/unban customer accounts. Banned customers cannot access the system. |
| **BR-75** | Driver must have active vehicle to set online status. Inactive vehicles prevent driver from going online. |
| **BR-76** | Driver service areas are stored as array of district names. Orders are filtered by driver service areas. |
| **BR-77** | Driver location coordinates must be valid: latitude between -90 and 90, longitude between -180 and 180. |
| **BR-78** | Driver location is stored in GeoJSON format: { type: "Point", coordinates: [longitude, latitude] }. |
| **BR-79** | Available orders are filtered by: driver is online, driver location within 2km of pickup, vehicle type compatibility, service area match. |
| **BR-80** | Orders are sorted by distance from driver location. Closest orders appear first in available orders list. |
| **BR-81** | Order items without driver assignment (driverId is null) are considered available. Items with driverId are not available. |
| **BR-82** | Socket.IO emits new order notifications only to drivers within 2km radius of pickup location. |
| **BR-83** | Real-time order tracking uses Socket.IO rooms. Customer joins room "customer:{customerId}", driver joins room "driver:{driverId}". |
| **BR-84** | Order status updates are broadcasted to customer via Socket.IO. Customer receives real-time notifications. |
| **BR-85** | VNPay payment URL is generated with order information. Payment amount is in VND (multiplied by 100 for VNPay format). |
| **BR-86** | VNPay IPN callback verifies payment checksum before processing. Invalid checksum is rejected. |
| **BR-87** | Payment processing is idempotent. If payment is already marked as "Paid", subsequent callbacks are ignored. |
| **BR-88** | File uploads are limited to images only. Maximum file size is 2MB per image for feedback photos. |
| **BR-89** | Avatar upload requires valid image URL. URL is stored in user profile and driver profile (if applicable). |
| **BR-90** | Driver application documents are uploaded to Cloudinary. Documents include: license (front/back), ID card (front/back), portrait, vehicle photos, vehicle documents. |
| **BR-91** | Profile name cannot be empty. Name is required field for profile update. |
| **BR-92** | Driver bank information is required for withdrawal requests: bank name, account name, account number are mandatory. |
| **BR-93** | JWT token is required for authenticated endpoints. Token is validated on each request. |
| **BR-94** | JWT token contains user ID and role. Role-based access control is enforced at middleware level. |
| **BR-95** | Customer role can access customer-specific endpoints. Driver role can access driver-specific endpoints. Admin role can access all endpoints. |
| **BR-96** | Order insurance can only be updated when order status is "Pending". Once order is accepted, insurance cannot be changed. |
| **BR-97** | Order total price is sum of all item prices. Total price is calculated automatically when order is created. |
| **BR-98** | Driver transaction types: OrderEarning (from completed orders), Withdrawal (money withdrawal), Payout (admin direct payment), Penalty (violation penalty). |
| **BR-99** | Driver transaction status can be: Pending, Completed, or Failed. Completed transactions update driver balance. |
| **BR-100** | Admin can directly payout money to driver. Payout creates transaction with type "Payout" and updates driver balance. |
| **BR-101** | System revenue is calculated as sum of all transaction fees (20% commission from all orders). |
| **BR-102** | Driver total trips counter increments by 1 when order item is delivered. Counter tracks driver's completed deliveries. |
| **BR-103** | Driver rating default is 5.0. Rating is updated based on average of all approved feedbacks. |
| **BR-104** | Feedback status default is "Approved". Admin can change to "Rejected" to hide inappropriate feedbacks. |
| **BR-105** | Violation reports can be anonymous. Anonymous reports do not display reporter information. |
| **BR-106** | Admin can add notes when processing violation reports. Notes are visible to admin only. |
| **BR-107** | Order cancellation by driver requires cancellation reason. Reason is stored and visible to customer. |
| **BR-108** | Order cancellation by customer is only allowed when no driver has accepted any item. Once accepted, customer cannot cancel. |
| **BR-109** | Payment refund is processed if order is cancelled and payment was already made. Refund method depends on original payment method. |
| **BR-110** | Order item photos are optional. Photos can be uploaded during order creation or added later. |
| **BR-111** | Driver must have valid bank account information before creating withdrawal request. Missing information prevents withdrawal. |
| **BR-112** | Withdrawal request amount must be positive number. Zero or negative amounts are rejected. |
| **BR-113** | Driver balance cannot go negative. Withdrawal and penalty operations check balance before processing. |
| **BR-114** | Admin revenue statistics include: total system revenue (20% fees), total driver payouts (80% of orders), total withdrawal requests. |
| **BR-115** | Order status "Created" means order is available for drivers to accept. No driver has been assigned yet. |
| **BR-116** | Order status "InProgress" means at least one item has been accepted by driver. Order is being processed. |
| **BR-117** | Order status "Completed" means all items have been delivered. Order is finished. |
| **BR-118** | Order status "Cancelled" means all items have been cancelled. Order cannot be processed further. |
| **BR-119** | Vehicle status can be: Active, Maintenance, or Inactive. Only Active vehicles can be used for orders. |
| **BR-120** | Driver status can be: Pending, Active, Rejected, or Blocked. Only Active drivers can receive orders. |
| **BR-121** | User role can be: Customer, Driver, or Admin. User can have multiple roles (stored in roles array). |
| **BR-122** | Email verification is optional if user registers with phone only. If email is provided, verification is required. |
| **BR-123** | OTP purpose can be: "verify_email" or "reset_password". Different purposes use different OTP codes. |
| **BR-124** | Password reset requires valid OTP code. OTP must match and not be expired. |
| **BR-125** | Password reset OTP expires after 10 minutes. Expired OTP cannot be used for password reset. |
| **BR-126** | Driver application districts list is retrieved from API. Districts are used for service area selection. |
| **BR-127** | Service areas are stored as array of district names. Driver can select multiple districts for service areas. |
| **BR-128** | Orders are filtered by driver service areas. Orders outside service areas are not shown to driver. |
| **BR-129** | Driver location update timestamp (locationUpdatedAt) is recorded. System tracks when location was last updated. |
| **BR-130** | Real-time order notifications are sent via Socket.IO. Drivers receive notifications for new orders within 2km. |
| **BR-131** | Customer receives real-time updates when driver accepts order, picks up order, delivers order, or cancels order. |
| **BR-132** | Order item status "Accepted" means driver has accepted the item. Item is assigned to that driver. |
| **BR-133** | Order item status "PickedUp" means driver has picked up the item from pickup location. |
| **BR-134** | Order item status "Delivering" means driver is currently delivering the item to dropoff location. |
| **BR-135** | Order item status "Delivered" means item has been successfully delivered to dropoff location. |
| **BR-136** | Order item status "Cancelled" means item has been cancelled. Cancellation can be by customer or driver. |
| **BR-137** | Payment processing triggers when item status changes to "Delivered" and paymentBy matches the payment trigger condition. |
| **BR-138** | Driver transaction is created when payment is processed. Transaction records amount, fee, net amount, and type. |
| **BR-139** | Driver balance update and transaction creation are atomic operations. Both must succeed or both fail. |
| **BR-140** | Withdrawal request creation does not deduct balance immediately. Balance is deducted when admin approves withdrawal. |
| **BR-141** | Withdrawal approval checks balance again before processing. Balance may have changed since request creation. |
| **BR-142** | Withdrawal rejection does not affect driver balance. Rejected requests are simply marked as rejected. |
| **BR-143** | Feedback creation automatically updates driver rating. Rating calculation uses average of all approved feedbacks. |
| **BR-144** | Feedback deletion automatically recalculates driver rating. Rating is updated based on remaining approved feedbacks. |
| **BR-145** | Feedback status change from Approved to Rejected removes feedback from rating calculation. Rating is recalculated. |
| **BR-146** | Violation report creation does not automatically affect driver. Admin must review and take action. |
| **BR-147** | Violation penalty is optional. Admin can apply penalty when processing violation report. |
| **BR-148** | Violation penalty is deducted from driver balance. Penalty transaction is created with type "Penalty". |
| **BR-149** | Admin can view violation statistics: total reports, reports by type, reports by driver, reports by severity. |
| **BR-150** | Admin can view withdrawal statistics: total requests, total amounts, requests by status, system fees collected. |

---

## Summary Statistics

| Category | Count |
|----------|-------|
| **Total Business Rules** | 150 |
| **Authentication & Account Rules** | 15 |
| **Order Management Rules** | 35 |
| **Driver Management Rules** | 30 |
| **Payment & Financial Rules** | 25 |
| **Feedback & Rating Rules** | 15 |
| **Violation & Reporting Rules** | 10 |
| **System & Technical Rules** | 20 |

---

**Document Version:** 1.0  
**Last Updated:** December 2024  
**Prepared by:** Development Team  
**Reviewed by:** Project Manager








