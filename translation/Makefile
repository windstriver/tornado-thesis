# LaTeX Makefile
FILE=translation_geometry

all: $(FILE).pdf

.PHONY: clean
clean:
	\rm *.aux *.blg *.out *.log *.bbl *.bcf *.synctex.gz

$(FILE).tex:

$(FILE).bib:

$(FILE).pdf: $(FILE).tex $(FILE).bib
	xelatex $(FILE).tex
	biber $(FILE)
	xelatex $(FILE).tex

.PHONY: view
view:
	evince $(FILE).pdf &
