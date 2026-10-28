# Mapping from app-facing model IDs to Databricks serving endpoint names and cost library 
# the key is picked "in frontend app" so should match:
# https://dev.azure.com/efsa-devops/TRI%20-%20Data%20product%20-%20Serve%201/_git/dp-srv1-autocat-apps.databricks?path=/aicq-frontend/src/NewExtractionForm.jsx&version=GBmain&line=3&lineEnd=4&lineStartColumn=1&lineEndColumn=1&lineStyle=plain&_a=contents
# 'oca': https://github.com/orkunkinay/openai_cost_calculator


MODEL_INFO= {'autocat-runtime-$ENV$-llm-claude-opus-4_6':
     {"env":"databricks", 
                        "limits": {"max_tokens": 128000 },
                        "oca":["anthropic","claude-opus-4-6"]},
      
     'autocat-runtime-$ENV$-llm-claude-opus-4_8':
         {"env":"databricks",
        "limits": {"max_tokens": 128000 },
        "oca": ["anthropic","claude-opus-4-8"] }, 
         
     'autocat-runtime-$ENV$-llm-claude-opus-5':
         {"env":"databricks",
                      "limits": {"max_tokens": 128000 },
                      "oca": ["anthropic","claude-opus-5"] },
          
     'autocat-runtime-$ENV$-llm-claude-sonnet-4_5':
         {"env":"databricks",
                          "limits": {"max_tokens": 64000 },
                          "oca": ["anthropic","claude-sonnet-4-5"] },
          
     'autocat-runtime-$ENV$-llm-claude-sonnet-4_6':
         {"env":"databricks",
                          "limits": {"max_tokens": 128000 },
                          "oca": ["anthropic","claude-sonnet-4-6"] }, 
         
     'autocat-runtime-$ENV$-llm-gpt4o':
         {"env":"databricks",
               "limits": {"max_tokens": 16384 },
               "oca": ["azure","gpt-4o-1120"] }, 
         
     'autocat-runtime-$ENV$-llm-gpt4o-mini':
         {"env":"databricks",
                    "limits": {"max_tokens": 16384 },
                    "oca": ["azure","gpt-4o-mini-0718"] }, 
         
     'autocat-runtime-$ENV$-llm-gpt5':
         {"env":"databricks",
              "limits": {"max_tokens": 128000 },
              "oca":  ["azure","gpt-5"]}, 
         
     'autocat-runtime-$ENV$-llm-gpt5_1':
         {"env":"databricks",
                "limits": {"max_tokens": 128000 },
                "oca":  ["azure","gpt-5.1"]},
          
     'autocat-runtime-$ENV$-llm-gpt5_4':
         {"env":"databricks",
                "limits": {"max_tokens": 128000 },
                "oca": ["azure","gpt-5.4"] }
         , 
     
     'autocat-runtime-$ENV$-llm-gpt5_5':
         {"env":"databricks",
                            "limits": {"max_tokens": 128000 },
                            #"oca": ["azure","gpt-5.5"]
                            },
      
     'autocat-runtime-$ENV$-llm-gpt5_6-luna':
         {"env":"databricks",
                                     "limits": {"max_tokens": 128000 },
                                     #"oca": ["azure","gpt-5.5"]
                                     }, 
     
     'autocat-runtime-$ENV$-llm-gpt5_6-sol':
         {"env":"databricks",
                   "limits": {"max_tokens": 128000 },
                   "oca": ["azure","gpt-5.6-sol"] }, 
         
     'autocat-runtime-$ENV$-llm-gpt5_6-terra':
         {"env":"databricks",
                      "limits": {"max_tokens": 128000 },
                      "oca": ["azure","gpt-5.6-terra"] }, 
         
     'autocat-runtime-$ENV$-llm-gpt5-mini':
         {"env":"databricks",
                   "limits": {"max_tokens": 128000 },
                   "oca": ["azure","gpt-5-mini"] },
          
     # 'autocat-runtime-$ENV$-llm-gpt5-nano':, 
     
     #'autocat-runtime-$ENV$-llm-text-embedding-3-large':, 
     #'autocat-runtime-$ENV$-llm-text-embedding-ada-002':
     }
    
    
                   
def get_model_list(env):
    match env:
      case "create":
        suffix = "1c"
      case "accept":
          suffix = "2a"
      case "publish":
           suffix = "3p"

    sub_env = env + "-" + suffix

    return [deployment.replace("$ENV$",sub_env) for deployment in MODEL_INFO.keys()]


def get_model_info(deployment):
    if 'create-1c' in deployment:
        key = deployment.replace('create-1c','$ENV$')
    elif 'accept-2a' in deployment:
        key = deployment.replace('accept-2a','$ENV$')
    elif 'publish-3p' in deployment:
        key = deployment.replace('publish-3p','$ENV$')
        
    return MODEL_INFO[key]
    
    
    

    # "innov--gpt-4o": {"env":"innovation-zone",
    #                   "limits": {"max_tokens": 16384 },
    #                   "deployment": "gpt-4o",
    #                   "oca": ["azure","gpt-4o-0513"] },

    # "innov--gpt-4.1-mini": {"env":"innovation-zone",
    #                         "limits": {"max_tokens": 32768 },
    #                         "deployment": "gpt-4.1-mini",
    #                         "oca": ["azure","gpt-4.1-mini"] },

    # "anthropic--claude-sonnet-4-5": {"env":"anthropic",
    #                                  "limits": {"max_tokens": 64000 },
    #                                  "deployment": "claude-sonnet-4-5",
    #                                  "oca": ["anthropic","claude-sonnet-4-5"] },

    # "anthropic--claude-sonnet-4-6": {"env":"anthropic",
    #                                  "limits": {"max_tokens": 128000 },
    #                                  "deployment": "claude-sonnet-4-6",
    #                                  "oca": ["anthropic","claude-sonnet-4-6"] },

    # "anthropic2--claude-sonnet-4-5": {"env":"anthropic2",
    #                                   "limits": {"max_tokens": 64000 },
    #                                   "deployment": "claude-sonnet-4-5-20250929",
    #                                   "oca": ["anthropic","claude-sonnet-4-5"] }

