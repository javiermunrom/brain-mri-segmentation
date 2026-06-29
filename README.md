# Brain MRI Segmentation

> Deep Learning project focused on semantic segmentation of brain MRI scans using PyTorch and MONAI.

This repository documents the development of a complete medical image segmentation pipeline, from data exploration and preprocessing to model training, evaluation and inference.

The main objective of this project is to gain hands-on experience with modern deep learning techniques for volumetric medical image analysis while following clean software engineering practices and building a high-quality portfolio project.

---

## Features

- 3D Brain MRI segmentation
- Medical image visualization
- NIfTI volume processing
- PyTorch training pipeline
- MONAI integration
- Data augmentation
- Model evaluation
- Experiment reproducibility
- Modular project structure

---

## Objectives

- Learn state-of-the-art medical image segmentation techniques.
- Understand the complete workflow of volumetric medical imaging.
- Build reproducible Deep Learning pipelines.
- Follow professional software engineering practices.
- Develop a high-quality portfolio project focused on AI for healthcare.

---

## Technologies

- Python
- PyTorch
- MONAI
- NumPy
- pandas
- Matplotlib
- NiBabel
- SimpleITK
- OpenCV
- scikit-image
- scikit-learn
- Jupyter Notebook

---

## Repository Structure

```text
brain-mri-segmentation/
│
├── configs/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── interim/
│   └── external/
│
├── docs/
├── models/
├── notebooks/
├── outputs/
│   ├── figures/
│   ├── logs/
│   └── predictions/
│
├── scripts/
│
├── src/
│   ├── dataset.py
│   ├── transforms.py
│   ├── model.py
│   ├── losses.py
│   ├── metrics.py
│   ├── train.py
│   ├── inference.py
│   ├── visualize.py
│   ├── utils.py
│   └── __init__.py
│
├── tests/
│
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── .editorconfig
├── .gitattributes
├── .pre-commit-config.yaml
└── LICENSE
```

---

## Dataset

This repository **does not include** the BraTS dataset.

To reproduce the experiments:

1. Register for the official BraTS Challenge.
2. Request access to the dataset.
3. Download the MRI volumes.
4. Place the dataset inside:

```text
data/raw/
```

The dataset remains subject to the BraTS license and terms of use.

---

## Installation

```bash
git clone https://github.com/javmunrom/brain-mri-segmentation.git

cd brain-mri-segmentation

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt

pre-commit install
```

---

## Current Roadmap

### Phase 1 — Dataset Exploration

- [ ] Explore the BraTS dataset
- [ ] Understand the NIfTI format
- [ ] Visualize MRI slices
- [ ] Visualize segmentation masks
- [ ] Inspect MRI modalities (T1, T1ce, T2, FLAIR)

---

### Phase 2 — Data Pipeline

- [ ] Implement custom Dataset
- [ ] Implement DataLoader
- [ ] Data preprocessing
- [ ] Data normalization
- [ ] Data augmentation

---

### Phase 3 — Model Development

- [ ] Baseline U-Net
- [ ] 3D U-Net
- [ ] Attention U-Net
- [ ] MONAI architectures
- [ ] Hyperparameter tuning

---

### Phase 4 — Training & Evaluation

- [ ] Training pipeline
- [ ] Validation pipeline
- [ ] Dice Score
- [ ] IoU
- [ ] Hausdorff Distance
- [ ] Model checkpointing
- [ ] Early stopping

---

### Phase 5 — Inference

- [ ] Prediction pipeline
- [ ] Volume reconstruction
- [ ] Visualization of predictions
- [ ] Performance comparison

---

### Phase 6 — Documentation

- [ ] Improve documentation
- [ ] Add examples
- [ ] Document experiments
- [ ] Publish project results

---

## Branching Strategy

The project follows a Git workflow based on feature branches.

```
main
│
└── develop
     ├── feature/preprocessing
     ├── feature/visualization
     ├── feature/dataset
     ├── feature/training
     ├── feature/inference
     └── feature/documentation
```

- `main` contains only stable versions.
- `develop` contains the latest integrated development.
- New work is implemented in dedicated `feature/*` branches.
- Features are merged into `develop` through Pull Requests.
- Stable releases are merged from `develop` into `main`.

---

## References

- BraTS Challenge
- MONAI Framework
- PyTorch Documentation
- NiBabel Documentation
- SimpleITK Documentation
- U-Net: Convolutional Networks for Biomedical Image Segmentation (Ronneberger et al., 2015)

---

## License

This project is licensed under the MIT License.
