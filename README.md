# 🛒 E-commerce Smoke Test (Alza.cz)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/framework-Playwright-green.svg)](https://playwright.dev/python/)

## 📝 Project Overview
This repository contains an automated **Smoke Test** for the Czech e-commerce giant **Alza.cz**. 
The automation focuses on the **Critical Path** — the most essential sequence of steps a user takes to generate revenue for the business.

### Why this test?
In a real-world scenario, if a user cannot search for a product or add it to the basket, the business loses money immediately. This test ensures that the core components (Search engine, Product Grid, and Shopping Cart) are functioning correctly.

---

## 🚀 Scenarios Covered
- **Navigation**: Loading the homepage and handling localized cookie consent.
- **Search Logic**: Finding a specific product (e.g., "iPhone 15").
- **Cart Management**: Adding the first available item to the basket.
- **Verification**: Asserting that the product is present in the cart.
- **Visual Proof**: Automated screenshot generation on test completion.

---

## 🛠️ Technical Stack
* **Language**: Python 3.13+
* **Testing Framework**: `pytest`
* **Automation Library**: `Playwright`
* **Reporting**: Automated screenshots for manual verification.

---

## ⚙️ Installation & Execution

1. **Clone the repository**:
   ```bash
   git clone <your-repo-link>
   cd alza-test