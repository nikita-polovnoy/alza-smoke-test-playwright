from playwright.sync_api import Page, expect
import pytest
import os

@pytest.mark.parametrize("item", ["iPhone 15", "Samsung Galaxy S24"])
def test_alza_shopping_cart_flow(page: Page, item: str):
    # 1. Navigate
    page.goto("https://www.alza.cz/", wait_until="domcontentloaded")

    # Cookie handle
    cookie_button = page.get_by_role("button", name="Rozumím")
    if cookie_button.is_visible():
        cookie_button.click()

    # 2. Search
    search_input = page.get_by_placeholder("Co hledáte?")
    search_input.fill(item)
    page.get_by_test_id("button-search").click()

    # 3. Add to cart
    buy_button = page.locator(".btnk1").first
    buy_button.wait_for(state="visible", timeout=7000)
    buy_button.click()

    # --- ВОТ ЭТОТ БЛОК НУЖНО ДОБАВИТЬ ОБЯЗАТЕЛЬНО ---
    
    # ПРАВКА №1: Если вылезло окно услуг (страховка), жмем "Продолжить"
    # Это специфично для Samsung и дорогих товаров
    continue_button = page.get_by_text("Pokračovat", exact=True)
    try:
        # Ждем немного, появится ли кнопка подтверждения
        if continue_button.is_visible(timeout=3000):
            continue_button.click()
    except:
        # Если кнопки нет (как у iPhone), просто идем дальше
        page.keyboard.press("Escape")

    # 4. Переход в корзину (ждем, пока счетчик обновится)
    page.wait_for_load_state("networkidle")
    page.get_by_test_id("headerBasketIcon").click(force=True)

    # 5. Проверка (Assertion)
    # Используем селектор, который ищет текст внутри элементов корзины
    expect(page.get_by_text(item).first).to_be_visible(timeout=10000)
    
    # Скриншот для отчета
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    page.screenshot(path=f"screenshots/basket_{item.replace(' ', '_')}.png")