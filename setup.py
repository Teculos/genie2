from setuptools import setup, find_namespace_packages, find_packages

setup(
      name='genie',
      version='0.0.2',
      description='de novo protein design through equivariantly diffusing oriented residue clouds',
      packages=find_packages(),
      install_requires=[
            'tqdm',
            'numpy',
            'torch',
            'scipy',
            'wandb',
            'tensorboard',
            'pytorch_lightning',
      ],
)
