from selenium import webdriver


def test_initial_start():
    browser = webdriver.Chrome()
    browser.get('http://localhost:8000')
    assert 'Congratulations' in browser.title
