
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse

app = FastAPI()


# HTML Response Example
@app.get('/html', response_class=HTMLResponse)
def get_html():
    return """
    <html>
        <head>
            <title>FastAPI HTML</title>
        </head>
            <title>FastAPI HTML</title>
        </head>
        <body>
            <h1>Hello from FastAPI!</h1>
            <p>This is HTML response</p>
        </body>
    </html>
    """



# Plain Text Response Example
@app.get('/text', response_class=PlainTextResponse)
def get_text():
    return "This is plain text response from FastAPI"



# Redirect Response Example
@app.get('/redirect')
def redirect_to_home():
    return RedirectResponse(url='/', status_code=302)





# File Response Example
from fastapi.responses import FileResponse

@app.get('/download')
def download_file():
    # Using example.txt for download
    file_path = "example.txt"  # File in the same directory
    return FileResponse(path=file_path, filename="downloaded_example.txt", media_type="text/plain")


