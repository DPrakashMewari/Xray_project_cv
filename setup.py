from setuptools import find_packages,setup



setup(
name = "Xray",
version=0.0.1,
author='Prakash',
author_email='Prakash.mewari@yahoo.com',
install_requires=[
  "bentoml==1.0.25",
  "joblib==1.2.0",
  "pip-chill==1.0.1",
  "torchvision==0.14.1",
  "tqdm==4.64.1",
  "wincertstore==0.2",
  "dvc",
  "mlflow",
  "ipykernel",
  "pandas",
  "numpy",
  "seaborn",
  "pytest==7.1.3",
  "tox==3.25.1",
  "black==22.8.0",
  "flake8==5.0.4",
  "mypy==0.971"
],
package=find_packages()
)