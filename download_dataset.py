import os

# Set Kaggle API key location inside Project_water
os.environ["KAGGLE_CONFIG_DIR"] = os.path.abspath(".")

# Install Kaggle (if not already installed)
os.system("pip install kaggle")

# Define dataset and download path
dataset_name = "glendell03/water-hyacinth"
output_path = "datasets"

# Create dataset directory
os.makedirs(output_path, exist_ok=True)

# Run Kaggle API to download dataset
os.system(f"kaggle datasets download -d {dataset_name} -p {output_path} --unzip")

print(f"✅ Dataset downloaded to: {output_path}")
