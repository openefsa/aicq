# Mapping from app-facing model IDs to Databricks serving endpoint names and cost library
# the key is picked "in frontend app" so should match:
# https://dev.azure.com/efsa-devops/TRI%20-%20Data%20product%20-%20Serve%201/_git/dp-srv1-autocat-apps.databricks?path=/aicq-frontend/src/NewExtractionForm.jsx&version=GBmain&line=3&lineEnd=4&lineStartColumn=1&lineEndColumn=1&lineStyle=plain&_a=contents
# 'oca': https://github.com/orkunkinay/openai_cost_calculator


MODEL_INFO = {
    "autocat-runtime-$ENV$-llm-claude-opus-4_6": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "oca": ["anthropic", "claude-opus-4-6"],
        "benchmarks": {
            "benchlm": {"overall": 61.82, "inputPrice": 5, "outputPrice": 25}
        },
    },
    "autocat-runtime-$ENV$-llm-claude-opus-4_8": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "oca": ["anthropic", "claude-opus-4-8"],
        "benchmarks": {
            "benchlm": {"overall": 69.63, "inputPrice": 5, "outputPrice": 25}
        },
    },
    "autocat-runtime-$ENV$-llm-claude-opus-5": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "benchmarks": {
            "benchlm": {"overall": 79.68, "inputPrice": 5, "outputPrice": 25}
        },
        "oca": ["anthropic", "claude-opus-5"],
    },
    "autocat-runtime-$ENV$-llm-claude-sonnet-4_5": {
        "env": "databricks",
        "limits": {"max_tokens": 64000},
        "benchmarks": {"benchlm": {"overall": 0}},
        "oca": ["anthropic", "claude-sonnet-4-5"],
    },
    "autocat-runtime-$ENV$-llm-claude-sonnet-4_6": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "benchmarks": {"benchlm": {"overall": 0}},
        "oca": ["anthropic", "claude-sonnet-4-6"],
    },
    "autocat-runtime-$ENV$-llm-gpt4o": {
        "env": "databricks",
        "limits": {"max_tokens": 16384},
        "benchmarks": {"benchlm": {"overall": 0}, "oca": ["azure", "gpt-4o-1120"]},
    },
    "autocat-runtime-$ENV$-llm-gpt4o-mini": {
        "env": "databricks",
        "limits": {"max_tokens": 16384},
        "benchmarks": {
            "benchlm": {"overall": 25.73, "inputPrice": 0.15, "outputPrice": 0.60}
        },
        "oca": ["azure", "gpt-4o-mini-0718"],
    },
    "autocat-runtime-$ENV$-llm-gpt5": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "benchmarks": {"benchlm": {"overall": 0}},
        "oca": ["azure", "gpt-5"],
    },
    "autocat-runtime-$ENV$-llm-gpt5_1": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "benchmarks": {"benchlm": {"overall": 0}},
        "oca": ["azure", "gpt-5.1"],
    },
    "autocat-runtime-$ENV$-llm-gpt5_4": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "benchmarks": {
            "benchlm": {"overall": 66.4, "inputPrice": 2.5, "outputPrice": 15}
        },
        "oca": ["azure", "gpt-5.4"],
    },
    "autocat-runtime-$ENV$-llm-gpt5_5": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "oca": ["azure", "gpt-5.5"],
        "benchmarks": {
            "benchlm": {"overall": 68.82, "inputPrice": 5, "outputPrice": 30}
        },
    },
    "autocat-runtime-$ENV$-llm-gpt5_6-luna": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "benchmarks": {
            "benchlm": {"overall": 63.8, "inputPrice": 0.2, "outputPrice": 1.2}
        },
        "oca": ["azure", "gpt-5.5"],
    },
    "autocat-runtime-$ENV$-llm-gpt5_6-sol": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "benchmarks": {
            "benchlm": {"overall": 74.83, "inputPrice": 4, "outputPrice": 20}
        },
        "oca": ["azure", "gpt-5.6-sol"],
    },
    "autocat-runtime-$ENV$-llm-gpt5_6-terra": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "benchmarks": {
            "benchlm": {"overall": 69.81, "inputPrice": 2, "outputPrice": 12}
        },
        "oca": ["azure", "gpt-5.6-terra"],
    },
    "autocat-runtime-$ENV$-llm-gpt5-mini": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "benchmarks": {
            "benchlm": {"overall": 47.92, "inputPrice": 0.25, "outputPrice": 2}
        },
        "oca": ["azure", "gpt-5-mini"],
    },
    "autocat-runtime-$ENV$-llm-gpt5-nano": {
        "env": "databricks",
        "limits": {"max_tokens": 128000},
        "benchmarks": {"benchlm": {"overall": 0}},
        "oca": ["azure", "gpt-5-mini"],
    },
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

    return [deployment.replace("$ENV$", sub_env) for deployment in MODEL_INFO.keys()]


def get_model_info(model_deployment_name):

    if "create-1c" in model_deployment_name:
        key = model_deployment_name.replace("create-1c", "$ENV$")
    elif "accept-2a" in model_deployment_name:
        key = model_deployment_name.replace("accept-2a", "$ENV$")
    elif "publish-3p" in model_deployment_name:
        key = model_deployment_name.replace("publish-3p", "$ENV$")
    else:
        raise Exception(f"unsupported deploymeny_id: {model_deployment_name}")

    return MODEL_INFO[key]
