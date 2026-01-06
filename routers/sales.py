from fastapi import APIRouter, Query
from schemas.sales import SalesCreate, SalesRead
from crud import sales as sales_crud
from services.prediction import PredictionService
from services.analytics import AnalyticsService

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/", response_model=SalesRead)
def add_sale(sale: SalesCreate):
    return sales_crud.create_sale(sale)

@router.get("/", response_model=list[SalesRead])
def get_sales():
    return sales_crud.get_all_sales()

@router.get("/predict")
def predict_sales(
    window: int = Query(7, ge=1, le=30)
):
    data = sales_crud.get_all_sales()
    service = PredictionService(data)

    prediction = service.moving_average(window)

    return {
        "predicted_quantity": prediction,
        "method": "moving_average",
        "window": window
    }
    
@router.get("/summary")
def sales_summary():
    data = sales_crud.get_all_sales()
    service = AnalyticsService(data)
    return service.summary()

@router.get("/daily")
def daily_analytics():
    data = sales_crud.get_all_sales()
    service = AnalyticsService(data)
    return service.daily_stats()
