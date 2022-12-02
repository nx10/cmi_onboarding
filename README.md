# CMI onboarding challanges

## Solutions

- "1. What is this?"
  - [inspect_files.ipynb](inspect_files.ipynb)
- "2. When given ____, show us ____."
  - The complete configuration used and its differences from the default pipeline
    - [configs.ipynb](configs.ipynb)
  - The a) longest and b) most memory-consuming tasks in the pipeline
    - [log_parsing.ipynb](log_parsing.ipynb)
  - All quality control (QC) plots generated throughout executions
    - [qc_plots.ipynb](qc_plots.ipynb)
  - When given voxelwise time series data, show us...
    - [voxel.ipynb](voxel.ipynb)
  - When given vertexwise time series and surface data, show us...
    - [surface.ipynb](surface.ipynb)
  - When given a BIDS input dataset, show us...
    - [cpac_proc.ipynb](cpac_proc.ipynb)
    - [cpac_run_proof](cpac_run_proof)


## Local execution / reproduction

Each notebook defines a data root (`DATA_ROOT`) variable that should 
be set to a directory containing the onboarding data.

Atlases and other third party data are downloaded dynamically to 
`DIR_TEMP` in some notebooks.

### Python dependencies

```
numpy==1.23.4
nibabel==4.0.2
nilearn==0.9.2
hcp_utils==0.1.0
seaborn==0.12.1
cpac==0.5.0
```