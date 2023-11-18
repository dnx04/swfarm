import os

# import validators.volgactf

CONFIG = {
    "DEBUG": os.getenv("DEBUG") == "1",
    "TEAMS": {f"Team #{i}": f"10.{32 + i // 200}.{i % 200}.2" for i in range(0, 256)},
    "FLAG_FORMAT": r"SAAR\{[A-Za-z0-9-_]{32}\}",
    # 'SYSTEM_PROTOCOL': 'ructf_http',
    # 'SYSTEM_URL': 'http://monitor.ructfe.org/flags',
    # 'SYSTEM_TOKEN': '275_17fc104dd58d429ec11b4a5e82041cd2',
    "SYSTEM_HOST": "10.32.250.2",
    "SYSTEM_PORT": "31337",
    "SYSTEM_PROTOCOL": "saarctf",
    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    "SUBMIT_FLAG_LIMIT": 100,
    "SUBMIT_PERIOD": 2,
    "FLAG_LIFETIME": 10 * 60,
    # VOLGA: Don't make more than INFO_FLAG_LIMIT requests to get flag info,
    # usually should be more than SUBMIT_FLAG_LIMIT
    # 'INFO_FLAG_LIMIT': 10,
    # Password for the web interface. This key will be excluded from config
    # before sending it to farm clients.
    # ########## DO NOT FORGET TO CHANGE IT ##########
    "SERVER_PASSWORD": "998244353",
    # For all time-related operations
    "TIMEZONE": "Europe/Moscow",
}
