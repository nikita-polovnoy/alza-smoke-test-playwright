import google.generativeai as genai

# Твой ключ
API_KEY = "AIzaSyBGqn1aBTBo8UrO1JmttF1FBs8mYAvB7JQ" 
genai.configure(api_key=API_KEY)

def get_ai_analysis(error_message):
    # Используем актуальную версию модели, чтобы избежать ошибки 404
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    prompt = f"""
    Ты — Senior QA Automation Engineer. 
    Проанализируй эту ошибку теста Playwright на сайте Alza.cz:
    
    {error_message}
    
    Дай ответ в 3 пунктах:
    1. Что именно сломалось?
    2. Это баг сайта или проблема в коде теста?
    3. Как это исправить?
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Не удалось получить анализ от ИИ: {e}" 