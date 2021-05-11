from django.test import SimpleTestCase
from django.urls import reverse,resolve
from web_app.views import patientprofile,patientprofilerequest,doctorprofile,pres

class TestUrls(SimpleTestCase):
  
    def test_list_url_is_resolved(self):
        url = reverse(('patientprofile'))
        print(resolve(url))
        self.assertEquals(resolve(url).func,patientprofile)

    def test_list_url_is_resolved(self):
        url = reverse(('patientprofilerequest'))
        print(resolve(url))
        self.assertEquals(resolve(url).func,patientprofilerequest)

    def test_list_url_is_resolved(self):
        url = reverse(('doctorprofile'))
        print(resolve(url))
        self.assertEquals(resolve(url).func,doctorprofile)
        
    def test_list_url_is_resolved(self):
        url = reverse(('pres'))
        print(resolve(url))
        self.assertEquals(resolve(url).func,pres)
