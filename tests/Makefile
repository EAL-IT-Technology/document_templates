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
