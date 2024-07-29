from typing import Any
from fastapi import status
from fastapi.responses import JSONResponse

from schemas.response_scheme import SuccessResponse, ErrorResponse, Message


class ResponseService:
    @staticmethod
    async def response(response: Any) -> Any:
        try:
            response_result = await response

            return SuccessResponse(detail=response_result, status="ok")

        except Exception as error_detail:

            error_response = ErrorResponse(
                detail=Message(message=str(error_detail)), status="error"
            )

            return JSONResponse(
                content=error_response.model_dump(),
                status_code=status.HTTP_400_BAD_REQUEST,
            )
