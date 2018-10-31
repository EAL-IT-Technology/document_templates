GIT_DATE := $(shell date -d $$(date -d @$$(git log -1 --format=%ct) +"%Y%m%d") +%s)

all: test.pdf test-notoc.pdf

test.pdf: test.md template/template.tex
	SOURCE_DATE_EPOCH=$(GIT_DATE)   \
	pandoc                          \
	  --from         markdown       \
	  --to           latex          \
	  --template     template/template.tex   \
	  --out          test.pdf       \
	  --pdf-engine   pdflatex       \
	  test.md

test-notoc.pdf: test.md template/template.tex
	SOURCE_DATE_EPOCH=$(GIT_DATE)   \
	pandoc                          \
	  --from         markdown       \
	  --to           latex          \
	  --template     template/template.tex   \
	  --out          test-notoc.pdf \
	  --pdf-engine pdflatex         \
	  --variable="skip-toc=true"    \
	  test.md

tex-only: test.tex test-notoc.tex

test.tex: test.md template/template.tex
	pandoc                          \
	  --from         markdown       \
	  --to           latex          \
	  --template     template/template.tex   \
	  --out          test.tex       \
	  test.md

test-notoc.tex: test.md template/template.tex
	pandoc                          \
	  --from         markdown       \
	  --to           latex          \
	  --template     template/template.tex   \
	  --out          test-notoc.tex \
	  --variable="skip-toc=true"    \
	  test.md


