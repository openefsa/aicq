import unittest

from jsonschema import SchemaError

from aicq.model import StructuredOutputSchema
from aicq.llm import get_model_list,get_model_info

valid_schema = {"type": "object", "properties": {"population_of_dairy_cows": {"description": "at least one of the populations studied was dairy cows (any lactation status, any age except calves and youngstock, including heifers in the last third of gestation) ", "type": "boolean"}, "housing_system": {"description": "article refers to at least one housing system or practice of keeping dairy cows", "type": "boolean"}, "mastitis": {"description": "study is on mastitis and not on case studies of mastitis outbreaks ", "type": "boolean"}, "cattle": {"description": "study is on cattle and not other animals such as calves, sheep, goat ", "type": "boolean"}, "topic_housing": {"description": "study is on housing systems and not on breeding, feeding, fertility, udder cleanliness and other welfare indicators, milk production, mortality, description of management without associations to health ", "type": "boolean"}, "study_design": {"description": "study design is observational or epidemiological studies or experimental studies", "type": "boolean"}}, "required": ["population_of_dairy_cows", "housing_system", "mastitis", "cattle", "topic_housing", "study_design"]}


class MyTest(unittest.TestCase):
    

    def test_modelinfo(self):
        self.assertListEqual(get_model_list("create"),['autocat-runtime-create-1c-llm-claude-opus-4_6', 'autocat-runtime-create-1c-llm-claude-opus-4_8', 'autocat-runtime-create-1c-llm-claude-opus-5', 'autocat-runtime-create-1c-llm-claude-sonnet-4_5', 'autocat-runtime-create-1c-llm-claude-sonnet-4_6', 'autocat-runtime-create-1c-llm-gpt4o', 'autocat-runtime-create-1c-llm-gpt4o-mini', 'autocat-runtime-create-1c-llm-gpt5', 'autocat-runtime-create-1c-llm-gpt5_1', 'autocat-runtime-create-1c-llm-gpt5_4', 'autocat-runtime-create-1c-llm-gpt5_5', 'autocat-runtime-create-1c-llm-gpt5_6-luna', 'autocat-runtime-create-1c-llm-gpt5_6-sol', 'autocat-runtime-create-1c-llm-gpt5_6-terra', 'autocat-runtime-create-1c-llm-gpt5-mini'])
        
        self.assertSetEqual(set([get_model_info(m)["limits"]["max_tokens"] for m in get_model_list("create")]),{128000, 64000, 16384})
        #model_info_create=get_model_info("create")
        
            
    
    def test_output_schema_invalid(self):
        with self.assertRaises(SchemaError):
            StructuredOutputSchema(json_schema={"type": "invalid"})
                                         

            
            
    def test_output_valid(self):
            StructuredOutputSchema(json_schema=valid_schema)
            StructuredOutputSchema(json_schema={"properties": {"a_thing": {}}})

            
