python3 -m venv ~/.udacity-devops
source ~/.udacity-devops/bin/activate
az webapp up --sku F1 -n azure-devops-service
az webapp log tail --name azure-devops-service