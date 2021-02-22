from uuid import UUID

def is_uuid_valid(uuid_v, ver=4):
    try:
        obj = UUID(uuid_v, ver)
    except ValueError:
        return False
    return str(obj) == uuid_v
