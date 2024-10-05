from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.temperature import crud, schemas
from app.city import crud as city_crud
from app.dependencies import get_db
from app.temperature.helpers import fetch_temperature

temperature_router = APIRouter()


@temperature_router.post("/update")
async def update_temperatures(db: Session = Depends(get_db)):
    cities = city_crud.get_cities(db)
    for city in cities:
        temperature = fetch_temperature(city.name)
        crud.create_temperature(db, schemas.TemperatureCreate(city_id=city.id, temperature=temperature))
    return {"ok": True}


@temperature_router.get("/", response_model=list[schemas.TemperatureRead])
def read_temperatures(db: Session = Depends(get_db)):
    return crud.get_temperatures(db)
