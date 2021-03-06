import unittest
import requests
import xmltodict

from yaml import load

class BaseApi(unittest.TestCase):
    def setUp(self):
        self.settings = load(open('settings.yaml').read())
        self.base_url = self.settings['base_url']
        
        self.cookies = self._login()
        
    def _login(self):
        url = self.base_url + '/user/login'
        
        params = {
        'login': self.settings['credentials']['login'],
        'password': self.settings['credentials']['password']
        }
        
        r = requests.post(url, data=params)
        return r.cookies
        
    def create_issue(self):
        url = self.base_url + '/issue'
        params = {
        'project': 'api',
        'summary': 'Generated by robots',
        'description': 'Hail the robots!'
        }
        r = requests.put(url, data=params, cookies=self.cookies)
        self.assertEquals(r.status_code, 201)
        
        issue_id = r.headers['location'].split('/')[-1]
        
        url = self.base_url + '/issue/' + issue_id
        r = requests.get(url, cookies=self.cookies)
        self.assertEquals(r.status_code, 200)
        return issue_id
        
    #def request(self, method):
    #    return getattr(request, method)(url, params, cookies=self.cookies)
    
    def request(self, url, method, params=None):
        return getattr(requests, method)(url, data=params, cookies=self.cookies)