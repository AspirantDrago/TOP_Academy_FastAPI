from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/filial/{filialId}/groups")
async def get_groups(filialId: int):
    groups = [
        'П31',
        'П41',
        '1414',
        '1416',
        '1412',
        'P41',
        '33B'
    ]
    return {
        'groups': sorted(groups)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
