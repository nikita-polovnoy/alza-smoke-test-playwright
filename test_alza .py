from playwright.sync_api import Page, expect
import pytest

def test_alza_shopping_cart_flow(page: Page):
    """
    Test Case: Verify the Critical Path for adding an item to the shopping cart.
    """
    # 1. Navigate to the website
    page.goto("https://www.alza.cz/", wait_until="domcontentloaded")

    # Handle Cookie Consent Dialog
    cookie_button = page.get_by_role("button", name="Rozumím")
    if cookie_button.is_visible():
        cookie_button.click()

    # 2. Search for a product
    search_input = page.get_by_placeholder("Co hledáte?")
    search_input.fill("iPhone 15")
    page.get_by_test_id("button-search").click()

    # 3. Add the first product to the cart
    # Selecting the first 'Buy' button from the results list
    buy_button = page.locator(".btnk1").first
    buy_button.click()

    # Wait for the modal/animation to stabilize
    page.wait_for_load_state("networkidle")

    # 4. Navigate to the shopping cart
    page.get_by_test_id("headerBasketIcon").click()

    # 5. Assertions: Verify the product is visible in the cart
    cart_item = page.locator(".mainItem")
    
    # Capture proof for the test report
    page.screenshot(path="basket_result.png")
    
    # Assert with an extended timeout for heavy dynamic content
    expect(cart_item).to_be_visible(timeout=10000)
    
    print("\n[SUCCESS] E-commerce Critical Path verified.")