
# Listar todos los workspaces en un grupo de recursos
az ml workspace list --resource-group my-resource-group


# Crear un compute
az ml compute create --name test-compute --size STANDARD_DS11_v2 --min-instances 0 --max-instances 5 --type AmlCompute --resource-group lil-desarrollando-modelos --workspace-name lil-azureml


# Ejemplos de comandos:
az ml job create --file my_job_definition.yaml
az ml environment update --name my-env --file my_updated_env_definition.yaml
az ml model list
az ml compute show --name my_compute