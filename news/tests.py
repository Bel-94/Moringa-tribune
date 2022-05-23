from django.test import TestCase
from .models import Editor, Article, tags

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.bel= Editor(first_name = 'Belinda', last_name ='Ntinyari', email ='belinda@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.bel,Editor))

     # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)