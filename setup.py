from setuptools import setup, find_packages

setup(
      name='genie',
      version='0.0.2',
      description='de novo protein design through equivariantly diffusing oriented residue clouds',
      packages=find_packages(where="genie",
                             include=["*"]),#['genie'],
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
