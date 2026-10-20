import unittest

from jsonschema import SchemaError

import model

valid_schema = {"type": "object", "properties": {"population_of_dairy_cows": {"description": "at least one of the populations studied was dairy cows (any lactation status, any age except calves and youngstock, including heifers in the last third of gestation) ", "type": "boolean"}, "housing_system": {"description": "article refers to at least one housing system or practice of keeping dairy cows", "type": "boolean"}, "mastitis": {"description": "study is on mastitis and not on case studies of mastitis outbreaks ", "type": "boolean"}, "cattle": {"description": "study is on cattle and not other animals such as calves, sheep, goat ", "type": "boolean"}, "topic_housing": {"description": "study is on housing systems and not on breeding, feeding, fertility, udder cleanliness and other welfare indicators, milk production, mortality, description of management without associations to health ", "type": "boolean"}, "study_design": {"description": "study design is observational or epidemiological studies or experimental studies", "type": "boolean"}}, "required": ["population_of_dairy_cows", "housing_system", "mastitis", "cattle", "topic_housing", "study_design"]}


class MyTest(unittest.TestCase):
    

    def test_output_schema_invalid(self):
        with self.assertRaises(SchemaError):
            model.StructuredOutputSchema(json_schema={"type": "invalid"})
                                         
        with self.assertRaises(SchemaError):
            model.StructuredOutputSchema(json_schema={"properties": {"a thing": {}}})

            
        
            
            
            
    def test_output_valid(self):
            model.StructuredOutputSchema(json_schema=valid_schema)
            model.StructuredOutputSchema(json_schema={"properties": {"a_thing": {}}})

            
