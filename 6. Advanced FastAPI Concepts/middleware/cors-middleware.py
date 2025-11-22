
# cors se we can allow or disallow requests from different origins (domains)
# by default, browsers block requests from different origins for security reasons.
# but with CORS middleware, we can specify which origins are allowed to access our API.


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://my-frontend.com', 'http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['*']
)



# allowed_origins: list of websites (origins) allowed to make requests to this API
# these can be your own frontends or any trusted third-party websites

# allowed_headers: from the list of allowed_origins which headers are allowed in requests.





# define endpoints







