# Brain MRI Segmentation

Proyecto de Deep Learning para segmentacion de resonancias magneticas cerebrales (MRI) orientado a portfolio profesional y base de investigacion reproducible con PyTorch y MONAI.

## Descripcion

Este repositorio esta disenado como una base de trabajo limpia, escalable y mantenible para experimentar con pipelines de segmentacion medica, desde la exploracion del dataset y el preprocesado hasta el entrenamiento, la validacion y la inferencia sobre volumenes 3D.

## Objetivos

- Construir un pipeline profesional para segmentacion de MRI cerebrales.
- Estandarizar el trabajo con datos medicos volumetricos.
- Integrar PyTorch y MONAI para investigacion y prototipado rapido.
- Mantener una estructura compatible con buenas practicas de ingenieria y MLOps ligero.
- Servir como portfolio tecnico para proyectos de Computer Vision e imagen medica.

## Tecnologias

- Python
- PyTorch
- MONAI
- NumPy
- Matplotlib
- NiBabel
- SimpleITK
- OpenCV
- scikit-image
- scikit-learn
- pandas
- Jupyter

## Arquitectura Del Proyecto

El repositorio separa claramente configuracion, datos, codigo fuente, artefactos generados, documentacion y notebooks. El codigo en `src/` se organiza por responsabilidad: carga de datos, transformaciones, definicion del modelo, funciones de perdida, metricas, entrenamiento, inferencia, visualizacion y utilidades compartidas.

## Dataset

El dataset BraTS no esta incluido en este repositorio.

Para utilizarlo, debe solicitarse acceso desde el challenge oficial correspondiente de BraTS y descargarse de acuerdo con sus terminos de uso y licencia. Una vez obtenido, los archivos deben colocarse localmente dentro de `data/raw/` o en la estructura que se documente en `configs/` y `docs/`.

## Instalacion

```bash
git clone https://github.com/<tu-usuario>/brain-mri-segmentation.git
cd brain-mri-segmentation
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pre-commit install
```

## Uso

Ejemplos iniciales de flujo de trabajo:

```bash
python -m src.train
python -m src.inference
python -m src.visualize
```

Los scripts y configuraciones se iran consolidando conforme se implementen los modulos funcionales del pipeline.

## Estructura Del Repositorio

```text
brain-mri-segmentation/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── .editorconfig
├── .gitattributes
├── .pre-commit-config.yaml
├── configs/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── interim/
│   └── external/
├── docs/
├── models/
├── notebooks/
├── outputs/
│   ├── figures/
│   ├── predictions/
│   └── logs/
├── scripts/
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
└── tests/
```

## Roadmap

- [ ] Explorar dataset
- [ ] Visualizar MRI
- [ ] Visualizar mascaras
- [ ] Dataset PyTorch
- [ ] DataLoader
- [ ] Data Augmentation
- [ ] U-Net 3D
- [ ] Entrenamiento
- [ ] Validacion
- [ ] Dice Score
- [ ] Inferencia
- [ ] Visualizacion de resultados
- [ ] MONAI Integration
- [ ] Comparacion de modelos

## Referencias

- BraTS Challenge
- PyTorch Documentation
- MONAI Documentation
- NiBabel Documentation
- SimpleITK Documentation

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulte `LICENSE` para mas informacion.
