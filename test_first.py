import requests
import unittest
import xmltodict

class TestGetIssue(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://codespace-api.myjetbrains.com/youtrack/rest'
        self.creds = ('root', 'c11desp@ce') 
        
    def test_get_issue(self):
        id = 'API-1'
        url = self.base_url + '/issue/' + 'API-1'
        response = requests.get(url, auth=self.creds)
        
        #print response.text
        response_dict = xmltodict.parse(response.text)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response_dict['issue']['@id'], id)
        
        def test_get_issue_invalid_id(self):
            url = self.base_url + '/issue/' + 'ZZZZZZZ'
            r = requests.get(url, auth=self.creds)
            #self.assertEquals()
            
        
if __name__ == '__main__':
    unittest.main()
            
        





#r = requests.get('http://marsweather.ingenology.com/v1/latest/')
#print r.text
#print r.content