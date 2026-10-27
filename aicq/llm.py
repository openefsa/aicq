# Mapping from app-facing model IDs to Databricks serving endpoint names and cost library 
# the key is picked "in frontend app" so should match:
# https://dev.azure.com/efsa-devops/TRI%20-%20Data%20product%20-%20Serve%201/_git/dp-srv1-autocat-apps.databricks?path=/aicq-frontend/src/NewExtractionForm.jsx&version=GBmain&line=3&lineEnd=4&lineStartColumn=1&lineEndColumn=1&lineStyle=plain&_a=contents
# 'oca': https://github.com/orkunkinay/openai_cost_calculator

                   


def get_model_info(sub_env):
    return {
    "claude-opus-4-6": {"env":"databricks", 
                        "limits": {"max_tokens": 128000 },
                        "deployment": f"autocat-runtime-{sub_env}-llm-claude-opus-4_6",
                        "oca":["anthropic","claude-opus-4-6"]},

    "claude-opus-4-8": {"env":"databricks",
                        "limits": {"max_tokens": 128000 },
                        "deployment":f"autocat-runtime-{sub_env}-llm-claude-opus-4_8",
                        "oca": ["anthropic","claude-opus-4-8"] },

    "claude-opus-5": {"env":"databricks",
                      "limits": {"max_tokens": 128000 },
                      "deployment": f"autocat-runtime-{sub_env}-llm-claude-opus-5",
                      "oca": ["anthropic","claude-opus-5"] },

    "claude-sonnet-4_5": {"env":"databricks",
                          "limits": {"max_tokens": 64000 },
                          "deployment": f"autocat-runtime-{sub_env}-llm-claude-sonnet-4_5",
                          "oca": ["anthropic","claude-sonnet-4-5"] },

    "claude-sonnet-4_6": {"env":"databricks",
                          "limits": {"max_tokens": 128000 },
                          "deployment": f"autocat-runtime-{sub_env}-llm-claude-sonnet-4_6",
                          "oca": ["anthropic","claude-sonnet-4-6"] },

    "gpt-5": {"env":"databricks",
              "limits": {"max_tokens": 128000 },
              "deployment": f"autocat-runtime-{sub_env}-llm-gpt5",
              "oca":  ["azure","gpt-5"]},

    "gpt-5.1": {"env":"databricks",
                "limits": {"max_tokens": 128000 },
                "deployment": f"autocat-runtime-{sub_env}-llm-gpt5_1",
                "oca":  ["azure","gpt-5.1"]},

    "gpt-5-4": {"env":"databricks",
                "limits": {"max_tokens": 128000 },
                "deployment": f"autocat-runtime-{sub_env}-llm-gpt5_4",
                "oca": ["azure","gpt-5.4"] },

    "gpt-5-6-terra": {"env":"databricks",
                      "limits": {"max_tokens": 128000 },
                      "deployment": f"autocat-runtime-{sub_env}-llm-gpt5_6-terra",
                      "oca": ["azure","gpt-5.6-terra"] },

    "gpt5_6-sol": {"env":"databricks",
                   "limits": {"max_tokens": 128000 },
                   "deployment": f"autocat-runtime-{sub_env}-llm-gpt5_6-sol",
                   "oca": ["azure","gpt-5.6-sol"] },

    "gpt-4o": {"env":"databricks",
               "limits": {"max_tokens": 16384 },
               "deployment": f"autocat-runtime-{sub_env}-llm-gpt4o",
               "oca": ["azure","gpt-4o-1120"] },

    "gpt-4o-mini": {"env":"databricks",
                    "limits": {"max_tokens": 16384 },
                    "deployment": f"autocat-runtime-{sub_env}-llm-gpt4o-mini",
                    "oca": ["azure","gpt-4o-mini-0718"] },

    "gpt-5-mini": {"env":"databricks",
                   "limits": {"max_tokens": 128000 },
                   "deployment": f"autocat-runtime-{sub_env}-llm-gpt5-mini",
                   "oca": ["azure","gpt-5-mini"] },


    "innov--gpt-4o": {"env":"innovation-zone",
                      "limits": {"max_tokens": 16384 },
                      "deployment": "gpt-4o",
                      "oca": ["azure","gpt-4o-0513"] },

    "innov--gpt-4.1-mini": {"env":"innovation-zone",
                            "limits": {"max_tokens": 32768 },
                            "deployment": "gpt-4.1-mini",
                            "oca": ["azure","gpt-4.1-mini"] },

    "anthropic--claude-sonnet-4-5": {"env":"anthropic",
                                     "limits": {"max_tokens": 64000 },
                                     "deployment": "claude-sonnet-4-5",
                                     "oca": ["anthropic","claude-sonnet-4-5"] },

    "anthropic--claude-sonnet-4-6": {"env":"anthropic",
                                     "limits": {"max_tokens": 128000 },
                                     "deployment": "claude-sonnet-4-6",
                                     "oca": ["anthropic","claude-sonnet-4-6"] },

    "anthropic2--claude-sonnet-4-5": {"env":"anthropic2",
                                      "limits": {"max_tokens": 64000 },
                                      "deployment": "claude-sonnet-4-5-20250929",
                                      "oca": ["anthropic","claude-sonnet-4-5"] }
}
