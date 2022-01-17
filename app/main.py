from fastapi import FastAPI


app = FastAPI()

@app.get("/all")
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
            }
        }
    }

