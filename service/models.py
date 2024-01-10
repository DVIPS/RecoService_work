import typing as tp

from pydantic import BaseModel

from service.config import popular_recomendations


class Top_popular:
    def __init__(self) -> None:
        self.recomends = popular_recomendations

    def recomend(self) -> tp.List[int]:
        return self.recomends


class Error(BaseModel):
    error_key: str
    error_message: str
    error_loc: tp.Optional[tp.Any] = None
