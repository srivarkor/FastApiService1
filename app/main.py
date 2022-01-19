from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/events/all")
async def all_events():
    return {
        "events":{
            "enagement":{
                "eventname":"engagement",
                "fromtime":"210120222330",
                "venuelat":"28.0235",
                "venuelong":"52.214"
            },
            "reception":{
                "eventname":"reception",
                "fromtime":"310120222330",
                "venuelat":"28.0235",
                "venuelong":"52.214"
            },
            "bachelorparty":{
                "eventname":"bachelorparty",
                "fromtime":"260120222230",
                "venuelat":"30.075",
                "venuelong":"54.824"
            },
            "poolparty":{
                "eventname":"poolparty",
                "fromtime":"280120222230",
                "venuelat":"80.075",
                "venuelong":"94.824"
            }
        }
    }

