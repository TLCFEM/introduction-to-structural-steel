# Introduction to Structural Steel

This is the official repository of the book `Introduction to Structural Steel`.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5513880.svg)](https://doi.org/10.5281/zenodo.5513880)

> [!WARNING]
> The `master` branch is regularly updated __after__ each semester.
> For the latest version of the current semester, please go to the corresponding revision branch.

## To Compile

In order to compile the book, one needs to generate some design charts.

```bash
python3 -m pip install -r requirements.txt
python3 ./CHARTS.py
```

Then, use `latexmk` to compile the book.

```bash
latexmk -pdf INTRO.tex
```

## To Collect Figures

All figures are stored under the `./PIC` folder. Various forms are used, including `.png`, `.svg`, `.pdf`, `.jpg` 
and some others.

A script is provided to collect all `.tex` figures in the book.

```bash
# collect all .tex files in the book
python3 ./GENERATOR.py
# compile the tex file 
latexmk -pdf IMAGES.tex
# convert each page to a png file
python3 ./CONVERTER.py
```

See [CI/CD](.github/workflows/pdf.yml) for more details.

## Comments/Suggestions

Any comments/suggestions are welcome. Please feel free to suggest improvements by creating new issues.

If you are familiar with LaTeX, pull requests can be created if you are willing to contribute.
