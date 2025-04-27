import os
import sys
from fastapi import FastAPI
from presentation.controllers.ai_controller import router as AIController
from presentation.controllers.auth_controller import router as AuthController

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def error_handlers(app):
    pass

def create_app():
    app = FastAPI()
    app.include_router(AIController, prefix="/api")
    app.include_router(AuthController, prefix="/api")

    return app
