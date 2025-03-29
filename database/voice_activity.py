from database.connection import get_database
from datetime import datetime, timezone

async def register_entry(user_id: int, guild_id: int):
    db = await get_database()
    time_management = db["timemanagement"]
    

    await time_management.insert_one({
        "user_id": user_id,
        "guild_id": guild_id,
        "entry_time": datetime.now(timezone.utc)
    })

async def register_exit(user_id: int, guild_id: int):
    db = await get_database()
    time_management = db["timemanagement"]
    record = db["records"]

    deleted_document = await time_management.findOneAndDelete({"user_id": user_id, "guild_id": guild_id})

    exit_time = datetime.datetime.utcnow()
    duration = (exit_time - deleted_document.entry_time).total_seconds()

    exists = await record.findOne({"user_id": user_id, "guild_id": guild_id})
    if exists:
        await record.updateOne({"user_id": user_id, "guild_id": guild_id}, {"$inc": {"duration": duration}})
        return
    
    await record.insertOne({{"user_id": user_id, "guild_id": guild_id, "duration": duration}})