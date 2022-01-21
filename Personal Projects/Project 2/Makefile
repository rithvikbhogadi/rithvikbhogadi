PY = python3
PYFLAGS = 
PYTEST = pytest
PYTESTFLAGS = --cov
DOXY = doxygen
DOCFLAGS = 
DOXYCFG = doxConfig

PYTESTIGNORE = --ignore $(SRCEXPT)
SRC = src
SRCEXPT = src/test_expt.py

RMDIR = rm -rf

.PHONY: test doc clean report

test:
	$(PYTEST) $(PYTESTFLAGS) $(SRC) $(PYTESTIGNORE)

expt: 
	$(PY) $(PYFLAGS) $(SRCEXPT)

doc:
	$(DOXY) $(DOXYCFG)
	cd latex && $(MAKE)

report:
	cd report && $(MAKE)

clean:
	@- $(RMDIR) html
	@- $(RMDIR) latex
