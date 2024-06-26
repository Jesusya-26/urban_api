"""
Data Transfer Objects (much like entities from database) are defined in this module.
"""

from .functional_zones import FunctionalZoneDataDTO
from .indicators import IndicatorDTO, IndicatorValueDTO, MeasurementUnitDTO
from .living_buildings import LivingBuildingsDTO, LivingBuildingsWithGeometryDTO
from .object_geometries import ObjectGeometryDTO
from .physical_objects import (
    PhysicalObjectDataDTO,
    PhysicalObjectTypeDTO,
    PhysicalObjectWithGeometryDTO,
    PhysicalObjectWithTerritoryDTO,
)
from .service_types import ServiceTypesDTO, ServiceTypesNormativesDTO, UrbanFunctionDTO
from .services import ServiceDTO, ServiceWithGeometryDTO, ServiceWithTerritoriesDTO
from .territories import TerritoryDTO, TerritoryTypeDTO, TerritoryWithoutGeometryDTO
from .users import TokensTuple, UserDTO

__all__ = [
    "TerritoryTypeDTO",
    "TerritoryDTO",
    "UserDTO",
    "TokensTuple",
    "ServiceDTO",
    "ServiceTypesDTO",
    "ServiceTypesNormativesDTO",
    "ServiceWithGeometryDTO",
    "ServiceWithTerritoriesDTO",
    "IndicatorDTO",
    "IndicatorValueDTO",
    "MeasurementUnitDTO",
    "ObjectGeometryDTO",
    "PhysicalObjectDataDTO",
    "PhysicalObjectTypeDTO",
    "PhysicalObjectWithGeometryDTO",
    "PhysicalObjectWithTerritoryDTO",
    "LivingBuildingsDTO",
    "LivingBuildingsWithGeometryDTO",
    "FunctionalZoneDataDTO",
    "TerritoryWithoutGeometryDTO",
    "UrbanFunctionDTO",
]
