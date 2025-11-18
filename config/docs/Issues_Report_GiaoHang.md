# ISSUES REPORT - GIAO HÀNG NHANH
## DELIVERY MANAGEMENT SYSTEM
**Project:** GiaoHang Delivery System  
**Report Date:** December 2024  
**Version:** 1.0

---

## Table of Issues

| Title | Description | Issue ID | URL | State | Assignee | Created At | Due Date | Milestone | Labels | Functions/Screens |
|-------|-------------|----------|-----|-------|----------|------------|----------|-----------|--------|-------------------|
| User Login Screen | This screen allows users (Customer, Driver, Admin) to enter email/phone and password to login. The system automatically determines user role and redirects to appropriate dashboard. Includes links for registration and password reset. | 1 | `https://gitlab.com/giaohang/project/-/issues/1` | Closed | Development Team | 01/10/2024 | 05/10/2024 | iter1 | WP, 3_Done | User Login |
| User Registration Screen | This screen allows new customers to register an account by entering name, phone, email, and password. Includes OTP email verification step before completing registration. | 2 | `https://gitlab.com/giaohang/project/-/issues/2` | Closed | Development Team | 01/10/2024 | 05/10/2024 | iter1 | WP, 3_Done | User Registration |
| Order Creation Screen | This screen allows customers to create delivery orders by selecting pickup and dropoff locations, adding items with weight, choosing additional services (loading, insurance), and selecting payment method. System automatically calculates distance and price. | 3 | `https://gitlab.com/giaohang/project/-/issues/3` | Closed | Development Team | 05/10/2024 | 10/10/2024 | iter1 | WP, 3_Done | Order Creation |
| Driver Available Orders Screen | This screen displays orders available for driver acceptance. Orders are filtered by service area, vehicle type compatibility, weight capacity, and distance (within 2km radius). Drivers can view order details and accept orders. | 4 | `https://gitlab.com/giaohang/project/-/issues/4` | Closed | Development Team | 10/10/2024 | 15/10/2024 | iter1 | WP, 3_Done | Driver Orders |
| Order Acceptance Feature | This feature allows drivers to accept available orders. System checks distance (≤2km), vehicle compatibility, and assigns driver to order item. Updates order status and notifies customer via Socket.IO. | 5 | `https://gitlab.com/giaohang/project/-/issues/5` | Closed | Development Team | 10/10/2024 | 15/10/2024 | iter1 | WP, 3_Done | Order Acceptance |
| Real-time Order Tracking | This feature allows customers to track their orders in real-time. Uses Socket.IO for live location updates, displays driver location on map, shows order status changes, and estimated delivery time. | 6 | `https://gitlab.com/giaohang/project/-/issues/6` | Closed | Development Team | 15/10/2024 | 20/10/2024 | iter1 | WP, 3_Done | Order Tracking |
| Payment Integration (VNPay) | This feature integrates VNPay payment gateway for online payments. Customers can pay for orders using banking transfer. Includes payment URL generation, IPN callback handling, and payment status update. | 7 | `https://gitlab.com/giaohang/project/-/issues/7` | Closed | Development Team | 20/10/2024 | 25/10/2024 | iter1 | WP, 3_Done | Payment |
| Driver Onboarding Screen | This screen allows users to apply to become a driver. Includes form for personal information, ID card, driver license, vehicle information, service areas selection, and document upload (ID photos, license, vehicle registration, insurance). | 8 | `https://gitlab.com/giaohang/project/-/issues/8` | Closed | Development Team | 10/10/2024 | 15/10/2024 | iter1 | WP, 3_Done | Driver Onboarding |
| Feedback and Rating System | This feature allows customers to rate and review drivers after order completion. Drivers can respond to feedback. Includes rating display, review management, and feedback statistics. | 9 | `https://gitlab.com/giaohang/project/-/issues/9` | Closed | Development Team | 25/10/2024 | 30/10/2024 | iter1 | WP, 3_Done | Feedback |
| Revenue Management System | This feature allows drivers to view their earnings, transaction history, revenue statistics, and request withdrawals. Includes revenue dashboard, charts, and withdrawal request flow. | 10 | `https://gitlab.com/giaohang/project/-/issues/10` | Closed | Development Team | 05/11/2024 | 10/11/2024 | iter2 | WP, 3_Done | Revenue Management |
| Order Status Update Flow | This feature allows drivers to update order status through sequence: Accepted → PickedUp → Delivering → Delivered. Each status change triggers payment processing (if applicable) and notifies customer via Socket.IO. | 11 | `https://gitlab.com/giaohang/project/-/issues/11` | Closed | Development Team | 15/11/2024 | 20/11/2024 | iter2 | WP, 3_Done | Order Status |
| Admin Dashboard | This screen provides admin with system overview including statistics (total users, orders, revenue), charts, and quick access to management functions (accounts, drivers, orders, revenue, reports). | 12 | `https://gitlab.com/giaohang/project/-/issues/12` | Closed | Development Team | 30/11/2024 | 05/12/2024 | iter2 | WP, 3_Done | Admin Dashboard |
| Admin Driver Application Review | This screen allows admin to view driver registration applications, review documents, approve or reject applications with reason, and update user role to Driver upon approval. | 13 | `https://gitlab.com/giaohang/project/-/issues/13` | Closed | Development Team | 10/10/2024 | 15/10/2024 | iter1 | WP, 3_Done | Driver Application Review |
| Admin Withdrawal Management | This screen allows admin to view driver withdrawal requests, review bank account details, approve/reject/complete withdrawal requests, and track withdrawal statistics. | 14 | `https://gitlab.com/giaohang/project/-/issues/14` | Closed | Development Team | 05/11/2024 | 10/11/2024 | iter2 | WP, 3_Done | Withdrawal Management |
| AI Chat Assistant | This feature provides an AI-powered chat assistant using Gemini API. Users can ask questions about services, pricing, how to use the system, and get instant responses. Available on all pages via floating chat button. | 15 | `https://gitlab.com/giaohang/project/-/issues/15` | Closed | Development Team | 20/11/2024 | 25/11/2024 | iter2 | WP, 3_Done | AI Chat |

---

## Summary Statistics

| Category | Count |
|----------|-------|
| **Total Issues** | 15 |
| **Work Packages (WP)** | 15 |
| **Tasks** | 0 |
| **Defects** | 0 |
| **Closed Issues** | 15 |
| **Open Issues** | 0 |

### By Milestone

| Milestone | Issues Count |
|-----------|--------------|
| iter1 | 9 |
| iter2 | 6 |

### By Function/Screen

| Function/Screen | Issues Count |
|-------------------|--------------|
| User Login | 1 |
| User Registration | 1 |
| Order Creation | 1 |
| Driver Orders | 1 |
| Order Acceptance | 1 |
| Order Tracking | 1 |
| Payment | 1 |
| Driver Onboarding | 1 |
| Feedback | 1 |
| Revenue Management | 1 |
| Order Status | 1 |
| Admin Dashboard | 1 |
| Driver Application Review | 1 |
| Withdrawal Management | 1 |
| AI Chat | 1 |

---

**Document Version:** 1.0  
**Last Updated:** December 2024  
**Prepared by:** Development Team  
**Reviewed by:** Project Manager

