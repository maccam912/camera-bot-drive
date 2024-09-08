from litestar import Litestar, get
from litestar.static_files import create_static_files_router
import httpx

async def forward_request(direction: str):
    async with httpx.AsyncClient() as client:
        external_api_url = "http://192.168.68.61:5000"
        response = await client.request(
            method="GET",
            url=f"{external_api_url}/control?direction={direction}",
            headers={"Content-Type": "application/json"},
        )
        return response.content, response.status_code, response.headers

@get("/control")
async def control(direction: str) -> None:
    await forward_request(direction)

app = Litestar(
    route_handlers=[
        create_static_files_router(
            path="/",
            directories=["html"],
            html_mode=True,
        ),
        control
    ],
)