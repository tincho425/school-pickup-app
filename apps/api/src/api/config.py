import os

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql+asyncpg://app:app@localhost:5432/school_pickup")

DATABASE_URL_SYNC = os.environ.get("DATABASE_URL_SYNC", "postgresql://app:app@localhost:5432/school_pickup")