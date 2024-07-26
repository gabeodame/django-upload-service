from dataclasses import dataclass
from typing import Optional, List, Union
from datetime import date

@dataclass
class ChemicalComposition:
    casNo: Optional[str]
    chemicalName: Optional[str]
    percentage: float

@dataclass
class PPE:
    health: Optional[int]
    flammability: Optional[int]
    physical: Optional[int]
    protection: str

@dataclass
class FormDataType:
    # General Information
    WPSID: Optional[str]
    chemNo: Optional[str]
    chemDesc: Optional[str]
    commodity: Optional[str]
    grade: Optional[str]
    testing: Optional[str]
    testProps: Optional[str]
    brandName: Optional[str]
    companyName: Optional[str]
    manuId: Optional[int]
    offsetsRuledOut_brand_manu: Optional[str]
    outsourced_only: Optional[str]
    composition: List[ChemicalComposition]
    functions: Optional[List[str]]
    contain_cl: str
    water_reaction: str
    dioxane: str

    # SDS Validation (specs)
    sdsSaved: Optional[str]
    coaSaved: Optional[str]
    sds_date: Optional[date]
    hazardous: Optional[str]
    oxidizer: Optional[str]
    corrosive: Optional[str]
    color: Optional[str]
    odor: Optional[str]
    appearance: Optional[str]
    form: Optional[str]
    flashPoint: Optional[str]
    freezePoint: Optional[str]
    spg: Optional[float]
    pH_neat: Optional[float]
    vaporPressure: Optional[str]
    meltingPoint: Optional[str]
    blkDens: Optional[float]
    pH_1percent: Optional[float]
    pictograms: Optional[List[str]]
    solubility: Optional[str]
    viscosity: Optional[str]
    molarMass: Optional[str]

    # PPE Validations
    ppe: Optional[PPE]
    respiratorRequired: Optional[str]
    respiratorType: Optional[str]
    respiratorNo: Optional[str]
    maskType: Optional[str]
    catridgeType: Optional[str]
    storageLocation: str
    container: List[str]

    # Regulatory Validation
    tsca: str
    sara313Reportable: str
    sara313CasNo: Optional[str]
    prop65: str
    propConc: Optional[List[ChemicalComposition]]

    # Environment Validation
    readilyBiodegradable: str
    bioMethod: Optional[str]
    bioAmount: Optional[float]
    marinePollutant: str
    canadian_DSL_NDSL: str
    voc: str
    percentVoc: Optional[float]
    percentLVPVOC: Optional[float]
    derivedFromNaturalSrc: str
    percentNaturallyDerived: Optional[float]
    bioBased: str
    percentBiobased: Optional[float]

    # Tier II Reportable
    tier_II_reportable: str
    tier_II_amount: Optional[float]
    tier_II_EHS: Optional[str]
    tier_II_hazard_composition: Optional[str]
    tier_II_hazard_form: Optional[str]
    tier_II_hazard_class: Optional[List[str]]

    # Allergens validation
    containsBacteria: str
    containsPalm_PalmKernelOil: str
    palmOil_Other_certified: str
    otherOils: str

    # Used in formulations
    certifications: List[str]
    notes: Optional[str]

    # Files
    sdsFile: Optional[Union[str, bytes]]
    coaFile: Optional[Union[str, bytes]]
    otherFiles: Optional[List[Union[str, bytes]]]
