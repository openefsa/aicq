from pydantic import AfterValidator, BaseModel, Field, RootModel, confloat, constr
from typing import Annotated, Any,List
from uuid import UUID
from jsonschema import validate
from jsonschema import Draft202012Validator


# Mapping from app-facing model IDs to Databricks serving endpoint names and cost library 
# the key is picked "in frontend app" so should match:
# https://dev.azure.com/efsa-devops/TRI%20-%20Data%20product%20-%20Serve%201/_git/dp-srv1-autocat-apps.databricks?path=/aicq-frontend/src/NewExtractionForm.jsx&version=GBmain&line=3&lineEnd=4&lineStartColumn=1&lineEndColumn=1&lineStyle=plain&_a=contents
# 'oca': https://github.com/orkunkinay/openai_cost_calculator
def get_model_info(sub_env):
    return {
    "claude-opus-4-6": {"env":"databricks", "deployment": f"autocat-runtime-{sub_env}-llm-claude-opus-4_6","oca":["anthropic","claude-opus-4-6"]},
    "claude-opus-4-8": {"env":"databricks","deployment":f"autocat-runtime-{sub_env}-llm-claude-opus-4_8","oca": ["anthropic","claude-opus-4-8"] },
    "claude-opus-5": {"env":"databricks","deployment": f"autocat-runtime-{sub_env}-llm-claude-opus-5","oca": ["anthropic","claude-opus-5"] },
    "claude-sonnet-4_5": {"env":"databricks","deployment": f"autocat-runtime-{sub_env}-llm-claude-sonnet-4_5","oca": ["anthropic","claude-sonnet-4-5"] },
    "claude-sonnet-4_6": {"env":"databricks","deployment": f"autocat-runtime-{sub_env}-llm-claude-sonnet-4_6","oca": ["anthropic","claude-sonnet-4-6"] },
    "gpt-5": {"env":"databricks","deployment": f"autocat-runtime-{sub_env}-llm-gpt5","oca":  ["azure","gpt-5"]},
    "gpt-5.1": {"env":"databricks","deployment": f"autocat-runtime-{sub_env}-llm-gpt5_1","oca":  ["azure","gpt-5.1"]},
    "gpt-5-4": {"env":"databricks","deployment": f"autocat-runtime-{sub_env}-llm-gpt5_4","oca": ["azure","gpt-5.4"] },
    "gpt-5-6-terra": {"env":"databricks","deployment": f"autocat-runtime-{sub_env}-llm-gpt5_6-terra","oca": ["azure","gpt-5.6-terra"] },
    "gpt5_6-sol": {"env":"databricks","deployment": f"autocat-runtime-{sub_env}-llm-gpt5_6-sol","oca": ["azure","gpt-5.6-sol"] },
    "gpt-4o": {"env":"databricks","deployment": f"autocat-runtime-{sub_env}-llm-gpt4o","oca": ["azure","gpt-4o-mini-0718"] },
    "gpt-4o-mini": {"env":"databricks","deployment": f"autocat-runtime-{sub_env}-llm-gpt4o-mini","oca": ["azure","gpt-5-mini"] },
    "gpt-5-mini": {"env":"databricks","deployment": f"autocat-runtime-{sub_env}-llm-gpt5-mini","oca": ["azure","gpt-4o-1120"] },

    "innov--gpt-4o": {"env":"innovation-zone","deployment": "gpt-4o","oca": ["azure","gpt-4o-0513"] },
    "innov--gpt-4.1-mini": {"env":"innovation-zone","deployment": "gpt-4.1-mini","oca": ["azure","gpt-4.1-mini"] },
    "anthropic--claude-sonnet-4-5": {"env":"anthropic","deployment": "claude-sonnet-4-5","oca": ["anthropic","claude-sonnet-4-5"] },
    "anthropic--claude-sonnet-4-6": {"env":"anthropic","deployment": "claude-sonnet-4-6","oca": ["anthropic","claude-sonnet-4-6"] },

    "anthropic2--claude-sonnet-4-5": {"env":"anthropic2","deployment": "claude-sonnet-4-5-20250929","oca": ["anthropic","claude-sonnet-4-5"] }
}

