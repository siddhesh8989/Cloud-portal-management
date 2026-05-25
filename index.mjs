kind = "api"
previewPath = "/"
title = "Cloud Portal"
version = "1.0.0"
id = "3B4_FFSkEVBkAeYMFRJ2e"

[[services]]
localPort = 5000
name = "Cloud Portal"
paths = ["/"]

[services.development]
run = "PORT=5000 python artifacts/cloud-portal/app.py"

[services.env]
PORT = "5000"
