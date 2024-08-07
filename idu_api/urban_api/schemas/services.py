from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, model_validator

from idu_api.urban_api.dto import ServiceDTO, ServiceWithGeometryDTO, ServiceWithTerritoriesDTO
from idu_api.urban_api.schemas.geometries import Geometry
from idu_api.urban_api.schemas.service_types import ServiceTypes
from idu_api.urban_api.schemas.territories import ShortTerritory, TerritoryType


class ServicesOrderByField(str, Enum):
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"


class ServicesData(BaseModel):
    """Service with all its attributes."""

    service_id: int = Field(example=1)
    service_type: ServiceTypes = Field(
        example={"service_type_id": 1, "urban_function_id": 1, "name": "Школа", "capacity_modeled": 1, "code": "1"}
    )
    territory_type: Optional[TerritoryType] = Field(example={"territory_type_id": 1, "name": "Город"})
    name: Optional[str] = Field(description="Service name", example="--")
    capacity_real: Optional[int] = Field(example=1)
    properties: Dict[str, Any] = Field(
        description="Service additional properties",
        example={"additional_attribute_name": "additional_attribute_value"},
    )
    created_at: datetime = Field(default_factory=datetime.utcnow, description="The time when the territory was created")
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, description="The time when the territory was last updated"
    )

    @classmethod
    def from_dto(cls, dto: ServiceDTO) -> "ServicesData":
        """
        Construct from DTO.
        """
        return cls(
            service_id=dto.service_id,
            service_type=ServiceTypes(
                service_type_id=dto.service_type_id,
                urban_function_id=dto.urban_function_id,
                name=dto.service_type_name,
                capacity_modeled=dto.service_type_capacity_modeled,
                code=dto.service_type_code,
            ),
            territory_type=TerritoryType(territory_type_id=dto.territory_type_id, name=dto.territory_type_name),
            name=dto.name,
            capacity_real=dto.capacity_real,
            properties=dto.properties,
            created_at=dto.created_at,
            updated_at=dto.updated_at,
        )


class ServiceWithTerritories(BaseModel):
    """Service with all its attributes and parent territory."""

    service_id: int = Field(example=1)
    service_type: ServiceTypes = Field(
        example={"service_type_id": 1, "urban_function_id": 1, "name": "Школа", "capacity_modeled": 1, "code": "1"}
    )
    territory_type: Optional[TerritoryType] = Field(example={"territory_type_id": 1, "name": "Город"})
    name: Optional[str] = Field(description="Service name", example="--")
    capacity_real: Optional[int] = Field(example=1)
    properties: Dict[str, Any] = Field(
        description="Service additional properties",
        example={"additional_attribute_name": "additional_attribute_value"},
    )
    territories: list[ShortTerritory] = Field(example=[{"territory_id": 1, "name": "Санкт-Петербург"}])
    created_at: datetime = Field(default_factory=datetime.utcnow, description="The time when the territory was created")
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, description="The time when the territory was last updated"
    )

    @classmethod
    def from_dto(cls, dto: ServiceWithTerritoriesDTO) -> "ServiceWithTerritories":
        """
        Construct from DTO.
        """
        return cls(
            service_id=dto.service_id,
            service_type=ServiceTypes(
                service_type_id=dto.service_type_id,
                urban_function_id=dto.urban_function_id,
                name=dto.service_type_name,
                capacity_modeled=dto.service_type_capacity_modeled,
                code=dto.service_type_code,
            ),
            territory_type=TerritoryType(territory_type_id=dto.territory_type_id, name=dto.territory_type_name),
            name=dto.name,
            capacity_real=dto.capacity_real,
            properties=dto.properties,
            territories=[
                ShortTerritory(territory_id=territory["territory_id"], name=territory["name"])
                for territory in dto.territories
            ],
            created_at=dto.created_at,
            updated_at=dto.updated_at,
        )


class ServicesDataPost(BaseModel):
    physical_object_id: int = Field(example=1)
    object_geometry_id: int = Field(example=1)
    service_type_id: int = Field(example=1)
    territory_type_id: Optional[int] = Field(None, example=1)
    name: Optional[str] = Field(None, description="Service name", example="--")
    capacity_real: Optional[int] = Field(None, example=1)
    properties: Dict[str, Any] = Field(
        default_factory=dict,
        description="Service additional properties",
        example={"additional_attribute_name": "additional_attribute_value"},
    )


class ServicesDataPut(BaseModel):
    service_type_id: int = Field(..., example=1)
    territory_type_id: Optional[int] = Field(..., example=1)
    name: Optional[str] = Field(..., description="Service name", example="--")
    capacity_real: Optional[int] = Field(..., example=1)
    properties: Dict[str, Any] = Field(
        ...,
        description="Service additional properties",
        example={"additional_attribute_name": "additional_attribute_value"},
    )


class ServicesDataPatch(BaseModel):
    service_type_id: Optional[int] = Field(None, example=1)
    territory_type_id: Optional[int] = Field(None, example=1)
    name: Optional[str] = Field(None, description="Service name", example="--")
    capacity_real: Optional[int] = Field(None, example=1)
    properties: Optional[Dict[str, Any]] = Field(
        None,
        description="Service additional properties",
        example={"additional_attribute_name": "additional_attribute_value"},
    )

    @model_validator(mode="before")
    @classmethod
    def check_empty_request(cls, values):
        """
        Ensure the request body is not empty.
        """
        if not values:
            raise ValueError("request body cannot be empty")
        return values

    @model_validator(mode="before")
    @classmethod
    def disallow_nulls(cls, values):
        """
        Ensure the request body hasn't nulls.
        """
        for k, v in values.items():
            if v is None:
                raise ValueError(f"{k} cannot be null")
        return values


class ServicesDataWithGeometry(BaseModel):
    service_id: int = Field(example=1)
    service_type: ServiceTypes = Field(
        example={"service_type_id": 1, "urban_function_id": 1, "name": "Школа", "capacity_modeled": 1, "code": "1"}
    )
    territory_type: Optional[TerritoryType] = Field(example={"territory_type_id": 1, "name": "Город"})
    name: Optional[str] = Field(description="Service name", example="--")
    capacity_real: Optional[int] = Field(example=1)
    properties: Dict[str, Any] = Field(
        description="Service additional properties",
        example={"additional_attribute_name": "additional_attribute_value"},
    )
    geometry: Geometry = Field(description="Object geometry")
    centre_point: Geometry = Field(description="Centre coordinates")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="The time when the territory was created")
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, description="The time when the territory was last updated"
    )

    @classmethod
    def from_dto(cls, dto: ServiceWithGeometryDTO) -> "ServicesDataWithGeometry":
        """
        Construct from DTO.
        """
        return cls(
            service_id=dto.service_id,
            service_type=ServiceTypes(
                service_type_id=dto.service_type_id,
                urban_function_id=dto.urban_function_id,
                name=dto.service_type_name,
                capacity_modeled=dto.service_type_capacity_modeled,
                code=dto.service_type_code,
            ),
            territory_type=TerritoryType(territory_type_id=dto.territory_type_id, name=dto.territory_type_name),
            name=dto.name,
            capacity_real=dto.capacity_real,
            properties=dto.properties,
            geometry=Geometry.from_shapely_geometry(dto.geometry),
            centre_point=Geometry.from_shapely_geometry(dto.centre_point),
            created_at=dto.created_at,
            updated_at=dto.updated_at,
        )
