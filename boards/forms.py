from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea(), max_length=4000)

	class Meta:
		model = Topic
		fields = ['subject', 'message']

# this is a Modelform associated with the topic model