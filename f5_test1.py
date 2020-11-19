import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/aasthana/Documents/tool/chromedriver')

    def test_image_in_herokuapp(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/dynamic_content")
        images = driver.find_elements_by_tag_name('img')
        for image in images:
            self.assertNotEqual(image.get_attribute('src') ,'https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg')
    
    
    def test_search_in_herokuapp(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/dynamic_content")
        content=driver.find_elements_by_xpath('//*[@id="content"]/div/div[2]')
        for element in content:
            parsed_text=element.text
            parsed_word_list=str.split(parsed_text,' ')
            index=0
            maxlen=0
            max_word=''
            while (index < len(parsed_word_list)):
                if len(parsed_word_list[index]) >maxlen:
                    maxlen=len(parsed_word_list[index])
                    max_word=parsed_word_list[index]
                index=index+1
            print(max_word)
            self.assertFalse(len(max_word)>10,msg='Text has all words smaller than 10')
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()