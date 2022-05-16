## Task description 🍪

      - Django model with fields (name, description, price).
      - GET /buy/{id}, which can be used to get Stripe Session Id to pay for the selected Item. Then the request stripe.checkout.Session.create(...) is executed and the         received session.id
      - GET /item/{id} to get HTML page with information about selected Item and Buy button. 
        Request /buy/{id}, get session_id, then redirect to Checkout form stripe.redirectToCheckout(sessionId=session_id)
***
Use ` docker compose up -d` or:

Create a virtual environment
>python -m venv env

Activate the venv
>env\scripts\activate.bat

Open the project folder
>cd project

Install all modules
>pip install -r requirements.txt

Starting the server
>python manage.py runserver

You can initiate a request by going to http://127.0.0.1:8000/
![image](https://user-images.githubusercontent.com/101140452/168677314-3e5e673b-42ce-413e-bd84-8b717b22dfed.png)
***
## API 🍪

***
   

