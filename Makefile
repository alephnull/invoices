# Makefile

pdf: gen $(patsubst %.tex,%.pdf,$(wildcard *.tex))

gen: 
	python3 generate-invoice.py

%.pdf: %.tex dapper-invoice.cls
	xelatex $< && xelatex $< #Twice for references

install: dapper-invoice.cls
	mkdir -p "$$(kpsewhich -expand-var '$$TEXMFHOME')/tex/latex/base"
	cp -a $? "$$(kpsewhich -expand-var '$$TEXMFHOME')/tex/latex/base/"

uninstall:
	rm -f "$$(kpsewhich -expand-var '$$TEXMFHOME')/tex/latex/base/dapper-invoice.cls"

clean:
	rm -fv *.aux *.log *.out

realclean: clean
	rm -fv *.pdf

.PHONY : install uninstall clean realclean
