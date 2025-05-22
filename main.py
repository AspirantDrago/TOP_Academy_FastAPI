import asyncio
import datetime

from fastapi import FastAPI
import uvicorn

app = FastAPI()
GROUPS = [
    {
        "id": 1,
        "name": "П31",
    },
    {
        "id": 2,
        "name": "П41",
    },
    {
        "id": 3,
        "name": "1414",
    },
    {
        "id": 4,
        "name": "1416",
    },
    {
        "id": 5,
        "name": "1412",
    },
    {
        "id": 6,
        "name": "P41",
    },
    {
        "id": 7,
        "name": "33B",
    },
]


def get_group(_id: int) -> str | None:
    for group in GROUPS:
        if group["id"] == _id:
            return group["name"]
    return None


DB = {
    'events': [
        {
            'id': 1,
            'groupId': 1,
            'group': get_group(1),
            'auditoryId': 1,
            'auditory': 'Rutube (3 этаж)',
            'date': datetime.date.today(),
            'time': datetime.time.fromisoformat('18:00')
        },
        {
            'id': 2,
            'groupId': 2,
            'group': get_group(2),
            'auditoryId': 2,
            'auditory': 'РПО (3 этаж)',
            'date': datetime.date.today(),
            'time': datetime.time.fromisoformat('18:30')
        },
        {
            'id': 3,
            'groupId': 3,
            'group': get_group(3),
            'auditoryId': 2,
            'auditory': 'РПО (3 этаж)',
            'date': datetime.date.today() - datetime.timedelta(days=1),
            'time': datetime.time.fromisoformat('16:00')
        },
        {
            'id': 1,
            'groupId': 1,
            'group': get_group(1),
            'auditoryId': 2,
            'auditory': 'РПО (3 этаж)',
            'date': datetime.date.today() + datetime.timedelta(days=1),
            'time': datetime.time.fromisoformat('16:00')
        },
    ]
}


@app.get("/filial/{filialId}/groups")
async def get_groups(filialId: int):
    await asyncio.sleep(1)
    return {
        'filialId': filialId,
        'groups': sorted(GROUPS, key=lambda g: g['name']),
    }


@app.get("/filial/{filialId}/groups/{groupId}/date/{date}")
async def get_group(filialId: int, groupId: int, date: datetime.date):
    await asyncio.sleep(1)
    return {
        'filialId': filialId,
        'groupId': groupId,
        'date': date,
        'events': [
            event for event in DB['events']
            if (event['groupId'] == groupId or groupId == 0)
            and event['date'] == date
        ]
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
