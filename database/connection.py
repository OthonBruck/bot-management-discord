import motor.motor_asyncio
from decouple import config

MONGO_URI = config("DATABASE_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[config("DATABASE_NAME")]

async def get_database():
    return db