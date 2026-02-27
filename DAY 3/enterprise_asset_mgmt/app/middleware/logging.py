import time
from fastapi import Request

async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Path: {request.url.path} | Method: {request.method} | Duration: {process_time:.4f}s")
    return response