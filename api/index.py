from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os

# Create a minimal FastAPI app for Vercel
app = FastAPI()

# Health check endpoint
@app.get("/api/health")
def health_check():
    return JSONResponse(
        status_code=200,
        content={"status": "healthy"}
    )

# Proxy endpoint for your actual API
@app.get("/api/{path:path}")
@app.post("/api/{path:path}")
@app.put("/api/{path:path}")
@app.delete("/api/{path:path}")
async def api_proxy(path: str):
    # In a real implementation, you would forward this to your actual API
    # This is a placeholder that returns a simple response
    return JSONResponse(
        status_code=200,
        content={"message": f"API endpoint: {path}"}
    )

# Serve static files
@app.get("/{full_path:path}")
async def serve_static(full_path: str):
    # This function handles all other routes and serves static files
    file_path = os.path.join("www", full_path or "index.html")
    
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return StaticFiles(directory="www", html=True)
    else:
        # Fallback to index.html for client-side routing
        return StaticFiles(directory="www", html=True)

# Export the app for Vercel
handler = app 