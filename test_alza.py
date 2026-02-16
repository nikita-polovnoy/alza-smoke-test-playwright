import pytest
import os
from playwright.sync_api import Page, expect
from pages.alza_page import AlzaPage 
from ai_helper import get_ai_analysis 

@pytest.mark.parametrize("item", ["iPhone 15", "Samsung Galaxy S24"])
def test_alza_shopping_cart_flow(page: Page, item: str):
    alza = AlzaPage(page)
    
    try:
        # 1. Заходим и жмем куки
        alza.navigate()
        if alza.cookie_button.is_visible():
            alza.cookie_button.click()

        # 2. Ищем товар
        alza.search_for(item)

        # 3. Добавляем в корзину и обрабатываем страховку
        alza.add_to_cart()
        
        try:
            if alza.continue_button.is_visible(timeout=3000):
                alza.continue_button.click()
        except:
            page.keyboard.press("Escape")

        # 4. Переходим в корзину
        page.wait_for_load_state("networkidle")
        alza.basket_icon.click(force=True)

        # 5. Проверка и скриншот
        expect(page.get_by_text(item).first).to_be_visible(timeout=10000)
        
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        page.screenshot(path=f"screenshots/basket_{item.replace(' ', '_')}.png")

    except Exception as e:
        print("\n" + "="*50)
        print("🤖 АНАЛИЗ ОШИБКИ ОТ GEMINI:")
        print(get_ai_analysis(str(e)))
        print("="*50)
        raise e 