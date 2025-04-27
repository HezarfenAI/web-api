from presentation.server import create_app
import uvicorn

is_development = True

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
