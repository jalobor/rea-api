from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "OK",
        "mensaje": "API desplegada correctamente"
    }

@app.get("/hello")
def hello():
    return {
        "respuesta": "Hola desde Render"
    }
