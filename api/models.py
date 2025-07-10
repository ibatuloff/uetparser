from pydantic import BaseModel, Field
from typing import List, Tuple, Literal, Optional, Union, Any


def create_pydantic_model(target_cols: Tuple[str]) -> type[BaseModel]:
    class ProductAttributeValid(BaseModel):
        value: Literal[target_cols] = Field(..., description="Корректное название атрибута")
        status: Literal['valid']
    
    class ProductAttributePredict(BaseModel):
        value: Literal[target_cols] = Field(..., description="Наиболее вероятное название атрибута")
        status: Literal['predict']
        explanation: str = Field(..., description="Почему выбрано именно это значение атрибута")

    class ProductAttributeRaw(BaseModel):
        value: str = Field(..., description="Произвольное значение атрибута")
        status: Literal['raw']
        explanation: str = Field(..., description="Почему сохранено исходное значение атрибута")

    ProductAttribute = Union[ProductAttributeValid, ProductAttributePredict, ProductAttributeRaw]

    class ProductAttributeEntryAnnotated(BaseModel):
        attribute: ProductAttribute = Field(..., description="Название атрибута с аннотацией")
        value: Union[str, int, float] = Field(..., description="Значение атрибута")

    class ProductAttributeListAnnotated(BaseModel):
        entries: List[ProductAttributeEntryAnnotated] = Field(
            [], description="Список атрибутов продукта с аннотированными полями"
        )

    return ProductAttributeEntryAnnotated, ProductAttributeListAnnotated
