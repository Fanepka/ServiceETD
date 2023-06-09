from api.routers.addresses import router as router_address
from api.routers.companies import router as router_company
from api.routers.executer import router as router_executer
from api.routers.requests import router as router_request
from api.routers.systems import router as router_system
from api.routers.types import router as router_type
from api.routers.users import router as router_user


rts = [
    router_address, router_company, 
    router_executer, router_request, 
    router_system, router_type, router_user
    ]