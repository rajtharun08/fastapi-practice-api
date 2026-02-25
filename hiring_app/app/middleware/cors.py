from fastapi.middleware.cors import CORSMiddleware

def cors_add(app):
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],              
    allow_headers=["*" ]
    )   