from django.test import TestCase

# Create your tests here.
from django.core.urlresolvers import reverse

class IndexTests(TestCase):
    def test_index_with_corps(self):
        response=self.client.get(reverse("analizer:index"))
        self.assertEqual(response.status_code,200)
        pst={"send_button":"pilots","names":"maar dagon"}
        response=self.client.post(reverse("analizer:list"),pst)
        self.assertEqual(response.status_code,200)
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