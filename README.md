# Deploy Azure Function App locally
execute the command below in your terminal (root level)
```bash
func azure functionapp publish "HeinekenApp" --python
```

# Change Management with Azure DevOps
See "ReleasePipeline-pipeline.yml" file and files in folder "pipelines" for the definitions for a build & release pipeline for the timer trigger function.