# import mlflow
# from mlflow.tracking import MlflowClient

# # Initialize MLflow client
# client = MlflowClient()

# # Check all experiments including deleted ones
# print("=== Active Experiments ===")
# experiments = client.search_experiments(view_type=mlflow.entities.ViewType.ACTIVE_ONLY)
# for exp in experiments:
#     print(f"Name: {exp.name}, ID: {exp.experiment_id}")

# print("\n=== Deleted Experiments ===")
# deleted_experiments = client.search_experiments(view_type=mlflow.entities.ViewType.DELETED_ONLY)
# for exp in deleted_experiments:
#     print(f"Name: {exp.name}, ID: {exp.experiment_id}")


import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Get experiment by name
experiment = client.get_experiment_by_name("random-forest-hyperopt")

if experiment:
    # First mark as deleted if not already deleted
    client.delete_experiment(experiment.experiment_id)
    # Then permanently delete
    print(f"Deleting experiment {experiment.experiment_id}")
    mlflow.tracking.utils._get_store().delete_experiment_permanently(experiment.experiment_id)