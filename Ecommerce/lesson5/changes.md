* views.py
```python
def contact_page(request):
	context = {
		"title":"Contact Page",
		"content":"Welcome to the contact page"
	}
	if request.method=='POST':
		print (request.POST)
		print (request.POST.get('fullname'))
		print (request.POST.get('email'))
		print (request.POST.get('content'))
	return render(request, "contact/view.html", context)
```
---
* In [templates] -> [contact] -> ```view.html```
* view.html: duplicate from ```home_page.html``` with changes:
```html
<p>{{content}}</p>
<div class='col-sm-6 col-12'>
    <form method='POST'> {% csrf_token %} <!-- Send data to back end -->
        <input type='text' class='form-control' placeholder="Name" name='fullname'>
        <input type='email' class='form-control' placeholder="Email" name='email'>
        <textarea class='form-control' placeholder="Your Content" name ='content'></textarea> 
        <button type='submit' class='btn btn-default'>Submit</button>
    </form>
</div>
```
