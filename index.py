import uvicorn
from main import app
if "__main__" == __name__:
    uvicorn.run(app=app, debug=False, host="0.0.0.0", port=3000)