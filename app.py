'''
The main application to run
'''

import os
from server import app
#run the app if it wasn't just imported
if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = os.environ.get("DEBUG")
    )
    