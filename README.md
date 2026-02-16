# Playwright Automation Project: Alza.cz Critical Path

This repository contains automated E-commerce tests for the **Alza.cz** website (Czech Republic's leading retailer). The project focuses on the critical path: searching for products and verifying the shopping cart flow.

## 🛠 Tech Stack
* **Language:** Python 3.13
* **Framework:** Pytest
* **Automation Library:** Playwright
* **Reporting:** Screenshots & Terminal Verbose Logs

## 🚀 Key Features & Solved Challenges
* **Dynamic Data (Parametrization):** Tests run for multiple products (iPhone 15, Samsung Galaxy S24) using a single test function.
* **Smart Modal Handling:** Implemented logic to handle Alza's specific "Upsell/Service" modals and cookie banners.
* **Stability Fixes:** Used robust locators (`get_by_text`) and auto-waiting mechanisms to prevent flaky results.
* **Clean Architecture:** Professional `.gitignore` setup and organized screenshot reporting.

## 📦 Installation & Setup
1. Clone the repo:
   ```bash
   git clone [https://github.com/nikita-polovnoy/alza-smoke-test-playwright.git](https://github.com/nikita-polovnoy/alza-smoke-test-playwright.git)