* ```views.py```
```python 
from .forms import ContactForm

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title":"Contact Page",
		"content":"Welcome to the contact page",
		"form":contact_form
	}
	# new stuff
	if contact_form.is_valid():
		print (contact_form.cleaned_data)
	
	if request.method=='POST':
		print (request.POST)
		print (request.POST.get('fullname'))
		print (request.POST.get('email'))
		print (request.POST.get('content'))
	return render(request, "contact/view.html", context)
```
---
* ```view.html```
```html
<div class='col-sm-6 col-12'>
    <form method='POST'> {% csrf_token %} <!-- Send data to back end -->
        {{ form }}
        <button type='submit' class='btn btn-default'>Submit</button>
    </form>
</div>
```
---
* In the same folder as ```urls.py``` and ```views.py```, create ```forms.py```
```python 
from django import forms

class ContactForm(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(
							attrs={
								"class":"form-control", 
								"placeholder": "Your Full Name", 
								"id":"form_full_name"
								}
							)
						)
	email = forms.EmailField(widget=forms.EmailInput(
							attrs={
								"class":"form-control", 
								"placeholder": "Your Email", 
								"id":"form_full_name"
								}
							)
						)
	content = forms.CharField(widget=forms.Textarea(
							attrs={"class":"form-control", 
									"placeholder": "Your Content"}))

	# Custom validation
	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("Email has to be gmail")
		return email
 ```
