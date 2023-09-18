# Sandbox project

The main goal is to increase my level in deployment and CD if possible (allowed by the host).  

The app itself is a form of to-do list that you can use by signing up.  

Of course, the administrator can create a team and its members have an inbox functionality to exchange.

## Memo

We have to comment this lines before the first migration:  
in   
```py
app/vmc/forms.py

class ThreadForm:
    ...

    class Meta:
        ...
        
        EMAIL_CHOICES = [(user.email, user.email) for user in staff_users]
        if EMAIL_CHOICES:
            widgets = {
                "email_choices": forms.SelectMultiple(choices=EMAIL_CHOICES),
            }
```