# -*- coding: utf-8 -*-
from time import sleep

from django.core.management import BaseCommand

from app.app_settings import BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD
from app.models import *
from selenium import webdriver

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

base_url = BASE_URL
login_url = base_url + '/login'
profile_url = base_url + '/profile/{}'


class Command(BaseCommand):

    def handle(self, *args, **options):

        try:
            driver = webdriver.PhantomJS(service_args=['--web-security=false', '--debug=true'],
                                         executable_path='/usr/local/bin/phantomjs')
            driver.get(login_url)
            username = driver.find_element_by_id("id_username")
            username.send_keys(ADMIN_USERNAME)
            password = driver.find_element_by_name("password")
            password.send_keys(ADMIN_PASSWORD)
            driver.find_element_by_name("submit").click()

            while True:
                users = User.objects.all()
                for user in users:
                    try:
                        driver.get(profile_url.format(user.id))
                        # print(driver.page_source.encode('utf-8'))
                        print('[+] visited "{}" profile.'.format(user.username))
                    except:
                        pass

                sleep(10)
        except:
            sleep(10)

