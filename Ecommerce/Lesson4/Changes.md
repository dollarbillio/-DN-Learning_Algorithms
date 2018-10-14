* views.py
```python
def home_page(request):
    context = {
        "title":"Hello home_page",
        "content": "Welcome to home_page"
    }
    return render (request, "home_page.html",context)
  
def about_page(request):
    context = {
        "title":"Hello About_page",
        "content": "Welcome to the about page"
    }
    return render (request, "home_page.html",context)
    
def contact_page(request):
    context = {
        "title":"Welcome to contact_page",
        "content": Welcome to contact_page
    }
    return render (request, "home_page.html",context)
```
---
* Link "context" "title"
* homepage.html
```html
<body>
    <div class='text-center'>
        <h1>{{ title }}</h1>
        <h1>Hello World! We are working</h1>
    </div>
    <!-- New -->
    <div class='container'>
    <div class='row'>
        <div class='col'>
            <!-- Show content from above -->
            <p>{{ content }}</p>  
        </div>
    </div>
    </div>
```
