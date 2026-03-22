from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .api_client import fetch_all_characters
from .filters import filter_characters

app = FastAPI()

# ---------------------------
#       CACHE
# ---------------------------

cached_characters = None


# ---------------------------
#       API ENDPOINTS
# ---------------------------

@app.get("/healthcheck", response_class=HTMLResponse)
def healthcheck():
    html = """
    <html>
    <head>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', sans-serif;
                background: radial-gradient(circle at top, #1e293b, #020617);
                color: #e5e7eb;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .card {
                background: rgba(15, 23, 42, 0.85);
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                width: 400px;
                box-shadow: 0 20px 50px rgba(0,0,0,0.6);
                animation: fadeIn 0.8s ease-out;
                border: 1px solid rgba(148,163,184,0.3);
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }

            h1 {
                margin-bottom: 10px;
            }

            p {
                color: #9ca3af;
                margin-bottom: 20px;
            }

            .btn {
                padding: 12px 20px;
                background: #6366f1;
                border-radius: 10px;
                color: white;
                cursor: pointer;
                border: none;
                font-weight: 600;
                transition: 0.15s ease-out;
                margin: 5px;
            }

            .btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 30px rgba(99,102,241,0.5);
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>Healthcheck</h1>
            <p>Status: <strong style="color:#22c55e;">OK</strong></p>
            <button class="btn" onclick="window.location.href='/'">Back to Home</button>
            <button class="btn" onclick="window.location.href='/ui/docs'">Go to Docs</button>
        </div>
    </body>
    </html>
    """
    return html


@app.get("/characters")
def get_characters():
    global cached_characters

    if cached_characters is None:
        characters = fetch_all_characters()
        filtered = filter_characters(characters)

        priority = ["Rick Sanchez", "Morty Smith"]
        sorted_chars = sorted(
            filtered,
            key=lambda c: (c["name"] not in priority, c["name"])
        )

        cached_characters = sorted_chars[:20]

    return cached_characters


# ---------------------------
#       HOME PAGE
# ---------------------------

@app.get("/", response_class=HTMLResponse)
def homepage():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Rick & Morty API Showcase</title>

        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', sans-serif;
                background: radial-gradient(circle at top, #1e293b, #020617);
                color: #e5e7eb;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .container {
                text-align: center;
                padding: 40px;
                background: rgba(15, 23, 42, 0.85);
                border-radius: 20px;
                width: 600px;
                box-shadow: 0 20px 50px rgba(0,0,0,0.6);
                animation: fadeIn 0.8s ease-out;
                border: 1px solid rgba(148,163,184,0.3);
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }

            h1 {
                font-size: 32px;
                margin-bottom: 10px;
            }

            p {
                font-size: 14px;
                color: #9ca3af;
                margin-bottom: 30px;
            }

            .btn {
                display: block;
                width: 100%;
                padding: 14px;
                margin: 10px 0;
                border-radius: 12px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                border: none;
                color: white;
                background: linear-gradient(135deg, #38bdf8, #6366f1);
                box-shadow: 0 10px 30px rgba(56, 189, 248, 0.4);
                transition: 0.15s ease-out;
            }

            .btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 16px 40px rgba(56, 189, 248, 0.6);
            }

            .footer {
                margin-top: 25px;
                font-size: 12px;
                color: #6b7280;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Rick & Morty API Showcase</h1>
            <p>FastAPI backend · Modern UI · External API integration.</p>

            <button class="btn" onclick="window.location.href='/ui/characters'">
                View Characters
            </button>

            <button class="btn" onclick="window.location.href='/ui/docs'">
                API Documentation
            </button>

            <button class="btn" onclick="window.location.href='/healthcheck'">
                Healthcheck
            </button>

            <div class="footer">
                Built for portfolio presentation
            </div>
        </div>
    </body>
    </html>
    """
    return html


# ---------------------------
#   CHARACTERS UI PAGE
# ---------------------------

@app.get("/ui/characters", response_class=HTMLResponse)
def characters_ui():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Characters</title>

        <style>
            body {
                margin: 0;
                padding: 20px;
                font-family: 'Segoe UI', sans-serif;
                background: radial-gradient(circle at top, #1e293b, #020617);
                color: #e5e7eb;
            }

            h1 {
                text-align: center;
                margin-bottom: 20px;
            }

            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
                gap: 20px;
                padding: 20px;
            }

            .card {
                background: rgba(15, 23, 42, 0.9);
                border-radius: 16px;
                padding: 12px;
                text-align: center;
                border: 1px solid rgba(148,163,184,0.3);
                transition: 0.15s ease-out;
            }

            .card:hover {
                transform: translateY(-4px);
                border-color: #38bdf8;
            }

            img {
                width: 100%;
                border-radius: 12px;
            }

            .name {
                margin-top: 10px;
                font-size: 16px;
                font-weight: 600;
            }

            .location {
                font-size: 12px;
                color: #9ca3af;
            }

            .back-btn {
                display: block;
                margin: 0 auto;
                margin-top: 20px;
                padding: 10px 20px;
                background: #6366f1;
                border-radius: 10px;
                color: white;
                cursor: pointer;
                border: none;
                font-weight: 600;
            }
        </style>
    </head>

    <body>
        <h1>Top 20 Characters</h1>

        <div id="grid" class="grid"></div>

        <button class="back-btn" onclick="window.location.href='/'">Back to Home</button>

        <script>
            async function load() {
                const res = await fetch("/characters");
                const data = await res.json();

                const grid = document.getElementById("grid");

                data.forEach(c => {
                    const card = document.createElement("div");
                    card.className = "card";

                    card.innerHTML = `
                        <img src="${c.image}" alt="${c.name}">
                        <div class="name">${c.name}</div>
                        <div class="location">${c.location}</div>
                    `;

                    grid.appendChild(card);
                });
            }

            load();
        </script>
    </body>
    </html>
    """
    return html


# ---------------------------
#   DOCS UI PAGE
# ---------------------------

@app.get("/ui/docs", response_class=HTMLResponse)
def docs_ui():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>API Docs</title>

        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', sans-serif;
                background: radial-gradient(circle at top, #1e293b, #020617);
                color: #e5e7eb;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .card {
                background: rgba(15, 23, 42, 0.85);
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                width: 450px;
                box-shadow: 0 20px 50px rgba(0,0,0,0.6);
                animation: fadeIn 0.8s ease-out;
                border: 1px solid rgba(148,163,184,0.3);
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }

            h1 {
                margin-bottom: 10px;
            }

            p {
                color: #9ca3af;
                margin-bottom: 20px;
                font-size: 14px;
            }

            .btn {
                padding: 12px 20px;
                background: #6366f1;
                border-radius: 10px;
                color: white;
                cursor: pointer;
                border: none;
                font-weight: 600;
                transition: 0.15s ease-out;
                margin: 5px;
            }

            .btn.secondary {
                background: #4b5563;
            }

            .btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 30px rgba(99,102,241,0.5);
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>API Documentation</h1>
            <p>Interactive Swagger UI is available. Use it to explore and test the API endpoints.</p>

            <button class="btn" onclick="window.location.href='/docs'">
                Open Swagger Docs
            </button>

            <button class="btn secondary" onclick="window.location.href='/'">
                Back to Home
            </button>
        </div>
    </body>
    </html>
    """
    return html

@app.get("/health")
def health_check():
    return {"status": "ok"}