latest_meta_schema = Draft202012Validator.META_SCHEMA
meta_validator = Draft202012Validator(latest_meta_schema)

def assert_valid_schema(value):
    meta_validator.check_schema(value)
    return value
    

    


class IRRDataExtractionItem(BaseModel):
    variable_name: str | None = None
    all_values: list[Any] | None = None
    unalike_score: confloat(ge=0.0, le=1.1) | None = None
    """
    Used if the variable is type 'categorical' or 'binary'. see R function ragree::unalike
    """
    string_distance: Any | None = None
    """
    Used if the variable is type 'text'. Uses 'edit distance' to calculate  text similarity metrices and then aggregate via xxxx into a single value
    """
    embedding_distance: confloat(ge=0.0, le=1.1) | None = None
    """
    Used if the variable is type 'text', Uses sentence-transformer to calculate embeddings and pair-wise cosine distance as text similarity metric and then aggregate via mean to a single value
    """
    normalized_coefficient_of_variation: float | None = None
    """
    Used if the variable is type 'number'
    """
    string_irr_strength: confloat(ge=0.0, le=1.1) | None = None
    """
    Used if the variable is type 'string'. Contains the LLM agreement scale (0.0-1.0).
    """
    string_irr_justification:  str | None = None
    """
    Used if the variable is type 'string'. Contains the LLM justification of agreement/disagreement.
    """
    consensus_result: str | None = None
    """
    Used if the variable is type 'string'. Contains the dominating/merged result
    produced by the judge LLM from the multiple LLM extractions.
    """


class IRRDataExtraction(RootModel[list[IRRDataExtractionItem]]):
    root: list[IRRDataExtractionItem] = Field(
        ..., examples=[{"variable_name": "is_primary?", "unalike_score": 0.5}]
    )


class PromptTemplate(RootModel[str]):
    root: str = Field(
        ...,
        examples=[
            "extract data from the following text:\n---------------------------------------------\n${content}"
        ],
    )
    """
    The overall template of the prompt which should contain 2 placeholders. ${schema} and ${content} which will be replaced at runtime.
    """

class StructuredOutputSchema(BaseModel):
    """
    JSON schema defining the shape of the data to extract
    """

    json_schema:   Annotated[dict[str, Any], AfterValidator(assert_valid_schema)] 
    
    


class DOI(RootModel[constr(pattern=r"^10.*$")]):
    root: constr(pattern=r"^10.*$") = Field(..., examples=["10.2903/j.efsa.2026.10049"])
    """
    Digital Object Identifier
    """


class ExtractedValue(BaseModel):
    variable_name: str
    variable_value: Any
    
class ExtractedValues(RootModel[list[ExtractedValue]]):
    root: list[ExtractedValue]



class DataExtractionResultMultiple(BaseModel):
    model_id: str
    doi: DOI
    extracted_values_array: list[ExtractedValues]
    files: list[str]


class DataExtractionResult(BaseModel):
    model_id: str
    doi: DOI
    extracted_values: ExtractedValues
    files: list[str]




class BibliographicReference(BaseModel):
    TY: str | None = None
    AU: str | None = None
    PY: int | None = None
    DA: str | None = None
    TI: str | None = None
    T2: str | None = None
    SP: int | None = None
    EP: int | None = None
    VL: int | None = None


class BibliographicReferenceList(RootModel[list[BibliographicReference]]):
    root: list[BibliographicReference]


class TitleAbstract(BaseModel):
    """
    Holds the title and abstract of a scientific paper
    """

    title: str
    abstract: str




class IRRDataExtractionItem(BaseModel):
    variable_name: str | None = None
    all_values: list[Any] | None = None
    unalike_score: confloat(ge=0.0, le=1.0) | None = None
    """
    Used if the variable is type 'categorical' or 'binary'. see R function ragree::unalike
    """
    string_distance: Any | None = None
    """
    Used if the variable is type 'text'. Uses 'edit distance' to calculate  text similarity metrices and then aggregate via xxxx into a single value
    """
    embedding_distance: confloat(ge=0.0, le=1.0) | None = None
    """
    Used if the variable is type 'text', Uses sentence-transformer to calculate embeddings and pair-wise cosine distance as text similarity metric and then aggregate via mean to a single value
    """
    normalized_coefficient_of_variation: float | None = None
    """
    Used if the variable is type 'number'
    """


