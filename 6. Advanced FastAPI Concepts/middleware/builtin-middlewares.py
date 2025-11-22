from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware


app = FastAPI()

# 1. Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://my-frontend.com', 'http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['*']
)


# cors se we can allow or disallow requests from different origins (domains)
# by default, browsers block requests from different origins for security reasons.
# but with CORS middleware, we can specify which origins are allowed to access our API.

# allowed_origins: list of websites (origins) allowed to make requests to this API, these can be your own frontends or any trusted third-party websites
# allowed_headers: from the list of allowed_origins which headers are allowed in requests.







# 2. Add GZip Middleware (Compresses responses larger than 1000 bytes)
app.add_middleware(
    GZipMiddleware, 
    minimum_size=1000
)

# 3. Add HTTPS Redirect Middleware (Forces HTTP requests to redirect to HTTPS)
# Note: Only use this if your server actually supports HTTPS, otherwise you'll get connection errors locally.
app.add_middleware(HTTPSRedirectMiddleware)


@app.get("/")
def main():
    return {"message": "I am using CORS, GZip, and HTTPS Redirect all together!"}




