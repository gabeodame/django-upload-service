from dataclasses import dataclass
from typing import Optional, List, Union
from datetime import date


@dataclass
class ChemicalComposition:
    name: str
    concentration: float
    unit: str
    pass


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
    flammability: Optional[str]
    pictograms: Optional[List[str]]
    solubility: Optional[str]
    viscosity: Optional[str]
    molarMass: Optional[str]

    # PPE Validations
    ppe: Optional[str]
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
    propconc: Optional[float]
    water_reaction: str
    contains_cl: str
    one_4_dioxane: str

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


prompt = (
    "using the attached information and any other files available to you fill the a chemical "
    "intake form with the following columns chemNo, chemDesc, chemGrade, commodity, testing, "
    "testProps, companyName, brandName, outsourced_only, composition, WPSID, sdsSaved, sdsFile, "
    "coaSaved, coaFile, sds_date, hazardous, oxidizer, form, color, odor, appearance, flashPoint, "
    "freezePoint, spg, pH_neat, vaporPressure, meltingPoint, pH_1percent, blkDens, corrosive, "
    "solubility, pictograms, ppe, respiratorRequired, respiratorType, respiratorNo, maskType, "
    "catridgeType, storageLocation, container, tsca, sara313Reportable, sara313CasNo, "
    "prop65, water_reaction, contains_cl, one_4_dioxane, propConc,"
    "readilyBiodegradable, bioMethod, bioAmount, "
    "marinePollutant, canadian_DSL_NDSL, voc, percentVoc, percentLVPVOC, derivedFromNaturalSrc, "
    "percentNaturallyDerived, bioBased, percentBiobased, tier_II_reportable, tier_II_amount, "
    "tier_II_EHS, tier_II_hazard_composition, tier_II_hazard_form, tier_II_hazard_class, "
    "containsBacteria, containsPalm_PalmKernelOil, otherOils, palmOil_Other_certified, "
    "certifications, notes, otherFiles. convert filled form into "
    "a json object to be easily consumed by front end react-hook-form as initial values. If data "
    "for a field is not specified use and empty string, for fields whose responses are boolean use "
    "Yes,No. For composition and propConc fields, "
    "it is likely to be a list of multiple components create appropriate array with chemicalName, "
    "casNo and percentage. Where percentage is given as a range calculate the average. "
    "Similarly for other fields where a range is give use average values. "
    "For container in [Drum, Tote, Super Sack, Bag] and certifications in [Safer Choice, "
    "Kosher, NSF, Green Seal, Whole Foods, EPA, FDA, Halal], break into a list with the most relevant match "
    "The dataTypes used for the form is {} be aware of units and convert to "
    "Imperial where appropriate as user is based in USA"
).format(FormDataType)