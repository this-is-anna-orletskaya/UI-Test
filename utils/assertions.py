




class Assertions:

    @staticmethod
    def get_current_url(driver):
        now_url = driver.current_url
        print("Текущая URL: " + now_url)

    @staticmethod
    def assert_url(driver, expected_url: str):
        now_url = driver.current_url
        assert now_url == expected_url
        print("Проверка URL выполнена.")
    
    @staticmethod
    def check_word(word, expected_word: str):
        value_word = word.text 
        assert value_word == expected_word 
        print("Проверка по слову выполнена.")
