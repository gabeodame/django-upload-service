from typing import Optional, List, Union
from datetime import date
from pydantic import BaseModel, Field, field_validator

class ChemicalComposition(BaseModel):
    casNo: Optional[str] = ""
    chemicalName: Optional[str] = ""
    percentage: Optional[float] = None

    @field_validator("percentage", mode="before")
    def _empty_percentage_to_none(cls, v):
        if v == "":
            return None
        return v

class PPE(BaseModel):
    health: Optional[int] = None
    flammability: Optional[int] = None
    physical: Optional[int] = None
    protection: str = ""

class FormDataType(BaseModel):
    model_config = {"extra": "ignore"}

    # General Information
    WPSID: Optional[str] = ""
    chemNo: Optional[str] = ""
    chemDesc: Optional[str] = ""
    commodity: Optional[str] = ""
    grade: Optional[str] = ""
    testing: Optional[str] = ""
    testProps: Optional[str] = ""
    brandName: Optional[str] = ""
    companyName: Optional[str] = ""
    manuId: Optional[int] = None
    offsetsRuledOut_brand_manu: Optional[str] = ""
    outsourced_only: Optional[str] = ""
    composition: List[ChemicalComposition] = Field(default_factory=list)
    functions: List[str] = Field(default_factory=list)
    contain_cl: str = ""
    water_reaction: str = ""
    dioxane: str = ""

    # SDS Validation (specs)
    sdsSaved: Optional[str] = ""
    coaSaved: Optional[str] = ""
    sds_date: Optional[date] = None
    hazardous: Optional[str] = ""
    oxidizer: Optional[str] = ""
    corrosive: Optional[str] = ""
    color: Optional[str] = ""
    odor: Optional[str] = ""
    appearance: Optional[str] = ""
    form: Optional[str] = ""
    flashPoint: Optional[str] = ""
    freezePoint: Optional[str] = ""
    spg: Optional[float] = None
    pH_neat: Optional[float] = None
    vaporPressure: Optional[str] = ""
    meltingPoint: Optional[str] = ""
    blkDens: Optional[float] = None
    pH_1percent: Optional[float] = None
    pictograms: List[str] = Field(default_factory=list)
    solubility: Optional[str] = ""
    viscosity: Optional[str] = ""
    molarMass: Optional[str] = ""

    # PPE Validations
    ppe: Optional[str] = ""
    respiratorRequired: Optional[str] = ""
    respiratorType: Optional[str] = ""
    respiratorNo: Optional[str] = ""
    maskType: Optional[str] = ""
    catridgeType: Optional[str] = ""
    storageLocation: str = ""
    container: List[str] = Field(default_factory=list)

    # Regulatory Validation
    tsca: str = ""
    sara313Reportable: str = ""
    sara313CasNo: Optional[str] = ""
    prop65: str = ""
    propConc: List[ChemicalComposition] = Field(default_factory=list)

    # Environment Validation
    readilyBiodegradable: str = ""
    bioMethod: Optional[str] = ""
    bioAmount: Optional[float] = None
    marinePollutant: str = ""
    canadian_DSL_NDSL: str = ""
    voc: str = ""
    percentVoc: Optional[float] = None
    percentLVPVOC: Optional[float] = None
    derivedFromNaturalSrc: str = ""
    percentNaturallyDerived: Optional[float] = None
    bioBased: str = ""
    percentBiobased: Optional[float] = None

    # Tier II Reportable
    tier_II_reportable: str = ""
    tier_II_amount: Optional[float] = None
    tier_II_EHS: Optional[str] = ""
    tier_II_hazard_composition: Optional[str] = ""
    tier_II_hazard_form: Optional[str] = ""
    tier_II_hazard_class: List[str] = Field(default_factory=list)

    # Allergens validation
    containsBacteria: str = ""
    containsPalm_PalmKernelOil: str = ""
    palmOil_Other_certified: str = ""
    otherOils: str = ""

    # Used in formulations
    certifications: List[str] = Field(default_factory=list)
    notes: Optional[str] = ""

    # Files
    sdsFile: Optional[Union[str, bytes]] = ""
    coaFile: Optional[Union[str, bytes]] = ""
    otherFiles: List[Union[str, bytes]] = Field(default_factory=list)

    @field_validator(
        "manuId",
        "sds_date",
        "spg",
        "pH_neat",
        "blkDens",
        "pH_1percent",
        "bioAmount",
        "percentVoc",
        "percentLVPVOC",
        "percentNaturallyDerived",
        "percentBiobased",
        "tier_II_amount",
        mode="before",
    )
    def _empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

    @field_validator(
        "composition",
        "functions",
        "pictograms",
        "container",
        "propConc",
        "tier_II_hazard_class",
        "certifications",
        "otherFiles",
        mode="before",
    )
    def _normalize_list_fields(cls, v):
        if v is None or v == "":
            return []
        if isinstance(v, str):
            return [item.strip() for item in v.split(",") if item.strip()]
        return v
