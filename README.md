<div align="center">

# Introduction to Structural Steel

**A Textbook on the Design of Steel Structures**

*Department of Civil and Natural Resources Engineering*<br/>
University of Canterbury &nbsp;·&nbsp; Christchurch, New Zealand

<br/>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5513880.svg)](https://doi.org/10.5281/zenodo.5513880)
[![Licence: CC BY-NC-ND 4.0](https://img.shields.io/badge/Licence-CC%20BY--NC--ND%204.0-1F3A5F?style=flat-square)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Build](https://github.com/TLCFEM/introduction-to-structural-steel/actions/workflows/pdf.yml/badge.svg)](https://github.com/TLCFEM/introduction-to-structural-steel/actions/workflows/pdf.yml)
[![Typeset in LaTeX](https://img.shields.io/badge/Typeset-LaTeX-0B7285?style=flat-square&logo=latex&logoColor=white)](https://www.latex-project.org/)

</div>

---

## Preface

This repository contains the complete source of *Introduction to Structural Steel*, a textbook for students of civil and structural engineering.
The text develops the theory and practice of steel member and connection design, illustrates the governing principles with worked examples, and relates them throughout to the relevant Australian/New Zealand standards.

The book is typeset in LaTeX and is accompanied by programmatically generated design charts and a collection of editable SMath Studio worksheets.
The manuscript, figures, and supporting scripts are maintained together under version control so that the published volume can be rebuilt directly from this repository.

**Principal features**

- **Comprehensive coverage** — design philosophy, material behaviour, tension and compression members, bending members, bolted and welded connections, and eccentric connections.
- **Standards-based treatment** — direct reference to NZS 3404, the AS/NZS 3679 and 3678 series, AS/NZS 1163, AS/NZS 1252.1, AS/NZS 1170.0, AS/NZS 4855, and ANSI/AISC 360-16.
- **Worked examples and worksheets** — hand-calculation examples supported by editable SMath Studio worksheets for checking and exploration.
- **Reproducible production** — a scripted toolchain generates the design charts and figure catalogue, and a containerised reference build reproduces the complete set of deliverables.
- **Open scholarly access** — the book is openly available under a Creative Commons licence and has a persistent DOI for citation.

## Contents

| Part | Chapter | Title | Scope |
|:----:|:-------:|:------|:------|
| I | 0 | Preface | Standards, additional resources, and guidance for using the book |
| I | 1 | Design | Design process, strength and serviceability approaches, and calculation accuracy |
| I | 2 | Material | Sustainability, steel properties, structural shapes, tolerances, and undesirable behaviour |
| I | 3 | Tension Members | Strength design, net area, distribution factors, and slenderness limitations |
| I | 4 | Compression Members | Elastic and local buckling, section and member capacity, and effective length |
| I | 5 | Bending Members | Limit states, flexural strength, shear, bearing, and biaxial loading |
| I | 6 | Bolted Connections | Connection and connector types, bolt behaviour, strength design, and serviceability |
| I | 7 | Welded Connections | Joint and weld types, symbols, processes, strength, defects, and member design |
| II | 8 | Eccentric Connections | Elastic and ultimate strength methods for bolted and welded eccentric connections |
| III | — | Appendix | Structural Steel Weld Specification and Implementation |

The volume also includes the *Liberty Steel Hot Rolled and Structural Steel Product* manual as an appendix, together with design charts for commonly used sections.

## Bibliographic Record

| | |
|:------------------|:------|
| **Title** | Introduction to Structural Steel |
| **Authors** | Dr. Gregory MacRae; Dr. Theodore Chang |
| **Institution** | Department of Civil and Natural Resources Engineering, University of Canterbury |
| **Publisher** | University of Canterbury, Christchurch, New Zealand |
| **DOI** | [10.5281/zenodo.5513880](https://doi.org/10.5281/zenodo.5513880) |
| **Licence** | [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) |
| **Source control** | [github.com/TLCFEM/introduction-to-structural-steel](https://github.com/TLCFEM/introduction-to-structural-steel) |

## Building the Book

### Prerequisites

- Python 3 with `pip`
- A TeX Live installation providing `latexmk` and the packages imported by `HEADER.tex`
- `poppler-utils`, required by `CONVERTER.py` for rasterising figures

The design charts must be generated before the book is compiled for the first time.

### 1. Generate the Design Charts

```bash
python3 -m pip install -r requirements.txt
python3 ./CHARTS.py
```

The charts are written into the `REF` directory and are included by the manuscript.

### 2. Typeset the Book

```bash
latexmk -pdf INTRO.tex
```

The resulting volume is `INTRO.pdf`.

## Collecting the Figures

All figures are stored under the `PIC` folder.
A variety of formats is used, including `.png`, `.svg`, `.pdf`, `.jpg`, and native LaTeX/TikZ sources.

A three-stage scripted workflow assembles every figure into a single catalogue:

```bash
# Collect all .tex figures in the book
python3 ./GENERATOR.py

# Compile the figure catalogue
latexmk -pdf IMAGES.tex

# Convert each page to a PNG image and package the archives
python3 ./CONVERTER.py
```

`GENERATOR.py` writes `IMAGES.tex`; `CONVERTER.py` rasterises `IMAGES.pdf` at 300 dpi and produces `IMAGES.zip` and `WORKSHEET.zip`.
See the [CI/CD workflow](.github/workflows/pdf.yml) for the complete automated procedure.

## Reference Build

The following procedure builds every deliverable in a reproducible Docker environment.
It requires `docker` and `curl`.

```bash
mkdir -p enci336
curl -fsSL https://raw.githubusercontent.com/TLCFEM/introduction-to-structural-steel/master/dockerfile -o enci336/dockerfile

docker build -f enci336/dockerfile -t enci336 enci336

cid=$(docker create enci336)
docker cp "$cid:/workspace/INTRO.pdf" ./enci336/
docker cp "$cid:/workspace/IMAGES.pdf" ./enci336/
docker cp "$cid:/workspace/IMAGES.zip" ./enci336/
docker cp "$cid:/workspace/WORKSHEET.zip" ./enci336/
docker rm "$cid" >/dev/null
```

The build outputs are placed in `enci336/`.

## Repository Organisation

| Path | Description |
|:---------------------|:------------|
| `INTRO.tex` | Main document; assembles the front matter, chapters, appendix, and bibliography |
| `TITLE.tex` | Title page, copyright statement, and running-head configuration |
| `HEADER.tex` | Preamble: packages, macros, theorem environments, and standard references |
| `CHAPTER/` | Chapter sources, `CH00.tex` through `CH08.tex`, and the appendix `WSI.tex` |
| `PIC/` | All figures, grouped by chapter and including native TikZ sources |
| `REF/` | Reference documents, section property data, and generated design charts |
| `WORKSHEET/` | SMath Studio worksheets accompanying selected worked examples |
| `BIB.bib` | Bibliography database |
| `CHARTS.py` | Generates the design charts used in the book |
| `GENERATOR.py` | Assembles all figures into the standalone `IMAGES.tex` catalogue |
| `CONVERTER.py` | Rasterises the figure catalogue and creates the distributed archives |
| `dockerfile` | Reproducible container definition for the complete build |
| `.github/workflows/pdf.yml` | Continuous integration, compilation, and release workflow |

## Continuous Integration

The [PDF workflow](.github/workflows/pdf.yml) rebuilds the book, the figure catalogue, and the worksheet archive on every push.
The resulting files — `INTRO.pdf`, `IMAGES.pdf`, `IMAGES.zip`, and `WORKSHEET.zip` — are published to the [`latest` release](https://github.com/TLCFEM/introduction-to-structural-steel/releases/tag/latest).

## Branching and Versioning

> [!WARNING]
> The `master` branch is regularly updated **after** each semester.
> For the latest version of the current semester, please use the corresponding revision branch.

Revision branches follow the `revision-*` naming convention (for example, `revision-2026`).
Readers who require a stable, citable version should consult the DOI record or the appropriate revision branch rather than `master`.

## Citation

If you use this book in your teaching, research, or professional practice, please cite it as:

```bibtex
@Book{MacRae2021,
  author    = {MacRae, Gregory and Chang, Theodore},
  publisher = {University of Canterbury},
  title     = {Introduction to Structural Steel},
  year      = {2021},
  address   = {Christchurch, NZ},
  month     = sep,
  doi       = {10.5281/zenodo.5513881},
  url       = {https://doi.org/10.5281/zenodo.5513881},
}
```

## Licence

The book and its associated materials are released under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Licence](https://creativecommons.org/licenses/by-nc-nd/4.0/).
You are free to share the work for non-commercial purposes with appropriate attribution; no derivatives may be distributed.
The full licence text is available in [`LICENSE`](LICENSE).

## Comments and Suggestions

Comments, corrections, and suggestions are welcome.
Please report invalid links, typographical errors, or technical issues by opening an [issue](https://github.com/TLCFEM/introduction-to-structural-steel/issues).

Readers familiar with LaTeX are encouraged to contribute improvements by submitting a pull request.

---

<div align="center">

*Department of Civil and Natural Resources Engineering*<br/>
*University of Canterbury &nbsp;·&nbsp; Christchurch, New Zealand*

</div>
