from django.test import TestCase

# Create your tests here.
from django.core.urlresolvers import reverse
"""
./manage.py dumpdata analizer --format=yaml --indent=4 > analizer/fixtures/analizer.yaml
"""
class IndexTests(TestCase):
    fixtures=['analizer']
    def test_index_with_corps(self):
        "combo tests"
        response=self.client.get(reverse("analizer:index"))
        self.assertEqual(response.status_code,200)
        
        pst={"send_button":"pilots","names":"maar dagon"}
        response=self.client.post(reverse("analizer:list"),pst)
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "maar dagon")
        self.assertContains(response, "91094600")
        
        pst={"send_button":"corps"}
        response=self.client.post(reverse("analizer:list"),pst,follow=True)
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "Unsupported:")
        print response.redirect_chain
        
        pst={"send_button":"pilots","names":""}
        response=self.client.post(reverse("analizer:list"),pst)
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "Absent pilots names")
        """
        for i in response.context:
            for y in i:
                print " --",y
            print i
        print response.context["error_message1"],"dddr"
        #print response.context """
        
    def test_pilot_detail(self):
        "pilot detail"
        response=self.client.get(reverse("analizer:pilot_detail",kwargs={"pilot_id":"01"}))
        self.assertEqual(response.status_code,404)
        
        response=self.client.get(reverse("analizer:pilot_detail",kwargs={"pilot_id":"91105801"}))
        self.assertEqual(response.status_code,200)
        #print response
        self.assertContains(response, "Bheskagor")
        
        response=self.client.get(reverse("analizer:pilot_detail",kwargs={"pilot_id":"90376921"}))
        self.assertEqual(response.status_code,200)
        #print response
        self.assertContains(response, "Liza Calm")
        
    def test_corp_detail(self):
        response=self.client.get(reverse("analizer:corp_detail",kwargs={"corp_id":"01"}))
        self.assertContains(response, "Unsupported:")