FROM texlive/texlive:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl poppler-utils \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 --branch master https://github.com/TLCFEM/introduction-to-structural-steel.git /workspace

WORKDIR /workspace

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin/:$PATH"

RUN uv venv .venv && uv pip install -r requirements.txt && \
    uv run python CHARTS.py && \
    uv run python GENERATOR.py && \
    latexmk -pdf INTRO.tex && \
    latexmk -pdf IMAGES.tex && \
    uv run python CONVERTER.py
