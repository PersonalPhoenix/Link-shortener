from django.test import TestCase
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPage(TestCase):

    def test_check_page_available(self):
        '''
        Проверяем доступна ли страница
        '''

        responce = self.client.get('')
        self.assertEqual(responce.status_code, 200)
    
    def check_correct_text_in_page(self):
        '''
        Проверяем корректно ли контент
        отображается на странице
        '''

        responce = self.client.get('')
        self.assertIn('Enter Your Long URL', responce.content.decode())
        self.assertIn('Your shorten URL', responce.content.decode())
        self.assertIn('Shortened It', responce.content.decode())

    def check_element_exist(self):
        '''
        Проверяем существование ожидаемых 
        элементов на странице
        '''

        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        search_fild_input = driver.find_element(By.ID, 'link')
        search_fild_input = driver.find_element(By.ID, 'getting')
        search_fild_button = driver.find_element(By.TAG_NAME, 'button')
        driver.quit()