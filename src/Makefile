# Makefile at /src
BMFONT = bmfont64.exe
PYTHON = python3
FNTNAME = TamaTou
FNTS = $(FNTNAME)12cond.fnt $(FNTNAME)20aa.fnt $(FNTNAME)20aab.fnt $(FNTNAME)20b.fnt $(FNTNAME)24aa.fnt $(FNTNAME)24aab.fnt
DST = ../mod/graphics/fonts/

.PHONY: all bmfc fnt install clean clean-fnt clean-bmfc clean-install
.SUFFIXES: .fnt .bmfc

all: bmfc fnt

.bmfc.fnt:
	$(BMFONT) -c $< -o $@
	$(PYTHON) fixface.py $@

bmfc: bmfcgen.json
	$(PYTHON) bmfcgen.py

fnt: bmfc $(FNTS)

install: clean-install
	mv $(FNTNAME)12cond.fnt $(DST)orbitron12condensed.fnt
	mv $(FNTNAME)20aa.fnt $(DST)orbitron20aa.fnt
	mv $(FNTNAME)20aab.fnt $(DST)orbitron20aabold.fnt
	mv $(FNTNAME)20b.fnt $(DST)orbitron20bold.fnt
	mv $(FNTNAME)24aa.fnt $(DST)orbitron24aa.fnt
	mv $(FNTNAME)24aab.fnt $(DST)orbitron24aabold.fnt
	mv *.png $(DST)

clean: clean-fnt clean-bmfc

clean-fnt:
	rm -f *.fnt *.png

clean-bmfc:
	rm -f *.bmfc

clean-install:
	rm -f $(DST)*fnt $(DST)*.png
