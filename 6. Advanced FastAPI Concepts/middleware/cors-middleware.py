

# cors se we can allow or disallow requests from different origins (domains)
# by default, browsers block requests from different origins for security reasons.
# but with CORS middleware, we can specify which origins are allowed to access our API.




from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://my-frontend.com', 'http://localhost:3000'
    ],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['*']
)


# define endpoints