class IRRDataExtraction(RootModel[list[IRRDataExtractionItem]]):
    root: list[IRRDataExtractionItem] = Field(
        ..., examples=[{"variable_name": "is_primary?", "unalike_score": 0.5}]
    )


class ValidationDataExtractionItem(BaseModel):
    variable_name: str | None = None
    agreement_with_ground_truth: confloat(ge=0.0, le=1.0) | None = None
    """
    Some form of scoring, able to compare single ground trueth and multiple LLM extractions/predictions. Need to work for categorical/binary variables, but also for text variables and produce a single score. Maybe this needs first an 'agreement' (using mayority vote ??. 'LLM as judge to summarize for text' ?) calculation for the multiple LLMs before comparing with single ground trueth
    """


class ValidationDataExtraction(RootModel[list[ValidationDataExtractionItem]]):
    root: list[ValidationDataExtractionItem]


class ValidationScreeningItem(BaseModel):
    variable_name: str | None = None
    agreement_with_ground_truth: confloat(ge=0.0, le=1.0) | None = None
    """
    Some form of scoring, able to compare single ground trueth and multiple LLM extractions/predictions. Need to work for 'boolean' variables.  Maybe this needs first an 'agreement' (using mayority vote ??. ) calculation for the multiple LLMs before comparing with single ground trueth
    """


class ValidationScreening(RootModel[list[ValidationScreeningItem]]):
    root: list[ValidationScreeningItem]


class ScreeningAgreement(RootModel[confloat(ge=0.0, le=1.0)]):
    root: confloat(ge=0.0, le=1.0)
    """
    Aggrement mong different LLMs regaring a screening variable prediction
    """


class FleissKappa(RootModel[confloat(ge=0.0, le=1.0)]):
    root: confloat(ge=0.0, le=1.0)


class ScreeningDecisionItem(BaseModel):
    screening_criteria: str
    screening_criteria_decision: bool


class ScreeningDecision(RootModel[list[ScreeningDecisionItem]]):
    root: list[ScreeningDecisionItem] = Field(
        ...,
        examples=[
            {"screening_criteria": "is_primary", "screening_criteria_decision": True}
        ],
    )




class DOI(RootModel[constr(pattern=r"^10.*$")]):
    root: constr(pattern=r"^10.*$") = Field(..., examples=["10.2903/j.efsa.2026.10049"])
    """
    Digital Object Identifier
    """




class ScreeningResult(BaseModel):
    model_id: str
    doi: DOI | None = None
    title_abstract: TitleAbstract
    screening_decision: ScreeningDecision


class IRRScreeningItem(BaseModel):
    variable_name: str
    screening_agreement: ScreeningAgreement


class IRRScreening(RootModel[list[IRRScreeningItem]]):
    root: list[IRRScreeningItem]


class Validation(BaseModel):
    model_id: str | None = None
    prompt_template: PromptTemplate | None = None
    documents: BibliographicReferenceList | None = None
    score: float | None = None


class VariableExtractionPrompt(BaseModel):
    id: UUID | None = None
    variable_name: str | None = None
    schema_: StructuredOutputSchema | None = Field(None, alias="schema")
    instruction: str | None = None
    validations: list[Validation] | None = None
    """
    The past validations of this extraction prompt, if any
    """


class DataExtractionJobRequest(BaseModel):
    """Request body for triggering a data extraction job."""
    prompt: str = Field(
        description="Prompt template with ${schema} and ${content} placeholders, replaced at runtime.",
    )
    screening_schema: StructuredOutputSchema = Field(
        description="JSON schema specifying which data to extract from documents.",
    )
    models: List[str] = Field(
        description="List of LLM model identifiers to use. Each model independently extracts data.",
    )
    use_original_document: bool = Field(
        default=False,
        description="When True, pass the original PDF pages to the LLM as multimodal input instead of extracting text first.",
    )

